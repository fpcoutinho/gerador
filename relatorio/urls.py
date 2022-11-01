from django.urls import path
from . import views

app_name = 'relatorio'

urlpatterns = [
    path('', views.relatorio_list, name="list"),
    path('relatorio/<int:rel_id>/', views.relatorio_visualiza, name="visualiza"),
    path('delete/<int:rel_id>/', views.relatorio_deleta, name="deleta"),
    path('edita/<int:rel_id>/', views.relatorio_edita, name="edita"),
    path('exporta/<int:rel_id>/', views.relatorio_exporta, name="exporta"),
    path('criar/', views.relatorio_cria, name="cria"),
    path('addplanejamento/<int:rel_id>/', views.planejamento_add, name="addplanejamento"),
    path('editaplanejamento/<int:rel_id>/', views.planejamento_edita, name="editaplanejamento"),
    path('addexternas/<int:rel_id>/', views.externas_add, name="addexternas"),
    path('editaexternas/<int:rel_id>/', views.externas_edita, name="editaexternas"),
    path('addqualitativas/<int:rel_id>/', views.qualitativas_add, name="addqualitativas"),
    path('editaqualitativas/<int:rel_id>/', views.qualitativas_edita, name="editaqualitativas"),
    path('addquantitativas/<int:rel_id>/', views.quantitativas_add, name="addquantitativas"),
    path('editaquantitativas/<int:rel_id>/', views.quantitativas_edita, name="editaquantitativas"),
]
