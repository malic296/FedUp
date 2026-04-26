"""initial_schema

Revision ID: 3062b4f44e34
Revises: 
Create Date: 2026-04-19 11:02:47.207288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3062b4f44e34'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
       CREATE TABLE channel ( id SERIAL PRIMARY KEY, uuid TEXT UNIQUE NOT NULL, title TEXT, link TEXT UNIQUE);
    """)
    op.execute("""
       CREATE TABLE article ( id SERIAL PRIMARY KEY, uuid TEXT UNIQUE NOT NULL, title TEXT, link TEXT UNIQUE, description TEXT, pub_date TIMESTAMPTZ, channel_id INTEGER REFERENCES channel(id) );
    """)
    op.execute("""
       CREATE TABLE logging ( id SERIAL PRIMARY KEY, timestamp TIMESTAMPTZ, status TEXT, module TEXT, method TEXT, message TEXT );
    """)
    op.execute("""
      CREATE TABLE password (id SERIAL PRIMARY KEY, hash TEXT NOT NULL);
    """)
    op.execute("""
       CREATE TABLE consumer (id SERIAL PRIMARY KEY, uuid TEXT UNIQUE NOT NULL, username TEXT NOT NULL, email TEXT NOT NULL, password_id integer REFERENCES password(id) ON DELETE CASCADE);
    """)
    op.execute("""
       CREATE TABLE likes (id SERIAL PRIMARY KEY, consumer_id integer REFERENCES consumer(id) ON DELETE CASCADE, article_id integer REFERENCES article(id) ON DELETE CASCADE, UNIQUE (consumer_id, article_id));
    """)
    op.execute("""
       CREATE TABLE disabled (id SERIAL PRIMARY KEY, consumer_id integer REFERENCES consumer(id), channel_id integer REFERENCES channel(id) ON DELETE CASCADE);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE disabled;")
    op.execute("DROP TABLE likes;")
    op.execute("DROP TABLE consumer;")
    op.execute("DROP TABLE password;")
    op.execute("DROP TABLE logging;")
    op.execute("DROP TABLE article;")
    op.execute("DROP TABLE channel;")
