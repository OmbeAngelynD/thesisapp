from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(
    auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
class Meta:
    abstract = True

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Thesis(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Advisor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    thesis = models.ForeignKey(Thesis,on_delete=models.CASCADE, null=True, blank=True)
