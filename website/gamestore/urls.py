from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact-success'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('create/', views.game_create_view, name="game_create"),
    path('list/', views.game_list_view, name="game_list"),
    path('update/<int:game_id>/', views.game_update_view, name="game_update"),
    path('delete/<int:game_id>/', views.game_delete_view, name="game_delete"),
    path('ims/', views.game_index_view, name="ims"),
]
