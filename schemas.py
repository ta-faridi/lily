from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from pydantic.types import Partial
from datetime import datetime
from enum import Enum, IntEnum

class ActionStatus(Enum): # repeated piece of code, need to put it somewhere
    TO_DO = "to do"
    IN_PROGRESS = "in progress"
    ON_HOLD = "on hold"
    DONE = "done"
    IN_REVIEW = "in review"
    CANCELED = "canceled"

class ActionPriority(IntEnum):
    TRIVIAL = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    CRITICAL = 5

class ActionBase(BaseModel):
    title: str = Field(..., min_length=1, max_length= 100, description="Title of the action", examples=["Read book X, chapters 6 & 7", "45 minutes exercise session", "Study Math 40 minutes session", "Memorizing Algorithms flashcards"])
    description: Optional[str] = Field(None, max_length=750)
    xp: int = Field(..., description="xp value")
    ix_boxy: bool = Field(default=False, description="") 
    minutes_per_unit: int = Field(ge=0, default=0, description="Allocated minutes per time box") # I don't know about this one. This behaviour only will be applied if the action is a boxy one.
    tags: List[str] = Field(default_factory=list, max_length=10, description="Tags for categorization")
    status: ActionStatus = Field(default=ActionStatus.TO_DO, description="Current status of the action")
    due_date: Optional[datetime] = Field(None, description="Due date for action")
    priority: ActionPriority = Field(default=ActionPriority.MEDIUM, description="Action's priority")

class ActionResponse(ActionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class ActionCreate(ActionBase):
    pass

class ActionUpdate(ActionBase):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=750)
    xp: Optional[int] = Field(None)
    ix_boxy: Optional[bool] = Field(None)
    minutes_per_unit: Optional[int] = Field(None, ge=0)
    tags: Optional[List[str]] = Field(None, max_length=10)
    status: Optional[ActionStatus] = Field(None)
    due_date: Optional[datetime] = Field(None)
    priority: Optional[ActionPriority] = Field(None)
    
    model_config = ConfigDict(from_attributes=True)