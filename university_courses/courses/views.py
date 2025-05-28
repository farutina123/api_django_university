from rest_framework.viewsets import ModelViewSet
from .models import UniversityCourse, University, Course
from .serializers import UniversitySerializer, UniversityCourseSerializer, CourseSerializer, UniversityCourseNameSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg




class UniversityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    @action(detail=True, url_path="courses",
            url_name="university-courses", serializer_class=UniversityCourseNameSerializer)
    def university_courses(self, request, pk=None):

        courses = UniversityCourse.objects.filter(university_id=pk)
        courses_serializer = UniversityCourseNameSerializer(courses, many=True)
        return Response(courses_serializer.data, status=200)


    @action(detail=True, url_path="course-stats",
            url_name="university-courses-stats")
    def university_courses_stats(self, request, pk=None):
        courses = {}
        courses['total_courses'] = UniversityCourse.objects.filter(university_id=pk).count()
        courses_avg = UniversityCourse.objects.filter(university_id=pk).aggregate(avg_duration_weeks=Avg('duration_weeks'))
        courses['average_duration'] = courses_avg['avg_duration_weeks']
        return Response(courses, status=200)


class UniversityCourseViewSet(ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ["course__title__contains", "university__name__contains"]
    filterset_fields = {
        'course__title': ["exact", "contains"],
        'semester': ["exact", "contains"]
    }
    ordering_fields = ["duration_weeks"]

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


