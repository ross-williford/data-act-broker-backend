"""add is submitted to d file table

Revision ID: 889892137919
Revises: 1f43c2880644
Create Date: 2016-08-03 13:02:05.463607

"""

# revision identifiers, used by Alembic.
revision = '889892137919'
down_revision = '1f43c2880644'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('d_file_metadata', sa.Column('is_submitted', sa.Boolean(), server_default='False', nullable=True))
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('d_file_metadata', 'is_submitted')
    ### end Alembic commands ###

