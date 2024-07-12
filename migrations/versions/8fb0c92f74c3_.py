"""empty message

Revision ID: 8fb0c92f74c3
Revises: 24166d2b31f0
Create Date: 2024-07-12 00:39:11.313681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fb0c92f74c3'
down_revision = '24166d2b31f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dog_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('birth', sa.Date(), nullable=True))
        batch_op.alter_column('gender',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('breed',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('spayed_neutered',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('weight',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.drop_column('age')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dog_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.alter_column('weight',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('spayed_neutered',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('breed',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('gender',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.drop_column('birth')

    # ### end Alembic commands ###
