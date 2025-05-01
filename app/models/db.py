from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    """Initializes the database connection using Flask-MySQLdb."""
    # Configuration for MySQL should be in config.py
    # Required keys: MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
    mysql.init_app(app)

