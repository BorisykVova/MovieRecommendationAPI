import uvicorn
from fastapi import FastAPI

import database

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.setup()


@app.on_event('shutdown')
async def shutdown():
    await database.shutdown()


@app.get('/')
async def health_check():
    return {
        'status': 'I am alive!'
    }


if __name__ == '__main__':
    uvicorn.run('runserver:app', port=8001, reload=True)
