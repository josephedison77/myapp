"""remove cleaning_logs from Staff

Revision ID: 6b83f4607f67
Revises: 56b815515e9a
Create Date: 2025-06-01 10:53:49.876704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b83f4607f67'
down_revision = '56b815515e9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cleaning_log', schema=None) as batch_op:
            
        batch_op.add_column(sa.Column('staff_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_cleaning_log_staff_id', 'staff', ['staff_id'], ['id'])

        # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cleaning_log', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('staff_id')

    # ### end Alembic commands ###
