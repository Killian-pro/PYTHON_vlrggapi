from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.team import Team


app = FastAPI(
    title="VLR.gg Scraper",
    version="1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["health"])
async def health_check():
    """
    Checks site health
    """
    return 'OK'

@app.get("/team/{id}", tags=["teams"])
async def team(id):
    """
    Gets team details of the team with the given ID
    """
    return Team.team(id)

