python-rottentomatoes
=====================

A super-simple python wrapper for the RottenTomatoes JSON API.

##Usage

You must first have an API key from developer.rottentomatoes.com

    from python-rottentomatoes import RottenTomatoesAPI
    api = RottenTomatoesAPI('uR_aPi_keY_rItE_huR')
    
Let's get the top rentals from Rotten Tomatoes. There are several different syntaxes, depending on how you want to do it. It's pretty flexible.
 
First, add arguments like you would to build the url and call the api!

    api('lists', 'dvds', 'top_rentals')
    # http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/top_rentals.json?apikey=uR_aPi_keY_rItE_huR
    # {"movies":[{"id":"770675766","title":"The Hobbit: An Unexpected Journey"... 
    
or use the get method if you don't want to use the callable,
    
    api.get('lists', 'dvds', 'top_rentals')
    # http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/top_rentals.json?apikey=uR_aPi_keY_rItE_huR
    # {"movies":[{"id":"770675766","title":"The Hobbit: An Unexpected Journey"...
    
or set the api to specific directories, to make it easier if you're only looking in one directory.

    api.set('lists', 'dvds')
    # sets base_url to http://api.rottentomatoes.com/api/public/v1.0/lists/dvds
    
    api('top_rentals')
    # http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/top_rentals.json?apikey=uR_aPi_keY_rItE_huR
    # {"movies":[{"id":"770675766","title":"The Hobbit: An Unexpected Journey"...
    
or the same thing in one line...

    api.set('lists', 'dvds').get('top_rentals')
    # which is the same as
    api.set('lists', 'dvds', 'top_rentals').get()
    
To get out of the set directory, just call set again to clear the directory.

    api.set()
    # sets base_url to http://api.rottentomatoes.com/api/public/v1.0/
    
Need to paginate? No problem! Any query string arguments can just be added via a keyword argument.

    api('lists', 'movies', 'in_theaters', page=2)
    # http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=uR_aPi_keY_rItE_huR&page=2
    # {"total":128,"movies":[{"id":"771225176","title":"Hansel and Gretel...

## Other options

https://github.com/zachwill/rottentomatoes

https://github.com/cvega/WWW-RottenTomatoes-Python
