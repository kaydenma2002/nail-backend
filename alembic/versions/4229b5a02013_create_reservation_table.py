"""Create reservation table

Revision ID: 4229b5a02013
Revises: d47b5421fa74
Create Date: 2023-12-15 14:36:53.365580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4229b5a02013'
down_revision: Union[str, None] = 'd47b5421fa74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'reservations',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('customer_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('worker_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('date', sa.DateTime(), nullable=False),
        sa.Column('status', sa.Integer(), nullable=False, default=0)
    )

def downgrade():
    op.drop_table('reservation')
