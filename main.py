from app import app, db
from blueprint import recipes

app.register_blueprint(recipes, url_prefix='/recipes')

if __name__ == '__main__':
    db.create_all()
    app.run()
