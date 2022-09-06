from django.urls import path
from . import views

app_name = 'relatorio'

urlpatterns = [
    path('', views.relatorio_list, name="list"),
    path('relatorio/<int:rel_id>/', views.relatorio_visualiza, name="visualiza"),
    path('delete/<int:rel_id>/', views.relatorio_deleta, name="deleta"),
    path('edita/<int:rel_id>/', views.relatorio_edita, name="edita"),
    path('criar/', views.relatorio_cria, name="cria"),
]
