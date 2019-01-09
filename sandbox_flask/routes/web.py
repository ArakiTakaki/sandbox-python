from flask import Flask
from controllers import index
from flask import Flask


def registerRoutes(app):
    app.route('/')(index.get)
    print('routes')