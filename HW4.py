from flask import Flask, render_template, request, make_response
from flask import session, redirect, url_for
import datetime
import sqlite3

# ДЗ 4. Создание блога.
"""
Создать базу данных blog.sqlite в которой создать таблицу posts.
Таблица должна содержать такие поля: id, title, description, date

Создать блог используя 4 страницы:
1. Страница для отображения всех записей в блоге,
   обычная выборка и отображение в темплейте
2. Страница для добавления новой записи в блог,
   страница должна принимать два параметра title и description
3. Страница для редактирования записи в блоге,
   страница должна принимать один главный параметр это id
   и title\description для обновления информации по посту
4. Страница для удаления поста, страница должна принимать id
   поста которого хотим удалить

- После успешного выполнения 2, 3, 4 страницы редиректим
  (перенаправляем) на страницу со всеми постами
- Обязательно писать doc-string в каждой функции
- Добавить .gitignore в проект
- Добавить базу данных в проект
- В начале файла программы вставить комментарий\doc-string
  с командой которой вы создали таблицу
- Стилизация темплейта приветствуется, но не обязательно

"""

app = Flask(__name__)

# Создаем базу данных "blog.sqlite".
conn = sqlite3.connect('blog.sqlite')

# Инициализируем курсор.
init_cursor = conn.cursor()

# # Создаём таблицу в базе данных "blog.sqlite".
# init_cursor.execute("""CREATE TABLE blog
# (id integer PRIMARY KEY, title text, description text, date text)""")

# Сохраняем все изменения.
conn.commit()

# Закрываем соединение.
conn.close()


# Создаём страницу для отображения всех записей в блоге.
# Обычная выборка и отображение в темплейте.
@app.route('/show')
def show_all_entries():
    # Подключаемся к базе необходимой данных.
    show_connection = sqlite3.connect('blog.sqlite')

    # Инициализируем курсор для выполнения операций.
    show_cursor = show_connection.cursor()

    # Выбираем всю информацию из необходимой таблицы.
    show_cursor.execute("""SELECT * FROM blog""")

    # Забираем результат команды "SELECT"
    # и сохраняем в переменной "show_data".
    show_data = show_cursor.fetchall()

    # Закрываем соединение.
    show_connection.close()

    # Передаем данные переменной в темплейт.
    return render_template('show_all_entries.html', show_data=show_data)


# Создаём страницу для добавления новой записи в блог.
# Страница должна принимает два параметра title и description
@app.route('/show/add')
def add_new_entry():
    # Получаем из аргументов информацию.
    add_title = request.args.get('title')
    add_description = request.args.get('description')

    # Подключаемся к базе необходимой данных.
    add_connection = sqlite3.connect('blog.sqlite')

    # Инициализируем курсор для выполнения операций.
    add_cursor = add_connection.cursor()

    # Инициализируем переменную текущего времени и даты.
    current_datetime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    # Располагаем данные в том порядке,
    # в котором хотим записать в базу данных.
    values = (add_title, add_description, current_datetime)

    # Выбираем необходимую информацию.
    add_cursor.execute("""INSERT INTO blog (id, title, description, date)
    VALUES (last_insert_rowid(), ?, ?, ?)""", values)

    # Отправляем добавления в базу данных на исполнение.
    add_connection.commit()

    # Закрываем соединение.
    add_connection.close()

    # Передаем данные в темплейт.
    return redirect('/show')


# Создаём страницу для редактирования записи в блоге.
# Страница принимает один главный параметр это id и
# title\description для обновления информации по посту
@app.route('/show/update')
def update_table():
    # Подключаемся к базе необходимой данных.
    update_connection = sqlite3.connect('blog.sqlite')

    # Инициализируем курсор для выполнения операций.
    update_cursor = update_connection.cursor()

    # Выбираем данные, которые хотим изменить
    # и сохраняем в переменную.
    values = """UPDATE blog SET title = 'Title8', 
    description = 'description8' WHERE id = '0'"""

    # Выполняем изменения.
    update_cursor.execute(values)

    # Отправляем добавления в базу данных на исполнение.
    update_connection.commit()

    # Закрываем соединение.
    update_connection.close()

    # Передаем данные в темплейт.
    return redirect('/show')


# Создаём страницу для удаления поста.
# Принимает id поста, который мы хотим удалить.
@app.route('/show/delete')
def delete_table():
    # Подключаемся к базе необходимой данных.
    delete_connection = sqlite3.connect('blog.sqlite')

    # Инициализируем курсор для выполнения операций.
    delete_cursor = delete_connection.cursor()

    # Выбираем данные, которые хотим удалить
    # и сохраняем в переменную.
    values = """DELETE FROM blog WHERE id = '0'"""

    # Выполняем изменения.
    delete_cursor.execute(values)

    # Отправляем добавления в базу данных на исполнение.
    delete_connection.commit()

    # Закрываем соединение.
    delete_connection.close()

    # Передаем данные в темплейт.
    return redirect('/show')


if __name__ == '__main__':
    app.run(debug=True)
