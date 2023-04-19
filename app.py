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
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
