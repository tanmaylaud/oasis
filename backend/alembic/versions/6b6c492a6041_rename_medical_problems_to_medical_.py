"""rename medical_problems to medical_conditions

Revision ID: 6b6c492a6041
Revises: 7d4ae3aca2ec
Create Date: 2020-06-01 21:24:46.700382

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "6b6c492a6041"
down_revision = "7d4ae3aca2ec"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "stories", sa.Column("_medical_conditions", sa.JSON(), nullable=True)
    )
    op.drop_column("stories", "_medical_problems")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "stories", sa.Column("_medical_problems", mysql.JSON(), nullable=True)
    )
    op.drop_column("stories", "_medical_conditions")
    # ### end Alembic commands ###
