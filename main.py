from fastapi import FastAPI, Request
from src.team import Team

app = FastAPI(
    title="VLR.gg Scraper",
    version="1",
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

