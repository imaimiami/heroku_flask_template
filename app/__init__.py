# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace with a secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# 開発環境用設定   
if os.environ.get('RACK_ENV') is not 'production':
    app.debug = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/test'

    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)


from view import views
app.register_blueprint(views)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)