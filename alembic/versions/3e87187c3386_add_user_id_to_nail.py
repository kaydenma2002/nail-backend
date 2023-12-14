"""add_user_id_to_nail

Revision ID: 3e87187c3386
Revises: 
Create Date: 2023-12-14 18:46:08.362887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e87187c3386'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    print("Starting upgrade...")
    op.add_column('nails', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_nails_user_id', 'nails', 'users', ['user_id'], ['id'])
    print("Upgrade completed.")


def downgrade() -> None:
    pass
