"""addErrorsPresent

Revision ID: a17156edb8a0
Revises: cdcaa9c693e3
Create Date: 2016-04-08 11:40:49.599000

"""

# revision identifiers, used by Alembic.
revision = 'a17156edb8a0'
down_revision = 'cdcaa9c693e3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file_status', sa.Column('errors_present', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file_status', 'errors_present')
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###

