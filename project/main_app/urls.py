from django.urls import path
from django.conf import settings

from .views import main, blog, blog_app
from django.conf.urls.static import static
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent

# sapper static

STATIC_APP = APP_DIR / 'sapper_static'

blog_urls = blog_app()

# print(blog_urls)

urlpatterns = [
    path('', main),
    #  path('blog.json', blog),
	 *blog(),
	 *blog_urls
]

# urlpatterns += static('static', document_root=APP_DIR)
