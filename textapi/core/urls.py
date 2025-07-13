from django.urls import path
from .views import RegisterView, LoginView, upload_paragraphs, search_word, home_view
from .views import register_view, login_view, upload_view, search_view, logout_view

urlpatterns = [

    # Root URL: renders the login page or home landing
    path('', home_view),     # Shows login page at http://127.0.0.1:8000/

    # Frontend routes for HTML templates
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('upload/', upload_view, name='upload'),
    path('search/', search_view, name='search'),
    path('logout/', logout_view, name='logout'),

      # API routes (used for external API consumers)
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/upload/', upload_paragraphs),
    path('api/search/', search_word),
]