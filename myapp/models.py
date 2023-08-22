from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200,default="Project Title")
    description = models.TextField(max_length=1000,default="Some quick example text to build on the card title and make up the bulk of the card's content.")
    about = models.TextField(max_length=1000,default="Click the below button and Explore more about the website.")
    btn = models.CharField(max_length=100,default="Go somewhere")
    url = models.URLField(default="https://debasishmohanta.netlify.app/")
    image = models.IntegerField(null=False)
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

