import json
from rest_framework import status
from django.utils import timezone
from django.http import response
from django.urls import reverse
from tourism.models import Destinations, Comment
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TourismTestCase(APITestCase):

    def setUp(self):
        
        self.headerInfo = {'content-type': 'application/json'}
        
        # PASSO 1

        # Criação de objetos que serão 
        # utilizados nos testes dos endpoints.

        # Instance do objeto Destinations.
        self.destination = Destinations.objects.create(
            tour_title = 'test1',
            booking_start_date='2021-05-30',
            booking_end_date= '2022-05-30',
            price=2000,
            description='test1',
            location='somewhere',
            author='test1',
        )
        self.destination.save()

        # Instance do objeto Comment.
        self.comment = Comment.objects.create(
            #the relation between both models
            post = self.destination,
            name = 'John',
            email = 'any@email.com',
            comment = 'test1',
            created_on = timezone.now(),
            active = False,
        )
        self.comment.save()

        # PASSO 2

        # Criação de dados para serem usados nos testes.
        self.destination_data = {
            'tour_title' :'test1',
            'booking_start_date':'2021-05-30',
            'booking_end_date':'2022-05-30',
            'price':2000,
            'description':'test1',
            'location':'somewhere',
            'author':'test1'
        }

        self.comment_data = {
            'post':self.destination.id,
            'name':'John',
            'email':'any@email.com',
            'comment':'test1',
            'created_on':timezone.now(),
            'active':False,
        }

        # PASSO 3

        # Criação da representação dos endpoints
        # que serão utilizados nos testes.

        self.url_destination_list = reverse('tourism:destinations-list')
        self.url_destination_detail = reverse('tourism:destinations-detail',
                                        kwargs={'pk': self.destination.pk})

        self.url_comment_url_list = reverse('tourism:comments-list')
        self.url_comment_detail = reverse('tourism:comments-detail', 
                                        kwargs={'pk': self.comment.pk})

    # PASSO 4
    # Usar os dados criados no setUp() 
    # para criar as funções de teste.

    def test_get_destination(self):
        """GET method"""
        response = self.client.get(self.url_destination_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_destination(self):
        """ Test POST method for Destination endpoint"""
        response = self.client.post(
            self.url_destination_list, self.destination_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_destination(self):
        """ Test PUT method for Destination endpoint"""
        response = self.client.put(
            self.url_destination_detail, self.destination_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_destination(self):
        """ Test DELETE method for Destination endpoint"""
        response = self.client.delete(
            self.url_destination_detail, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_comment(self):
        """GET method"""
        response = self.client.get(self.url_comment_url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        """ Test POST method for Comment endpoint"""
        response = self.client.post(
            self.url_comment_url_list, self.comment_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_comment(self):
        """ Test PUT method for Comment endpoint"""
        response = self.client.put(
            self.url_comment_detail, self.comment_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        """ Test DELETE method for Comment endpoint"""
        response = self.client.delete(
            self.url_comment_detail, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)