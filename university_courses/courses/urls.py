from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views

router = DefaultRouter()
router.register("University", views.UniversityViewSet)
router.register("Course", views.CourseViewSet)
router.register("UniversityCourse", views.UniversityCourseViewSet)


urlpatterns = [
    path("", include(router.urls))
]