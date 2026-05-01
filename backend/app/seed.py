from .database import SessionLocal,Base,engine
from .models import User,Employee
from .security import hash_password

USERS=[('admin@example.com','Admin'),('hr@example.com','HR Admin'),('it@example.com','IT Admin'),('security@example.com','Security Admin'),('grc@example.com','GRC Analyst'),('auditor@example.com','Auditor'),('manager@example.com','Manager')]

def run():
    Base.metadata.create_all(bind=engine)
    db=SessionLocal()
    if db.query(User).count()==0:
        for email,role in USERS:
            db.add(User(name=role,email=email,password_hash=hash_password('password123'),role=role))
        for i in range(1,21):
            db.add(Employee(employee_number=f'E{i:04d}',first_name=f'Emp{i}',last_name='Demo',email=f'emp{i}@example.com',department='Engineering',employment_type='full_time',status='active'))
        db.commit()
    db.close()

if __name__=='__main__': run()
