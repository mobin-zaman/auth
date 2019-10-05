"""empty message

Revision ID: c8b34e27f33e
Revises: 
Create Date: 2019-10-04 19:59:34.458233

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c8b34e27f33e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business_model',
    sa.Column('id', mysql.BIGINT(unsigned=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('owner_name', sa.String(length=255), nullable=True),
    sa.Column('billing_address', sa.Text(), nullable=True),
    sa.Column('geo_lat', sa.Float(), nullable=True),
    sa.Column('geo_long', sa.Float(), nullable=True),
    sa.Column('billing_phone', sa.String(length=20), nullable=True),
    sa.Column('billing_email', sa.String(length=127), nullable=True),
    sa.Column('logo_id', mysql.BIGINT(unsigned=True), nullable=True),
    sa.Column('cover_id', mysql.BIGINT(unsigned=True), nullable=True),
    sa.Column('open_time', sa.Time(), nullable=True),
    sa.Column('close_time', sa.Time(), nullable=True),
    sa.Column('bot_app_id', mysql.BIGINT(unsigned=True), nullable=True),
    sa.Column('bot_url', sa.String(length=127), nullable=True),
    sa.Column('page_id', mysql.BIGINT(unsigned=True), nullable=True),
    sa.Column('page_url', sa.String(length=127), nullable=True),
    sa.Column('inserted_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('business_model')
    # ### end Alembic commands ###
