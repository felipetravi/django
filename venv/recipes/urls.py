from django.urls import path
from recipes.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contato/', contato),
    path('sobre/', sobre),
    path('', home)
]
