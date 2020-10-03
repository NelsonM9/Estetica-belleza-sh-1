from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import *
from flask_cors import CORS
from db.model import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "postgresql://postgres:pass1234@localhost:5432/Estetica_belleza_sh"

CORS(app, supports_credentials= True)
db.init_app(app)

app.add_url_rule(client["signin"], view_func= client["view_func_signin"])

if __name__ == "__main__":
    app.run(port= 5000, debug= True)
