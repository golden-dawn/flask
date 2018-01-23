from flask import Flask
from app.models.db_models import db
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db.init_app(app)


@app.route('/')
def index():
    return 'db_api'


@app.route('/populate_db', methods=['POST'])
def populate_db():
    # TODO: populate this method with content from stxeod, opteod;
    # TODO: add stxintraday
    # TODO: use COPY instruction to bulk upload data from files.
    # cnx = db.session.connection()
    # cnx.execute('select * from equities')
    # TODO: load the data from the flash at: /media/cma/CMA_3/...
    pass
