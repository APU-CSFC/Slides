Concepts to know about
----------------------
 * **MVC** - Model-View-Controller
 * **MVT** - Model-View-Template
 * Links to read from:
     * https://en.wikipedia.org/wiki/Model-view-controller
     * http://www.codinghorror.com/blog/2008/05/understanding-model-view-controller.html
 
Example of large-scale MVC/T Web frameworks/CMS in python
---------------------------------------------------------
 * Plone - <http://plone.org>
 * Django (_D_ is silent) - <https://www.djangoproject.com>
 * Pyramid - <http://www.pylonsproject.org/projects‎>
 
Minimalistic MVC/T Web frameworks
---------------------------------
 * Bottle - <http://bottlepy.org/‎>
 * Flask - <http://flask.pocoo.org>
 * web.py - <http://webpy.org>

simple web.py app to say hello to visitors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    import web
 
    urls = (
        '/', 'Index',
        )
 
    class Index(object):
        def GET(self):
            return 'Hello!'
 
    if __name__ == '__main__':
        app = web.application(urls, globals())
        app.run()

say hello to visitor with name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::
    
    import web
 
    urls = (
        '/', 'Index',
        '/([a-zA-Z]+)', 'HelloName',
        # regular expression (regexp) to catch word of any length
        )
 
    class Index(object):
        def GET(self):
            return 'Hello!'
 
    class HelloName(object):
        def GET(self, name):
        # regexp was passed as argument with the request
           return 'Hello, %s!' % name

    if __name__ == '__main__':
        app = web.application(urls, globals())
        app.run()

web app to make a resume
^^^^^^^^^^^^^^^^^^^^^^^^
::
    
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
        def GET(self, handle):  
        # regexp was passed as argument with the request
            base_url = 'https://api.github.com/users/'
            req = requests.get(base_url + handle)
            resp = req.json()
            avatar = resp['avatar_url']
            name = resp['name']
            url = resp['html_url']
            return render.profile(handle, name, avatar, url)
 
    if __name__ == '__main__':
        app = web.application(urls, globals())
        app.run()
 
html template code. It's located under templates/profile.html
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $def with (handle, name, avatar, url)
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Resume of $handle</title>
        </head>
        <body>
            <h1>This is a resume for $name</h1>
            <p><img src="$avatar" /></p>
            <p>Repositories of code $name has written can be found at: <a href="$url">$url</a>.</p>
        </body>
    </html>
