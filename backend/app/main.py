from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt,JWTError
from .database import Base,engine,get_db
from .models import User,Employee,Workflow,Task,AuditLog
from .security import hash_password,verify_password,create_token,ALGO
from .config import SECRET_KEY

app=FastAPI(title='employee-lifecycle-automation-governance-agent')
Base.metadata.create_all(bind=engine)
oauth2=OAuth2PasswordBearer(tokenUrl='/auth/login')

def current_user(token:str=Depends(oauth2),db:Session=Depends(get_db)):
    try: email=jwt.decode(token,SECRET_KEY,algorithms=[ALGO]).get('sub')
    except JWTError: raise HTTPException(401,'invalid token')
    user=db.query(User).filter(User.email==email).first()
    if not user: raise HTTPException(401,'not found')
    return user

@app.get('/health')
def health(): return {'status':'ok'}

@app.post('/auth/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    u=db.query(User).filter(User.email==form_data.username).first()
    if not u or not verify_password(form_data.password,u.password_hash): raise HTTPException(401,'bad creds')
    return {'access_token':create_token(u.email),'token_type':'bearer'}

@app.get('/auth/me')
def me(user=Depends(current_user)): return {'email':user.email,'role':user.role,'name':user.name}

@app.get('/employees')
def employees(user=Depends(current_user),db:Session=Depends(get_db)):
    return db.query(Employee).all()

@app.post('/employees')
def create_employee(payload:dict,user=Depends(current_user),db:Session=Depends(get_db)):
    if user.role not in ['Admin','HR Admin']: raise HTTPException(403,'forbidden')
    e=Employee(**payload); db.add(e); db.commit(); db.refresh(e)
    db.add(AuditLog(actor_user_id=user.id,action='create_employee',entity_type='Employee',entity_id=str(e.id)))
    db.commit()
    return e

@app.post('/lifecycle/onboarding')
def onboarding(payload:dict,user=Depends(current_user),db:Session=Depends(get_db)):
    e=db.get(Employee,payload['employee_id'])
    wf=Workflow(employee_id=e.id,workflow_type='onboarding',risk_score=20)
    db.add(wf); db.commit(); db.refresh(wf)
    for t in ['Confirm HR record','Manager approval','Create identity account','Assign baseline application access','Issue laptop','Generate onboarding evidence package']:
        db.add(Task(workflow_id=wf.id,title=t,owner_team='IT'))
    db.commit(); return {'workflow_id':wf.id}

@app.get('/workflows')
def workflows(user=Depends(current_user),db:Session=Depends(get_db)):
    return db.query(Workflow).all()
