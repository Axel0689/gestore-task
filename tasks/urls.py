from django.urls import path
from . import views

urlpatterns = [
    # URL patterns per le viste dei task
    path('', views.task_list, name='task_list'),
    
    path('dashboard/', views.dashboard, name='dashboard'),  # Nuovo percorso per la dashboard
    
    # Dettaglio di un singolo task
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/toggle/', views.task_toggle_complete, name='task_toggle_complete'),
    
    # URL patterns per la gestione dei task (creazione, modifica, eliminazione)
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
    # URL patterns per l'autenticazione
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]