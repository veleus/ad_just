from celery import Celery 
from db import pg_engine
from database.database import Tasks
import uuid

app = Celery('tasks', broker='pyamqp://guest@localhost//')
@app.task
def add_quque(*args):

    exp = Tasks(id=uuid.uuid4(), name=args[0],description=args[1],data_start=args[2],data_end=args[3])
    pg_engine.add(exp)
    pg_engine.commit()
    pg_engine.refresh(exp)  

    return exp
    
    
