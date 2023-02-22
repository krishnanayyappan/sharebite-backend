from django.urls import path
from . import views

urlpatterns = [
    # View entire restaurant menu
    path('', views.view_menu, name='home'),

    # Endpoints for CRUD operations on Section
    path('sections/', views.get_sections, name='get-sections'),
    path('sections/add', views.add_sections, name='add-sections'),
    path('sections/update/<int:pk>/', views.update_sections, name='update-sections'),
    path('sections/delete/<int:pk>/', views.delete_sections, name='delete-sections'),

    # Endpoints for CRUD operations on Item
    path('items/', views.get_items, name='get-items'),
    path('items/add', views.add_items, name='add-items'),
    path('items/update/<int:pk>/', views.update_items, name='update-items'),
    path('items/delete/<int:pk>/', views.delete_items, name='delete-items'),

    # Endpoints for CRUD operations on Modifier
    path('modifiers/', views.get_modifiers, name='get-modifiers'),
    path('modifiers/add', views.add_modifiers, name='add-modifiers'),
    path('modifiers/update/<int:pk>/', views.update_modifiers, name='update-modifiers'),
    path('modifiers/delete/<int:pk>/', views.delete_modifiers, name='delete-modifiers'),

    # Endpoints for mapping Items and Modifiers
    # path('mapping/', views.get_mapping, name='get-mapping'),
    path('mapping/add/<int:pk>/', views.map_items_and_modifiers, name='add-mapping'),
    path('mapping/update/<int:pk>/', views.map_items_and_modifiers, name='update-mapping'),
    # path('mapping/delete/<int:pk>/', views.delete_mapping, name='delete-mapping'),
]
