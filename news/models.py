from django.db import models
#if the class is creating, automaticly will create base data this
class Articles(models.Model):
  title = models.CharField(max_length = 120)
  post = models.TextField()
  date = models.DateTimeField()

  def __str__(self):
    return self.title