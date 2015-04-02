"""removed test model

Revision ID: 3fd742efb314
Revises: 39c574fb2952
Create Date: 2015-04-02 13:30:18.691586

"""

# revision identifiers, used by Alembic.
revision = '3fd742efb314'
down_revision = '39c574fb2952'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testmodel')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testmodel',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('testval', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###
