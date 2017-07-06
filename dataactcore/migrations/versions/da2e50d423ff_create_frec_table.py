"""create FREC table

Revision ID: da2e50d423ff
Revises: aa10ae595d3e
Create Date: 2017-07-06 10:27:04.738865

"""

# revision identifiers, used by Alembic.
revision = 'da2e50d423ff'
down_revision = 'aa10ae595d3e'
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
    op.create_table('frec',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('frec_id', sa.Integer(), nullable=False),
    sa.Column('frec_code', sa.Text(), nullable=True),
    sa.Column('agency_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('frec_id')
    )
    op.create_index(op.f('ix_frec_frec_code'), 'frec', ['frec_code'], unique=True)
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_frec_frec_code'), table_name='frec')
    op.drop_table('frec')
    ### end Alembic commands ###

