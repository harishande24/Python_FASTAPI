"""add user table

Revision ID: 299a4df97a8b
Revises: a1c3f794a90d
Create Date: 2024-11-09 21:46:18.215548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '299a4df97a8b'
down_revision = 'a1c3f794a90d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass