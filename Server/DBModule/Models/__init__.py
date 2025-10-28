import pgvector
from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .user_model import User
from .password_model import Password
from .upvotes_model import Upvotes
from .news_model import News
from .interest_model import Interest
from .category_model import Category
from .user_interest_model import User_Interest
from .user_category_model import User_Category