"""empty message

Revision ID: 81eac70c57f9
Revises: d3fa6be53b72
Create Date: 2023-02-28 01:24:15.822583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81eac70c57f9'
down_revision = 'd3fa6be53b72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=128), nullable=False))
        batch_op.drop_column('nickname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nickname', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
        batch_op.drop_column('username')

    # ### end Alembic commands ###
