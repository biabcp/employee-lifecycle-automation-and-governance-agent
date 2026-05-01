from datetime import datetime,timedelta,timezone
from jose import jwt
from passlib.context import CryptContext
from .config import SECRET_KEY
ALGO='HS256'
pwd=CryptContext(schemes=['bcrypt'],deprecated='auto')

def hash_password(p:str): return pwd.hash(p)
def verify_password(p,h): return pwd.verify(p,h)
def create_token(sub:str):
    return jwt.encode({'sub':sub,'exp':datetime.now(timezone.utc)+timedelta(hours=24)},SECRET_KEY,algorithm=ALGO)
