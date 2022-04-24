# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status



class TaskTestCase(TestCase):

    def setUp(self):
        """
        Setup para las pruebas
        """
        pass
    

    def test_consulta_si_es_mutante(self):
        """
        Crear consultar un mutante
        """
        client = APIClient()
        
        test_mutant = {
            "": "",
        }

        response = client.post(
            '/mutant/', 
            data=json.dumps(test_mutant),
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_202_CREATED)


