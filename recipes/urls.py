from django.urls import path
from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home, name='home'), 
    path('sobre/', sobre, name='sobre'),  
    path('contato/', contato, name="contato") 
]