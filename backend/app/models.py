from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,Boolean,Text
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String,unique=True,index=True)
    password_hash=Column(String)
    role=Column(String,index=True)
    department=Column(String,default='General')
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,server_default=func.now())

class Employee(Base):
    __tablename__='employees'
    id=Column(Integer,primary_key=True)
    employee_number=Column(String,unique=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String)
    department=Column(String)
    manager_id=Column(Integer,ForeignKey('users.id'),nullable=True)
    employment_type=Column(String)
    status=Column(String,default='active')

class Workflow(Base):
    __tablename__='workflows'
    id=Column(Integer,primary_key=True)
    employee_id=Column(Integer,ForeignKey('employees.id'))
    workflow_type=Column(String)
    status=Column(String,default='active')
    risk_score=Column(Integer,default=0)

class Task(Base):
    __tablename__='tasks'
    id=Column(Integer,primary_key=True)
    workflow_id=Column(Integer,ForeignKey('workflows.id'))
    title=Column(String)
    owner_team=Column(String)
    status=Column(String,default='pending')

class AuditLog(Base):
    __tablename__='audit_logs'
    id=Column(Integer,primary_key=True)
    actor_user_id=Column(Integer,nullable=True)
    action=Column(String)
    entity_type=Column(String)
    entity_id=Column(String)
    before_json=Column(Text,nullable=True)
    after_json=Column(Text,nullable=True)
    created_at=Column(DateTime,server_default=func.now())
