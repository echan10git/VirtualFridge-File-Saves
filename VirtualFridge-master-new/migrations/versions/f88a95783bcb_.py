"""empty message

Revision ID: f88a95783bcb
Revises: 30ba37867349
Create Date: 2020-05-17 13:36:03.639698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f88a95783bcb'
down_revision = '30ba37867349'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('knownIngredients', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fridges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ingredient', sa.String(length=140), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fridges_ingredient'), 'fridges', ['ingredient'], unique=False)
    op.create_index(op.f('ix_fridges_quantity'), 'fridges', ['quantity'], unique=False)
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipeingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Numeric(), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('link',
    sa.Column('recipeingredients_id', sa.Integer(), nullable=False),
    sa.Column('ingredients_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ingredients_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['recipeingredients_id'], ['recipeingredients.id'], ),
    sa.PrimaryKeyConstraint('recipeingredients_id', 'ingredients_id')
    )
    op.drop_index('ix_fridge_ingredient', table_name='fridge')
    op.drop_index('ix_fridge_quantity', table_name='fridge')
    op.drop_table('fridge')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fridge',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ingredient', sa.VARCHAR(length=140), nullable=True),
    sa.Column('quantity', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_fridge_quantity', 'fridge', ['quantity'], unique=False)
    op.create_index('ix_fridge_ingredient', 'fridge', ['ingredient'], unique=False)
    op.drop_table('link')
    op.drop_table('recipeingredients')
    op.drop_table('recipes')
    op.drop_index(op.f('ix_fridges_quantity'), table_name='fridges')
    op.drop_index(op.f('ix_fridges_ingredient'), table_name='fridges')
    op.drop_table('fridges')
    op.drop_table('ingredients')
    # ### end Alembic commands ###
