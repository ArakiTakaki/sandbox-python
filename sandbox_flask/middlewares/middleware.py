
def registerMiddleware(app):

    @app.before_request
    def before():
        print('before')

    @app.after_request
    def after(response):
        print('after')
        return response
