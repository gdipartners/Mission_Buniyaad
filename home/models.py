from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class Standard(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class AssignSubject(models.Model):
    classname = models.ForeignKey(Standard,verbose_name='Class',on_delete=models.CASCADE)
    subjectname = models.ManyToManyField(Subject,verbose_name=' List of Subjects')


class Chapter(models.Model):
    classname = models.ForeignKey(Standard,verbose_name='Class',on_delete=models.CASCADE)
    subjectname = models.ForeignKey(Subject,verbose_name='Subject',on_delete=models.CASCADE)
    chname = models.CharField('Chapter Name',max_length=50)

    def __str__(self):
        return self.chname

class Content(models.Model):
    classname = models.ForeignKey(Standard,verbose_name='Class',on_delete=models.CASCADE)
    subjectname = models.ForeignKey(Subject,verbose_name='Subject',on_delete=models.CASCADE)
    chname = models.ForeignKey(Chapter,verbose_name='Chapter',on_delete=models.CASCADE)
    added = models.DateField(auto_now=True)
    videotitle = models.CharField('Video Title',max_length=100,default='')
    videourl = EmbedVideoField(verbose_name='Video URL')
    assignmenturl = models.URLField(verbose_name='Assignment URL',max_length=500)
    learningoutcome = models.CharField('Learning Outcome',max_length=100)

    
