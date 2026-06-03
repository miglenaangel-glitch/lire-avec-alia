from flask import Flask, redirect, url_for, render_template
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# MySQL config mapping
app.config['MYSQL_HOST'] = Config.MYSQL_HOST
app.config['MYSQL_USER'] = Config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = Config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = Config.MYSQL_DB
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Make mysql available to blueprints
app.extensions['mysql'] = mysql

from routes.child import child_bp
from routes.parent import parent_bp
from routes.api import api_bp
from routes.admin import admin_bp

app.register_blueprint(child_bp, url_prefix='/child')
app.register_blueprint(parent_bp, url_prefix='/parent')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def index():
    from routes.child import LEVELS
    mysql = app.extensions['mysql']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM characters WHERE is_active = TRUE LIMIT 1")
    character = cur.fetchone()
    cur.execute("SELECT level_key, is_locked FROM level_locks")
    locks = {r['level_key']: r['is_locked'] for r in cur.fetchall()}
    cur.close()
    return render_template('child/home.html', character=character, levels=LEVELS, locks=locks)

if __name__ == '__main__':
    app.run(debug=True)
