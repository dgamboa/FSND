"""empty message

Revision ID: 523596f67c2a
Revises: b63873e032db
Create Date: 2020-09-11 11:49:25.900867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '523596f67c2a'
down_revision = 'b63873e032db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_venue_id', 'Show', type_='foreignkey')
    op.drop_constraint('fk_artist_id', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('fk_artist_id', 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key('fk_venue_id', 'Show', 'Venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###
