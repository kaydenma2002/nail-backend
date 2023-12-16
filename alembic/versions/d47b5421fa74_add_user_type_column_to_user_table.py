"""Add user_type column to user table

Revision ID: d47b5421fa74
Revises: 3e87187c3386
Create Date: 2023-12-15 14:30:33.909527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd47b5421fa74'
down_revision: Union[str, None] = '3e87187c3386'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('user_type', sa.Integer(), nullable=False, default=1))

def downgrade():
    op.drop_column('users', 'user_type')
