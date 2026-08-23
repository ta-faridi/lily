from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime, time, date

Base = declarative_base()

class Action(Base):
    __tablename__ = "actions"

    # columns
    """
    id
    title
    positive or negetive kind
    xp
    is it a boxy action?
        if yes:
            minutes per each unit
    tags
    created_at
    updated_at
    """

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
