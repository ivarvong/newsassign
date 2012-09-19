from django.db import models
from django.contrib.auth.models import User
class Story(models.Model):
    slug = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    
    def __unicode__(self):
      return self.slug
      
    def was_created_recently(self):
      return self.created_date >= timezone.now() - datetime.timedelta(days=1)  
            
class Assignment(models.Model):
    story = models.ForeignKey(Story)
    slug = models.CharField(max_length=200)
    description = models.TextField()
    desk = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    
    who_cares = models.CharField(max_length=200)
    
    editor = models.ForeignKey(User, related_name="%(class)s_editor_ownership")
    reporter = models.ForeignKey(User, related_name="%(class)s_reporter_ownership")
    
    created_date = models.DateTimeField('date created')
    deadline_date = models.DateTimeField('deadline')
    publish_date = models.DateTimeField('date published')
    
    def __unicode__(self):
      return self.slug
      
    def was_created_recently(self):
      return self.created_date >= timezone.now() - datetime.timedelta(days=1)  
