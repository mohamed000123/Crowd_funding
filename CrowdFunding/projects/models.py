from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    category = models.CharField(max_length=50,
                                choices=[('charity', 'charity'),
                                         ('Technology', 'Technology'),
                                         ('Industrial', 'Industrial')])
    totalTarget = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)



class ProjectRating(models.Model):
    class Meta:
        unique_together = (('project', 'user_id'),)

    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    donations = models.IntegerField(default=0)


class ProjectImages(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/projects/images/')


class ProjectTags(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)


class Comments(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()


class Replies(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()


class ReportProject(models.Model):
    type = models.CharField(max_length=50,
                            choices=[('harassment', 'Harassment'),
                                     ('scam', 'Scam'),
                                     ('Inappropriate', 'Inappropriate'),
                                     ('illegal', 'Illegal')])
    msg = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)


class ReportComment(models.Model):
    type = models.CharField(max_length=50,
                            choices=[('harassment', 'Harassment'),
                                     ('scam', 'Scam'),
                                     ('Inappropriate', 'Inappropriate'),
                                     ('illegal', 'Illegal')])
    msg = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)


