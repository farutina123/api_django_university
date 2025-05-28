from rest_framework import serializers
from .models import Course, UniversityCourse, University


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        read_only_fields = ["id"]
        fields = [
            "id",
            "title",
            "description"
        ]


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        read_only_fields = ["id"]
        fields = [
            "id",
            "name",
            "country"
        ]


class UniversityCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UniversityCourse
        read_only_fields = ["id"]
        fields = [
            "id",
            "university",
            "course",
            "semester",
            "duration_weeks"
        ]


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        read_only_fields = ["id"]
        fields = [
            "title"
        ]


class UniversityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        read_only_fields = ["id"]
        fields = [
            "name"
        ]



class UniversityCourseNameSerializer(serializers.ModelSerializer):
    university = UniversityNameSerializer()
    course = CourseNameSerializer()
    class Meta:
        model = UniversityCourse
        read_only_fields = ["id"]
        fields = [
            "id",
            "university",
            "course",
            "semester",
            "duration_weeks"
        ]