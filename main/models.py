from django.db import models

# Create your models here.
class Joke(models.Model):
    CATEGORIES = [
        ("classic", "1"),
        ("science", "2"),
        ("family", "3"),
        ("bar_jokes", "4")
    ]
    content = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return self.content
    
