"""empty message

Revision ID: 9081a5e32706
Revises: 4757ef31c613
Create Date: 2019-07-08 18:39:51.893170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9081a5e32706'
down_revision = '4757ef31c613'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('posts_user_id_fkey', 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('posts_user_id_fkey', 'posts', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
