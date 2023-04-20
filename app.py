import sys
print(sys.executable)

from flask import Flask, render_template
import couchdb

app = Flask(__name__)

couchdb_server = couchdb.Server("http://localhost:5984")

@app.route('/')
def home():
    categories = [
        {"id": 1, "name": "Electronics"},
        {"id": 2, "name": "Books"},
        # Add more categories as needed
    ]
    return render_template('home.html', title="Amazon Project - Accueil", categories=categories)

@app.route('/category/<int:category_id>')
def category(category_id):
    return render_template('category.html', title=f"Amazon Project - Category {category_id}")

if __name__ == '__main__':
    app.run(debug=True)
