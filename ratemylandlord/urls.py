from django.urls import path
from .views import indexPageView
from .views import viewReviewsPageView
from .views import editReviewsPageView
from .views import aboutPageView, addReviewsPageView

urlpatterns = [    
    path("viewreviews/", viewReviewsPageView, name="viewreviews"),
    path("editreviews/", editReviewsPageView, name="editreviews"),
    path("addreviews/", addReviewsPageView, name="addreviews"),
    path("about/", aboutPageView, name="about"),
    path("", indexPageView, name="index"),
]           