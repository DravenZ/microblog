"""empty message

Revision ID: 94202c26a7e8
Revises: 8cea59372d7c
Create Date: 2018-12-10 14:21:59.056716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94202c26a7e8'
down_revision = '8cea59372d7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###