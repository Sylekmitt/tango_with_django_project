import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    ''' First we will create lists of dictionaries containg the pages
    we want to add into each category. THen we will create a dictionary of dictionaries
    for our own categories. This might seem a little bit confusing, but it allows us 
    to iterate through each data structure, and add the data to our models.'''

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views': 170},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 125},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 242} ]
    
    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 91},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views': 76},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 64} ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 21},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 9} ]

    cats = {
        'Python': {
            'pages': python_pages,
            'views': 128,
            'likes': 64,
        },
        'Django': {
            'pages': django_pages,
            'views': 64,
            'likes': 32,
        },
        'Other Frameworks': {
            'pages': other_pages,
            'views': 32,
            'likes': 16,
        }
    }
    
    # Any additional categories should be added above

    # This code goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views): 
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()