from django.conf.urls import url
from cap import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^submit/$', views.SubmitPageView.as_view()), # Add this /about/ route
]