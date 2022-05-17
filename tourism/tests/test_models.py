from django.test import TestCase
from tourism.models import Destinations, Comment
from django.utils import timezone

class TestModels(TestCase):

    def test_destinations_model(self):
        #test if Destinations model is passing correctly its values
        destination = Destinations.objects.create(
            tour_title = 'test1',
            booking_start_date='2021-05-30',
            booking_end_date= '2022-05-30',
            location='somewhere',
            price=2000,
            description='test1',
            author='test1',
        )
        destination.save()
        self.assertEquals(destination.tour_title, 'test1')
        self.assertEquals(destination.booking_start_date, '2021-05-30')
        self.assertEquals(destination.booking_end_date, '2022-05-30')
        self.assertEquals(destination.price, 2000)
        self.assertEquals(destination.description, 'test1')
        self.assertEquals(destination.author, 'test1')

    def test_comment_model(self):
        #test if Comment model is related to Destinations model
        destination2 = Destinations.objects.create(
            tour_title = 'test2',
            booking_start_date ='2021-05-30',
            booking_end_date= '2022-05-30',
            location='somewhere',
            price = 2000,
            description = 'test1',
            author = 'test1',
        )
        destination2.save()
        comment = Comment.objects.create(
            #the relation between both models
            post = destination2,
            name = 'John',
            email = 'any@email.com',
            comment = 'test1',
            created_on = timezone.now(),
            active = False,
        )
        comment.save()
        self.assertEquals(comment.post, destination2)