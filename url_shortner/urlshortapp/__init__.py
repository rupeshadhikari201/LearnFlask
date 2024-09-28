from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'hosdh045sdf4544sdfs7s64s1s4'
    from . import urlshortapp
    app.register_blueprint(blueprint=urlshortapp.bp)
    return app