import web
import requests

urls = (
    '/', 'Index',
    '/([a-zA-Z]+)', 'Profile',
    )

# dir for all templates, name of template corresponds to class
render = web.template.render('templates')

class Index(object):
    def GET(self):
        return 'Hello!'

class Profile(object):
    def GET(self, handle): # regexp was passed as argument with the request
        base_url = 'https://api.github.com/users/'
        req = requests.get(base_url + handle)
        resp = req.json()
        avatar = resp['avatar_url'].split('?')[0]
        name = resp['name']
        url = resp['html_url']
        return render.profile(handle, name, avatar, url)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
