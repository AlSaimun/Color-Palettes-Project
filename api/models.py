from django.db import models
from django.contrib.auth.models import User
# Create your models here.


"""color palette Model"""
class ColorPalette(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,unique=True)
    dominant_colors = models.JSONField()
    accent_colors = models.JSONField()
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f'{self.name}'


class FavoritePalettes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    palette = models.ForeignKey(ColorPalette,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user.username}    {self.palette.name}'

    
