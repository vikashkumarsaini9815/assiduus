from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255, null = True, blank = True)
    email = models.EmailField(unique = True)
    Token = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
            return self.username


class Message(models.Model):
    message = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, related_name='users',on_delete=models.CASCADE)

    def __str__(self):
            return self.message

   
