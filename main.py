from fastapi import FastAPI
from db.base import database
from endpoints import users, auth, jobs
import uvicorn


app = FastAPI(title='Employment_exchange')
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(jobs.router, prefix='/jobs', tags=['jobs'])

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)