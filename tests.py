import unittest
import json
from os import environ, getenv

from application.models import db, Genes
from application import *


SQL_URI = getenv('SQLALCHEMY_DATABASE_URI')

app = create_app()      # Get the application context

class TestUser(unittest.TestCase):

    # Setup for tests...
    def setUp(self):
        """
            This method is run before each test.
            Database setup, if any, must be done here.
        """
        self.client = app.test_client()  # Get the flask test client
        app.testing = True


    def tearDown(self):
        """
            Destroy temporary setup done for tests.
            This is called after each test
        """
        pass


    def test_get_root(self):
        response = self.client.get('/')

        # We respond with 405 for any routes other than /genes
        self.assertEqual(response.status_code, 405)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data["message"], "Method Not Allowed")

    
    def test_put_patch_post(self):

        response = self.client.post('/', data=json.dumps({'foo': 'bar'}))
        self.assertEqual(response.status_code, 405)

        response = self.client.put('/genes', data=json.dumps({'foo': 'bar'}))
        self.assertEqual(response.status_code, 405)

        response = self.client.patch('/test', data=json.dumps({'foo': 'bar'}))
        self.assertEqual(response.status_code, 405)


    def test_genes_query(self):
        # Get 400 if query lengths are not >= 3
        response = self.client.get('/genes', query_string={'lookup':'xy'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data["message"], "Lookup query length must be greater than 2.")

        response = self.client.get('/genes', query_string={'lookup':'xyx', 'species': 'xx'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data["message"], "Species query length must be greater than 2.")

        # Missing the required parameter
        response = self.client.get('/genes', query_string={'species':'xy'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data["message"], "Lookup query length must be greater than 2.")

        expected = [
            {
                "gene": "BRCA1", 
                "location": "KB913268.1:364684-386426", 
                "species": "zonotrichia_albicollis", 
                "stable_id": "ENSZALG00000004870"
            }, 
            {
                "gene": "BRCA2", 
                "location": "KB913047.1:6379056-6413486", 
                "species": "zonotrichia_albicollis", 
                "stable_id": "ENSZALG00000003961"
            }, 
            {
                "gene": "BRCC3", 
                "location": "KB913059.1:7659861-7666402", 
                "species": "zonotrichia_albicollis", 
                "stable_id": "ENSZALG00000002479"
            }
        ]


        # It is best to create a temporary database for tests, but 
        # we do not have that luxury in this case. Just test against a valid API request.
        response = self.client.get('/genes', query_string={'lookup': 'brc', 'species':'zono'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data, expected)

if __name__ == '__main__':
    unittest.main()
