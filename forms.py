from wtforms import Form, StringField, TextAreaField

class RecipeForm(Form):
    title = StringField('title')
    text = TextAreaField('text')
