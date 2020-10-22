from django.urls import path
#from .views import view_function
from .views import HomePageView

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('', Calculation.as_view(num=100), name="calculation"),
]
#sending num perameter to template