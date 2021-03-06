"""empty message

Revision ID: 6b1274f61edd
Revises: 6b335fbd58ab
Create Date: 2019-07-10 22:56:20.082864

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6b1274f61edd'
down_revision = '6b335fbd58ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kvm', sa.Column('timestamp_build_finished', sa.DateTime(), nullable=True))
    op.add_column('kvm', sa.Column('timestamp_prep_finished', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kvm', 'timestamp_prep_finished')
    op.drop_column('kvm', 'timestamp_build_finished')
    # ### end Alembic commands ###
