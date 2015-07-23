"""cache server-side sanitized markdown to HTML

Revision ID: 15a8d37b2d50
Revises: 27b093d6a9e8
Create Date: 2015-07-22 17:07:43.164404

"""

# revision identifiers, used by Alembic.
revision = '15a8d37b2d50'
down_revision = '27b093d6a9e8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###
