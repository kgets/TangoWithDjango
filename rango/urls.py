from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# /polls/
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.category, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)