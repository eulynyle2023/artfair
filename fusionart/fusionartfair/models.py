from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

# Student model
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     date_of_birth = models.DateField()
#     address = models.CharField(max_length=255)
#     city_town = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='student_photos', blank=True, null=True)

#     def __str__(self):
#         return self.user.username

# Course model
# class Course(Group):
#     description = models.TextField()
#     length = models.CharField(max_length=100)
#     start = models.DateField()
#     fee = models.DecimalField(max_digits=25, decimal_places=2)

#     class Meta:
#         verbose_name = 'Course'
#         verbose_name_plural = 'Courses'

#     def __str__(self):
#         return self.name
    
# Module model
# class Module(models.Model):
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=50, unique=True)
#     credit = models.IntegerField()
#     category = models.CharField(max_length=100)
#     description = models.TextField()
#     availability = models.BooleanField(default=True)
#     courses_allowed_to_register = models.ManyToManyField(Group, related_name='allowed_modules')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    
# Registration model
# class Registration(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)
#     date_of_registration = models.DateField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     class Meta:
#         unique_together = ('student', 'module')
        
#     def __str__(self):
#         return f"{self.student.username} - {self.module.name}"

# user profile model
# class Profile(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.png', upload_to='profile_pics')

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'
    
