"""empty message

Revision ID: 471c509d08dd
Revises: f7b5f17499a5
Create Date: 2019-10-07 13:49:49.925777

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '471c509d08dd'
down_revision = 'f7b5f17499a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('business_merchant', sa.Column('user_id', mysql.BIGINT(unsigned=True), nullable=False))
    op.create_foreign_key(None, 'business_merchant', 'business', ['business_id'], ['id'])
    op.create_foreign_key(None, 'business_merchant', 'merchant', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'business_merchant', type_='foreignkey')
    op.drop_constraint(None, 'business_merchant', type_='foreignkey')
    op.drop_column('business_merchant', 'user_id')
    # ### end Alembic commands ###
