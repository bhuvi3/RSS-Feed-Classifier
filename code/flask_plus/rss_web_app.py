from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)

DATABASE = "../rss_feed_classification.sqlite"

@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def index():
	categories = g.db.execute("SELECT distinct category FROM RSSEntries").fetchall()
	return render_template('index.html', categories = categories)

@app.route('/', methods=['POST'])
def show():
	category = request.form["category"]
	rows = g.db.execute("SELECT entry_id, feed_url, title, description, date FROM RSSEntries WHERE category = (?) ",(category, ))
	return render_template('result_table.html', rows = rows, category = category)

if __name__ == '__main__':
    app.run()