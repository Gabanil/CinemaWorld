"""
URL configuration for Product project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cinema.views import MovieAPIView, ResevationAPIView, MovieDetailAPIView, SessionsViewList, MovieAvalableSession, ReservationTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path("reservation/", ReservationTemplate.as_view()),
    path("", MovieAPIView.index),
    path("movie/<int:pk>/", MovieDetailAPIView.as_view()),
    path("session/", SessionsViewList.as_view()),
    path("movie/<int:pk>/sessions/", MovieAvalableSession.as_view()),
    path("movie/<int:pk>/sessions/<int:session_id>/reservation/", ResevationAPIView.as_view()),
    ]
    # path("api/v1/", MovieAPIView.as_view(), name="api_test") начало апишки


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
