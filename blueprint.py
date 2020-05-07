from flask import Blueprint, render_template, request, redirect, url_for
from models import Recipe, Tag
from forms import RecipeForm
from app import db
import logging

recipes = Blueprint('recipes', __name__)


@recipes.route('/edit', methods=['POST', 'GET'])
def edit_recipe():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        try:
            recipe = Recipe(title=title, text=text)
            if recipe.title == '':
                return redirect(url_for('recipes.edit_recipe'))
            else:
                db.session.add(recipe)
                db.session.commit()
        except:
            logging.basicConfig(filename="Error.log", level=logging.INFO)

        return redirect(url_for('recipes.index'))
    form = RecipeForm()
    return render_template('recipes/edit_recipe.html', form=form)


@recipes.route('/')
def index():
    q = request.args.get('q', '')

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q != '':
        recipes_posts = Recipe.query.filter(Recipe.title.contains(q) | Recipe.text.contains(q))
    else:
        recipes_posts = Recipe.query.order_by(Recipe.published.desc())

    pages = recipes_posts.paginate(page=page, per_page=12)

    return render_template('recipes/index.html', recipes_posts=recipes_posts, pages=pages)


@recipes.route('/<slug>')
def recipe_detail(slug):
    recipe_post = Recipe.query.filter(Recipe.slug == slug).first()
    tags = recipe_post.tags
    return render_template('recipes/recipe_detail.html', recipe_post=recipe_post, tags=tags)


@recipes.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    recipe_items = tag.recipes.all()
    return render_template('recipes/tag_detail.html', tag=tag, recipes=recipe_items)
