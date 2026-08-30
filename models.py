from sqlalchemy import Integer, Identity, String, Boolean, DateTime, func, Enum as SQLEnum
from enum import Enum, IntEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from typing import Optional, List
from sqlalchemy.dialects.postgresql import ARRAY

class Base(DeclarativeBase):
    pass

class ActionStatus(Enum):
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

class Action(Base):
    __tablename__ = "actions"

    # should read about what columns to choose be indexed
    id: Mapped[int] = mapped_column(Integer, Identity(start=1), primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(750), nullable=True)
    xp: Mapped[int] = mapped_column(Integer, nullable=False)
    is_boxy: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    minutes_per_unit: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=False, server_default="{}", default_factory=list)
    status: Mapped[ActionStatus] = mapped_column(SQLEnum(ActionStatus), nullable=False, default=ActionStatus.TO_DO, server_default=ActionStatus.TO_DO.value)
    due_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True, default=None)
    priority: Mapped[ActionPriority] = mapped_column(Integer, nullable=False, default=ActionPriority.MEDIUM, server_default="3")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class Reward(Base):
    __tablename__ = "rewards"
    # columns
        """
        id
        title
        how much xp does it cost?
        status -> unlock or not?
        status -> consumed or not?
        created_at
        updated_at
        """

# I should apply the same syntax of my notebook for the app
# search what other things you should apply

class UserProfile(Base):
    __tablename__ = "user_profile"

    #columns
    """
    probably:
    id
    total_xp_eanred from the start
    current xp which means the xp that actually has left for user to use
    current level - not sure still about it, if applied, should consider how exactly should calculate it
    created_at
    I don't know if I should consider the case of all the users or stay on local use
    """

# also I think I need another table for gathering logs, history of all the actions of the user, not sure
