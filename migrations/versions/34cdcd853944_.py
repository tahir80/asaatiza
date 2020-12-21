"""empty message

Revision ID: 34cdcd853944
Revises: 
Create Date: 2020-12-16 12:50:08.919021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34cdcd853944'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('TASK', sa.Column('URL_completion_code', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('TASK', 'URL_completion_code')
    # ### end Alembic commands ###
