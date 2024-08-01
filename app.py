from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config # type: ignore

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from routes import init_routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
