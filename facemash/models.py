from __future__ import unicode_literals

from django.db import models

# Create your models here.
def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    # PostModel = instance.__class__
    # new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(instance.Name, filename)
class photo(models.Model):
    Name = models.CharField(max_length=120)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                            width_field = "width_field",
                            height_field = "height_field")
    height_field = models.IntegerField(default=1000)
    width_field = models.IntegerField(default=1000)
    Discription = models.TextField(null=True)
    nlikes=models.IntegerField(null=True,default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.Name

    def __str__(self):
        return self.Name
class rank_db(models.Model):
    id_a = models.IntegerField()
    id_b = models.IntegerField()
    score = models.IntegerField()
class total_likes(models.Model):
    Name = models.CharField(max_length=120)
    t_l=models.IntegerField(null=True,default=0)
