# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
# class GeeksModel(models.Model):
# 		# fields of the model
# 	title = models.CharField(max_length = 200)
# 	description = models.TextField()
# 	last_modified = models.DateTimeField(auto_now_add = True)
# 	img = models.ImageField(upload_to = "images/")

# 		# renames the instances of the model
# 		# with their title name
# 	def __str__(self):
# 		return self.title



from django.db import models
from django.db.models import Model
# Create your models here.

# class GeeksModel(Model):
# 	geeks_field = models.IntegerField()

# 	def __str__(self):
# 		return self.geeks_field





from django.db import models
  
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title



from django.http import HttpResponse
from django.views import View
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')



class Album(models.Model):
	title = models.CharField(max_length = 30)
	artist = models.CharField(max_length = 30)
	genre = models.CharField(max_length = 30)

	def __str__(self):
		return self.title

class Song(models.Model):
	name = models.CharField(max_length = 100)
	album = models.ForeignKey(Album, on_delete = models.CASCADE)

	def __str__(self):
		return self.name





