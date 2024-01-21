from django.urls import path
from PlatformReciclagem import views

urlpatterns = [
    path('vendas/', views.sales, name='vendas'),
    path('compradores/', views.buyers_view, name='compradores'),
    path('vendedores/', views.sellers_view, name='vendedores'),
    path('vender/', views.seller_view, name='vender'),
    path('comprar/', views.buyer_view, name='comprar'),
    path('educacaoambiental/', views.environmental_education_view, name='educacaoambiental'),
    path('adicionarvenda/', views.add_sale, name="adicionarvenda"),    
    path('vervenda/<int:id>', views.see_sale),    
    path('atualizarvenda/<int:id>', views.update_sale),  
    path('deletarvenda/<int:id>', views.destroy_sale), 
    path('vervendedor/<int:id>', views.see_seller),  
    path('atualizarvendedor/<int:id>', views.update_seller),  
    path('deletarvendedor/<int:id>', views.destroy_seller), 
    path('vercomprador/<int:id>', views.see_buyer),  
    path('atualizarcomprador/<int:id>', views.update_buyer),  
    path('deletarcomprador/<int:id>', views.destroy_buyer), 
]