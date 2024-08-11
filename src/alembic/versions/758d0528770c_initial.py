"""initial

Revision ID: 758d0528770c
Revises: 961d2c7b1b78
Create Date: 2024-08-04 19:40:00.028292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '758d0528770c'
down_revision: Union[str, None] = '961d2c7b1b78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('closed_tasks', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('closed_tasks', 'description')
    # ### end Alembic commands ###
