"""add content column to posts table

Revision ID: a1c3f794a90d
Revises: 4be4688cde25
Create Date: 2024-11-09 12:04:34.113670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1c3f794a90d'
down_revision = '4be4688cde25'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass