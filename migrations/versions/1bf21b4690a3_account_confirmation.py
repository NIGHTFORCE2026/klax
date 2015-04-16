"""account confirmation

Revision ID: 1bf21b4690a3
Revises: 3b9f565eaaef
Create Date: 2015-04-15 19:49:26.880487

"""

# revision identifiers, used by Alembic.
revision = '1bf21b4690a3'
down_revision = '3b9f565eaaef'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
