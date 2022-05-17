from django.db import models

# Create your models here.
class Destinations(models.Model):
    author = models.CharField(max_length=200, unique=False)
    tour_title = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.tour_title)


class Comment(models.Model):
    post = models.ForeignKey(Destinations,
       on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
