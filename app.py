]from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Создаем базу данных SQLite и таблицу для хранения данных о семье
def create_table():
    conn = sqlite3.connect('family.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS family
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, relation TEXT)''')
    conn.commit()
    conn.close()

# Добавляем данные о члене семьи в базу данных
def add_member(name, age, relation):
    conn = sqlite3.connect('family.db')
    c = conn.cursor()
    c.execute("INSERT INTO family (name, age, relation) VALUES (?, ?, ?)", (name, age, relation))
    conn.commit()
    conn.close()

# Получаем всех членов семьи из базы данных
def get_family_members():
    conn = sqlite3.connect('family.db')
    c = conn.cursor()
    c.execute("SELECT * FROM family")
    members = c.fetchall()
    conn.close()
    return members

# Отображаем главную страницу с формой для добавления члена семьи
@app.route('/')
def index():
    return render_template('index.html')

# Обрабатываем данные из формы и добавляем члена семьи в базу данных
@app.route('/add_member', methods=['POST'])
def add_member_route():
    name = request.form['name']
    age = request.form['age']
    relation = request.form['relation']
    add_member(name, age, relation)
    return redirect(url_for('family_list'))

# Отображаем список всех членов семьи
@app.route('/family')
def family_list():
    members = get_family_members()
    return render_template('family.html', members=members)

if __name__ == '__main__':
    create_table() # Создаем таблицу при запуске сервера
    app.run(debug=True)
# Импортируем функцию render_template
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Отображаем главную страницу с формой для добавления члена семьи
@app.route('/')
def index():
    return render_template('index.html')

# Остальные функции остаются без изменений
# ...

if __name__ == '__main__':
    create_table() # Создаем таблицу при запуске сервера
    app.run(debug=True)
render_template('templates/index.html')
