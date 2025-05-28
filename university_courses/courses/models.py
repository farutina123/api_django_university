from django.db import models


class University(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    def __str__(self):
        return self.name if len(self.name) < 15 else f"{self.name[:15]}..."


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    def __str__(self):
        return self.title if len(self.title) < 15 else f"{self.title[:15]}..."


class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='universityCourses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coursesUniversity')
    semester = models.CharField(max_length=20)
    duration_weeks = models.PositiveIntegerField(max_length=200)
    def __str__(self):
        return self.semester if len(self.semester) < 15 else f"{self.semester[:15]}..."
