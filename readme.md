Данный проект - это небольшой сайт с минимальными возможностями.
В котором есть возможность:
####Создавать посты





## Как работает:

В проекте надо запустить app: 

### `python main.py run`

При запуске сформируется локальный сервер:<br />
Откройте: [http://localhost:5000](http://localhost:5000) в вашем браузере.

Из консоли можно добавлять теги в уже имеющуюся базу:
В консоли зайдите в папку проекта
запустите python
Ввеедите данные для создаия скрипта:
### `from app import db`
### `from models import Tag`
У Тега есть переменная 'name', с помощью которого позже тег записывается в созданную базу данных.
Создадим переменную "t"
### `name_tag = Tag(name='other tag')`
Запишем тег в базу
### `db.session.add(name_tag)`
### `db.session.commit()`
Для того, чтоб убедиться, что тег записан, просто введите его переменную и у него появится свой id.<br />
Для подключения тега к посту делаем следующее(если ранее скрипт завершили):
### `from app import db`
### `from models import Recipe, Tag`
Или добавьте:
### `from models import Recipe`
Найдем пост, к которому хотим привязать тег:

### `name_tag = Tag(name='other tag')`
запрос пометим в переменную:
q='ваш_запрос')
Ищем по заголовку:
### `name_recipe = Recipe.query.filter(Recipe.title.contains(q))`
Или по тексту:
### `text_recipe = Recipe.query.filter(Recipe.text.contains(q))`
Проверяем, сколько постов есть с искомым значениемЖ
### `name_recipe.count()` или `text_recipe.count()`
Увидим кол-во постов.
Чтобы добавить тег, нужно будет создать более точный запрос. Тег привязывается отдельно к каждому посту.
или выберем первыый постЖ
### `name_recipe.first()` или `text_recipe.first()`
Привяжем тег к посту:
### `name_recipe = name_recipe.first()` или `text_recipe = text_recipe.first()`
### `name_recipe.tags.append(name_tag)` или `text_recipe.tags.append(name_tag)`

### `db.session.add(name_recipe)` или `db.session.add(text_recipe)`
### `db.session.commit()`

На странице рецепта появяется дополнительная кнопка для создания поста.
В представленной конфигурации есть посты, теги.
даже рабочий поиск.