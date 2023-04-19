import sys
print(sys.executable)

from flask import Flask, render_template
from flask_couchdb import CouchDBManager

app = Flask(__name__)
app.config.update(
    COUCHDB_SERVER="http://localhost:5984",
    COUCHDB_DATABASE="amazon_project_db",
)

couchdb = CouchDBManager()
couchdb.setup(app)

@app.route('/')
def home():
    categories = [
        {"id": 1, "name": "Electronics"},
        {"id": 2, "name": "Books"},
        # Add more categories as needed
    ]
    return render_template('home.html', title="Amazon Project - Accueil", categories=categories)

if __name__ == '__main__':
    app.run(debug=True)