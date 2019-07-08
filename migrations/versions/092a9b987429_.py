"""empty message

Revision ID: 092a9b987429
Revises: 9081a5e32706
Create Date: 2019-07-08 18:43:23.655118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '092a9b987429'
down_revision = '9081a5e32706'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###
