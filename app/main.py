from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.routers import post

app = FastAPI()
settings = get_settings()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router, tags=['Posts'], prefix='/api/posts')


@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello World'}
