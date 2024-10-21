"""add actions.confidence_float

Revision ID: 2873c5c8c41e
Revises: 137eee1d3b3e
Create Date: 2024-10-18 20:03:10.612242+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2873c5c8c41e"
down_revision: Union[str, None] = "137eee1d3b3e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("actions", sa.Column("confidence_float", sa.Numeric(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("actions", "confidence_float")
    # ### end Alembic commands ###