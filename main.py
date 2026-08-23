"""main file"""

from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()

@app.get("/")
def home(db: Annotated[Session, Depends(get_db)]):
    return {"message": "Welcome to Lily."}

@app.get("/actions")
def actions_page(db: Annotated[Session, Depends(get_db)]):
    pass

@app.post("/actions")
def action_create(db: Annotated[Session, Depends(get_db)]):
    pass

@app.get("/actions/{action_id}")
def action_details(action_id: int, db: Annotated[Session, Depends(get_db)]):
    pass

@app.patch("/actions/{action_id}")
def action_modify(action_id: int, db: Annotated[Session, Depends(get_db)]):
    pass

@app.delete("/actions/{action_id}")
def action_delete(action_id: int, db: Annotated[Session, Depends(get_db)]):
    pass

@app.get("/rewards")
def rewards_page(db: Annotated[Session, Depends(get_db)]):
    pass

@app.post("/rewards")
def reward_create(db: Annotated[Session, Depends(get_db)]):
    pass

@app.get("/rewards/{reward_id}")
def reward_details(db: Annotated[Session, Depends(get_db)]):
    pass

@app.patch("/rewards/{reward_id}")
def reward_modify(reward_id: int, db: Annotated[Session, Depends(get_db)]):
    pass

@app.delete("/rewards/{reward_id}")
def reward_delete(reward_id: int, db: Annotated[Session, Depends(get_db)]):
    pass

@app.post("/rewards/{reward_id}/consume")
def reward_consume(reward_id: int, db: Annotated[Session, Depends(get_db)]):
    pass

@app.post("/rewards/{reward_id}/purchase")
def reward_purchase(reward_id: int, db: Annotated[Session, Depends(get_db)]):
    pass

# tasks:
# define models
# define schemas
# configure DB settings
# search about what other advanced features you can learn to add

# moment:
# need food but don't feel like eating
# listening: porcupine tree, some famous classical violin pieces
# read today: ---
# a good thing to remember: the kindness of upper-level guys when they give you advice