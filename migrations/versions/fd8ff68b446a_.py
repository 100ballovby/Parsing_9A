"""empty message

Revision ID: fd8ff68b446a
Revises: 
Create Date: 2021-05-19 09:23:50.807069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd8ff68b446a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_link', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('ingredient', sa.String(length=255), nullable=True),
    sa.Column('price', sa.String(length=50), nullable=True),
    sa.Column('img_link', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pizzas_name'), 'pizzas', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pizzas_name'), table_name='pizzas')
    op.drop_table('pizzas')
    # ### end Alembic commands ###