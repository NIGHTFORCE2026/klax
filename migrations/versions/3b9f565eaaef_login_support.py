"""login support

Revision ID: 3b9f565eaaef
Revises: 3fd742efb314
Create Date: 2015-04-14 11:23:02.587054

"""

# revision identifiers, used by Alembic.
revision = '3b9f565eaaef'
down_revision = '3fd742efb314'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    ### end Alembic commands ###