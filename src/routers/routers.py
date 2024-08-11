from fastapi import APIRouter
from db import pg_engine
from dto.model import Tasks as Tasks_model
from database.database import Tasks
from message.tasks import add_quque
router = APIRouter()

@router.get('/get/{id}')
async def tasks(id:int):
    return pg_engine.query(Tasks).filter(Tasks.id == id).first()


@router.post('/tasks/')
async def add_tasks(data: Tasks_model):
    result = add_quque.delay(data.name, data.description, data.data_start, data.data_end)
    return f'{result.id}'

@router.get('/all/')
async def all_tasks():
    return pg_engine.query(Tasks).all()


