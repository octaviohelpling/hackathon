from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'contraword'
app.config['MYSQL_DATABASE_DB'] = 'hackathon'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

app.debug = True

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/matching')
def matching():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events')
    data = cursor.fetchall()

    return str(data)


if __name__ == "__main__":
    app.run()
