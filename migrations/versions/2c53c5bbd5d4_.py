"""empty message

Revision ID: 2c53c5bbd5d4
Revises: 
Create Date: 2023-06-07 16:09:20.113723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c53c5bbd5d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('compounds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('structure', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('global_statistics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('average_experiments', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('signup_date', sa.Date(), nullable=True),
    sa.Column('total_experiments', sa.Integer(), nullable=True),
    sa.Column('most_common_compounds_ids', sa.ARRAY(sa.Integer()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('global_statistics')
    op.drop_table('compounds')
    # ### end Alembic commands ###
