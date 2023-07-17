from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fadzlinaim21'
app.config['MYSQL_DB'] = 'pallyspa'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-treatment', methods=['POST'])
def add_treatment():
    # Get form data
    name = request.form['treatment-name']
    category = request.form['treatment-category']
    description = request.form['treatment-description']
    price = request.form['treatment-price']

    # Insert treatment details into database
    cursor = mysql.connection.cursor()
    cursor.execute(
        'INSERT INTO treatments (name, category, description, price) VALUES (%s, %s, %s, %s)',
        (name, category, description, price)
    )
    mysql.connection.commit()
    cursor.close()

    # Redirect to success page
    return redirect(url_for('index', _anchor='successMessage'))

if __name__ == '__main__':
    app.run()
