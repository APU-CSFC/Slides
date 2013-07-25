import web

urls = (
    '/', 'Index',
    '/([a-zA-Z]+)', 'HelloName',
    )

class Index(object):
    def GET(self):
        return 'Hello!'

class HelloName(object):
    def GET(self, name):
        return 'Hello, %s!' % name

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
