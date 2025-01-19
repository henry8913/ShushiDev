from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('contattaci/', views.contact, name='contact'),
    path("successo/", views.successo_contatto, name="successo_contatto"),
    path('carrello/', views.carrello, name='carrello'),
    path('aggiungi/<int:roll_id>/', views.aggiungi_al_carrello, name='aggiungi_al_carrello'),
    path('conferma_ordine/', views.conferma_ordine, name='conferma_ordine'),
    path('rimuovi/<int:roll_id>/', views.rimuovi_dal_carrello, name='rimuovi_dal_carrello'),
]