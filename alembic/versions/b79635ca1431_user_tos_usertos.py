"""User TOS UserTOS

Revision ID: b79635ca1431
Revises: 
Create Date: 2021-07-26 03:09:54.490960

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b79635ca1431'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('privacy_terms_of_service',
    sa.Column('version', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('version'),
    sa.UniqueConstraint('version')
    )
    op.create_table('user',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('discord_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('discord_id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user_privacy_tos',
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('tos_version', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['tos_version'], ['privacy_terms_of_service.version'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'tos_version')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_privacy_tos')
    op.drop_table('user')
    op.drop_table('privacy_terms_of_service')
    # ### end Alembic commands ###