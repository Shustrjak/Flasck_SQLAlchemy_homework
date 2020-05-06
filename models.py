from app import db
from datetime import datetime
import re


def slugify(title_item):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', title_item)


recipe_tags = db.Table('recipe_tags',
                       db.Column('recipe_id',
                                 db.Integer,
                                 db.ForeignKey('recipe.id')
                                 ),
                       db.Column('tag_id',
                                 db.Integer,
                                 db.ForeignKey('tag.id')
                                 ),
                       )


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(40), unique=True)
    text = db.Column(db.Text)
    published = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        super(Recipe, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=recipe_tags, backref=db.backref('recipes', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title).lower()

    def __repr__(self):
        return f'<Recipe id:{self.id}, ' \
               f'title: {self.title},' \
               f'slug: {self.slug}, ' \
               f'text:" {self.text}", ' \
               f'published: {self.published}.>'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return f'<Tag id:{self.id}, name:{self.name}>'
