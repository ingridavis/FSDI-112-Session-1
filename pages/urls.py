from django.urls import path
#from .views import view_function
from .views import HomePageView, AboutPageView # from this folder find the views module and import ____
from django.conf import settings
from django.conf.urls.static import static

# Takes a list and use path to specify route, function that handles the route
urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('', HomePageView.as_view(), name="home"),
    path('aboutme', AboutPageView.as_view(), name="aboutme"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)