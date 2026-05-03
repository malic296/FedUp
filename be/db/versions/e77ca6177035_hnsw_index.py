"""hnsw index

Revision ID: e77ca6177035
Revises: 429f7dd2b158
Create Date: 2026-05-03 13:11:24.491690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e77ca6177035'
down_revision: Union[str, Sequence[str], None] = '429f7dd2b158'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE INDEX IF NOT EXISTS idx_article_embedding_hnsw ON article USING hnsw (embedding vector_cosine_ops)")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP INDEX IF EXISTS idx_article_embedding_hnsw")
