from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import StudentsView

router=DefaultRouter()
router.register("students",StudentsView,basename="students")

urlpatterns =[
    
]+router.urls