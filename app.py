import sqlite3

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


# Create a page to display all posts.
# Regular sampling and display in the template.
@app.route('/')
def display_posts():
    # Connect to the database of the required database.
    connection = sqlite3.connect('database.sqlite')

    # Initialize the cursor to perform operations.
    cursor = connection.cursor()

    # Select all the information from the required table.
    cursor.execute("""SELECT * FROM NAMES""")

    # Take the result of the "SELECT" command
    # and save it in the "show_data" variable.
    names = cursor.fetchall()

    # Close the connection.
    cursor.close()

    # Transfer the data to the variable to the template.
    return render_template('index.html', names=names)


# Create a page for adding a new post. The page should
# take two parameters title and description.
@app.route('/add')
def add_new_entry():
    # Get information from the arguments.
    add_name = request.args.get('name')
    add_description = request.args.get('description')

    # If a name has not been entered, we throw an error.
    if not add_name:
        return 'Sorry, you should insert name'

    # Connect to the required database.
    connection = sqlite3.connect('database.sqlite')

    # Initialize the cursor to perform operations.
    cursor = connection.cursor()

    # Arrange the data in the order,
    # in which we want to write to the database.
    values = (add_name, add_description)

    # Select the necessary information.
    cursor.execute("""INSERT INTO NAMES (id, name, description)
    VALUES (last_insert_rowid(), ?, ?)""", values)

    # Send additions to the database for execution.
    connection.commit()

    # Close the connection.
    cursor.close()

    # Transfer data to the template.
    return redirect('/')


# Create a page for editing a post.
# The page takes one main parameter this is id and
# title \ description to update post information
@app.route('/update')
def update_table():
    # Get information from the arguments.
    update_id = request.args.get('id')
    update_name = request.args.get('name')
    update_description = request.args.get('description')

    # If a name has not been entered, we throw an error.
    if not update_name:
        return 'Sorry, you should insert update name'

    # Connect to the required database.
    connection = sqlite3.connect('database.sqlite')

    # Initialize the cursor to perform operations.
    cursor = connection.cursor()

    # Arrange the data in the order,
    # in which we want to write to the database.
    values = (update_name, update_description, update_id)

    # Making changes.
    cursor.execute("""UPDATE NAMES SET name = ?,
    description = ? WHERE Id = ?""", values)

    # Send additions to the database for execution.
    connection.commit()

    # Close the connection.
    cursor.close()

    # Transfer data to the template.
    return redirect('/')


# Create a page to delete a post.
# Accepts the id of the post we want to delete.
@app.route('/delete')
def delete_table():
    # Get information from the arguments.
    delete_id = request.args.get('id')

    # Connect to the required database.
    connection = sqlite3.connect('database.sqlite')

    # Initialize the cursor to perform operations.
    cursor = connection.cursor()

    # Making changes.
    cursor.execute("""DELETE FROM NAMES WHERE Id = ?""", delete_id)

    # Send additions to the database for execution.
    connection.commit()

    # Close the connection.
    cursor.close()

    # Transfer data to the template.
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
