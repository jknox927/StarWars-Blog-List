"""empty message

Revision ID: d3fa6be53b72
Revises: d445fe04309c
Create Date: 2023-02-28 00:24:08.698757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3fa6be53b72'
down_revision = 'd445fe04309c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('birth_year', sa.String(length=256), nullable=True))
    op.add_column('people', sa.Column('eye_color', sa.String(length=256), nullable=True))
    op.add_column('people', sa.Column('gender', sa.String(length=256), nullable=True))
    op.add_column('people', sa.Column('hair_color', sa.String(length=256), nullable=True))
    op.add_column('people', sa.Column('height', sa.Integer(), nullable=True))
    op.add_column('people', sa.Column('mass', sa.Integer(), nullable=True))
    op.add_column('people', sa.Column('skin_color', sa.String(length=256), nullable=True))
    op.add_column('people', sa.Column('homeworld', sa.String(length=256), nullable=True))
    op.add_column('people', sa.Column('url', sa.String(length=256), nullable=True))
    op.add_column('people', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.add_column('people', sa.Column('date_edited', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('people', 'date_edited')
    op.drop_column('people', 'date_created')
    op.drop_column('people', 'url')
    op.drop_column('people', 'homeworld')
    op.drop_column('people', 'skin_color')
    op.drop_column('people', 'mass')
    op.drop_column('people', 'height')
    op.drop_column('people', 'hair_color')
    op.drop_column('people', 'gender')
    op.drop_column('people', 'eye_color')
    op.drop_column('people', 'birth_year')
    # ### end Alembic commands ###
