from django.urls import path
from .views import indexPageView
from .views import viewReviewsPageView
from .views import editReviewsPageView
from .views import contactPageView

urlpatterns = [
    path("", indexPageView, name="index"),    
    path("viewreviews/", viewReviewsPageView, name="viewreviews"),
    path("editreviews/", editReviewsPageView, name="editreviews"),
    path("contact/", contactPageView, name="contact"),
]           