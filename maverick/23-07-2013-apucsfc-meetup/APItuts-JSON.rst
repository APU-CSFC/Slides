Reading JSON from API(s)
========================
::
    
    # import the necessary library
    import requests
    import json
    
    # define the base url of the API you want to read from. 
    # (We'll be using github public API)
    base_url = 'https://api.github.com/users/'
    
    # let's define username on github.
    username = 'mavjs'
    req = requests.get(base_url+username)
    
    resp = req.json()
    print resp
    
    avatar = resp['avatar_url'].split('?')[0]
    print avatar
    
    name = resp['name']
    print name

    githuburl = resp['html_url']
    print githuburl
