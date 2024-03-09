# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна
# (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'title': 'Интернет Магазин "Стильный стиль :)',
        'content_main': 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты. Он что большой рукопись cвоего семь парадигматическая пояс коварных себя, обеспечивает назад вскоре имеет злых заманивший путь? Первую задал рыбными то, запятых lorem журчит решила осталось пунктуация, на берегу что ipsum жаренные гор рукопись',
    }
    return render_template('index.html', **context)



@app.route('/Catalog')
def catalog():
    context = {
        'title': 'Каталог',
        'data': {'Одежда':['Куртка', 'Брюки'], "Обувь":['Ботинки']},
    }
    return render_template('catalog.html', **context)


@app.route('/Catalog/<category>')
def category(category):
    context = {
        'data': {'Одежда': ['Куртка', 'Брюки'], "Обувь": ['Ботинки']},
    }
    if category in context['data'].keys():
        context['title'] = category
        return render_template('category.html', **context)
    else:
        context['title'] = 'Ошибка'
        return render_template('error.html', **context)




@app.route('/Contact')
def contact():
    context = {
        'title': 'Контакты',
        'data': {'email':'gegegg@fdfd.ru', 'tel':'+1023444234'},
    }
    return render_template('contact.html', **context)

if __name__ == '__main__':
    app.run(debug=True)