from flask import Flask
from routes import web
from middlewares import middleware

app = Flask(__name__)

web.registerRoutes(app)
middleware.registerMiddleware(app)

app.run(debug=True, port=3000, host='0.0.0.0')