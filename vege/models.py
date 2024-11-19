


from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=255)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipes/', blank=True, null=True)  # Adjust upload path as needed
    recipe_view_count = models.IntegerField(default=1) 

    def __str__(self):
        return self.recipe_name