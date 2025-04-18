AUTHOR = 'aadith thiruvallarai'
SITENAME = 'aadith thiruvallarai'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/taadith'),
    ('linkedin', 'https://www.linkedin.com/in/aadithth/'),
)

DEFAULT_PAGINATION = 10

THEME = 'themes/Peli-Kiera'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
