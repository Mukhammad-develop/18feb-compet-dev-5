from django.db import models


class Center(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField()
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=150)
    center = models.ForeignKey(Courses, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phone_number = models.TextField(max_length=15)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Marks(models.Model):
    reyting = models.FloatField(default=0, null=True, blank=True)
    mark = models.FloatField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.student.name

class Teachers(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    phone_number = models.TextField(max_length=15)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name