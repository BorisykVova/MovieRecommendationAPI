import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def health_check():
    return {
        'status': 'I am alive!'
    }


if __name__ == '__main__':
    uvicorn.run('runserver:app', port=8001, reload=True)
