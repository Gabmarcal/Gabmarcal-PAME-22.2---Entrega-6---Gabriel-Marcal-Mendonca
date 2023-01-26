"""empty message

Revision ID: 237e59b7d73c
Revises: f95406099240
Create Date: 2023-01-24 21:01:59.498099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '237e59b7d73c'
down_revision = 'f95406099240'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medicine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=True),
    sa.Column('prescricao', sa.String(length=30), nullable=True),
    sa.Column('fabricante', sa.String(length=30), nullable=True),
    sa.Column('validade', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medicine')
    # ### end Alembic commands ###
