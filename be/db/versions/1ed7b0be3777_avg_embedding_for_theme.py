"""avg embedding for theme

Revision ID: 1ed7b0be3777
Revises: e77ca6177035
Create Date: 2026-05-09 09:42:52.437297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ed7b0be3777'
down_revision: Union[str, Sequence[str], None] = 'e77ca6177035'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        ALTER TABLE theme ADD COLUMN centroid_embedding vector(384);
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE theme DROP COLUMN centroid_embedding;
    """)
