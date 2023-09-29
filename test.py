import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
     
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_user = os.environ.get('db_user')
        self.database_pwd = os.environ.get('db_pwd')
        self.database_name = "castingagency"
        self.database_path = "postgresql://{}:{}@{}/{}".format(self.database_user, self.database_pwd, "localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {"title": "Goblin", "release_year": "2017"}
        self.new_actor = {"name": "Gong Yoo", "age": "40", "gender": "Male", "movie_id": "4"}

        self.update_movie = {"release_year": "2019"}
        self.update_actor = {"age": "24"}

        self.header_ca = {'Content-Type': 'application/json', 'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZhMjZlYTgyNWVmNGY1ZmFiNjYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTYzMjUwLCJleHAiOjE2OTU5NzA0NTAsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.aFisxHf33hpedz40Q_gRvHK0pzr2DjQCnb07fzLHbIuofd-YCUECwKX47VJtoiSuz7LtnFsUW6eTUpIuij7XyGwdLJ1bfNe7P5It9rnkuQa9pyR0nFI-66iJIcSutWj7CLVfaV8N-eibsKt1wVa2Hhek_2mTtmfk61OfvioSgrMKmineem6uFujQ5cMXzoebyY4ybKje1OWuvsJHYG29krDqqhp0tCoUt9_Uo6a0RjMpctnfSGyiHqldZQIAQe6me4BUaJGwxziGtaPM07T27dOVMopRkwe8_fxMVhONMejnOYsTMOLhnl7piEzoIXzSUv-4cB-s6KqzEB5bhNEGeQ"}
        self.header_ep = {'Content-Type': 'application/json', 'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZmMzdmZDQ4YWU0OTEwZTJkOTYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTY3NTA1LCJleHAiOjE2OTU5NzQ3MDUsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.RyM-__H27tkuJhRpOI6PyctquQ-YTqHp0MamUEYvXXbcZhzPOBE16nwx42p24LdEwHGBj9WG8e7e96pscbgoL2O_FZ2pHWizbxuuX5qn4ZjZVG8SsbnLJ-Ej_GZPxaszIZOnpVVvp_AKmZoKST7kTlrWdowzaddArdk_j0HI_iOmdT5-G61QheZE6oO4bQLgfpvom189oNVX2a3f6acxGzF4apR7BAtVtHMPvDyUeT3hJn1AzqgmKU0GIYHJC0JNx9xhzPyiUh45NNirTVnPYQXiPxZhS4CD3YYW5qpcCS5Q1p_XMbcfLYrABgC8HjCVWqXQ9T_gZn8x0Q6oJMH2SA"}
        self.header_cd = {'Content-Type': 'application/json', 'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZmMzdmZDQ4YWU0OTEwZTJkOTYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTY3OTczLCJleHAiOjE2OTU5NzUxNzMsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.V9m0gTmh6D1ZVWv6fue0ycdVr-ERJmZXyagj0gb0lKO_oWEQgU816nQBR8a9kMolBcomtYABBPPiitTvRFtwHb_HszUUZMBO1OPicWcMeGJW7prOSTMIT4ailsi2wdUQ31eE997xOp626Ly4URWo6FMMeoTsEpHAT4lLN9RAxCA-1pc4Bg8LMVhgDStPEBARXcP94NsgAcouVRqBrzBFEgsHuYgWb1ncBy4wGLeLnBo2wKmbVEx_fc1HBpR7wQEiRPzIiEOfQSjHV6Aj5QoClU1TtwyEdb379V3p0n9NADgIHyPQrWirWBn834jlObHBgGbvpxuNuJcy4-4H79dlgg"}
         
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_movies(self):
        res = self.client().get("/movies", headers=self.header_ca)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_movies_empty(self):
         res = self.client().get("/movie", headers=self.header_ca)
         data = json.loads(res.data)

         self.assertEqual(res.status_code, 404)
         self.assertEqual(data["success"], False)
         self.assertEqual(data["message"], "resource not found")

    def test_get_actors(self):
        res = self.client().get("/actors", headers=self.header_ca)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_actors_empty(self):
         res = self.client().get("/actor", headers=self.header_ca)
         data = json.loads(res.data)

         self.assertEqual(res.status_code, 404)
         self.assertEqual(data["success"], False)
         self.assertEqual(data["message"], "resource not found")

    def test_create_new_movie(self):
        res = self.client().post("/movies/add", json=self.new_movie, headers=self.header_ep)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie_id"])
        

    def test_405_if_movie_creation_not_allowed(self):
        res = self.client().get("/movies/add", json=self.new_movie, headers=self.header_ep)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")

    
    def test_create_new_actor(self):
        res = self.client().post("/actors/add", json=self.new_actor, headers=self.header_cd)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor_id"])
        

    def test_405_if_actor_creation_not_allowed(self):
        res = self.client().get("/actors/add", json=self.new_actor, headers=self.header_cd)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")


    def test_update_movie(self):
         res = self.client().patch("/movies/update/2", json=self.update_movie, headers=self.header_cd)
         data = json.loads(res.data)

         movie = Movie.query.filter(Movie.id == 2).one_or_none()

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data["success"], True)
         self.assertTrue(data["movie_id"])

    def test_update_404_if_movie_does_not_exist(self):
        res = self.client().patch("/movies/update/1000", json=self.update_movie, headers=self.header_cd)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_update_actor(self):
         res = self.client().patch("/actors/update/1", json=self.update_actor, headers=self.header_cd)
         data = json.loads(res.data)

         actor = Actor.query.filter(Actor.id == 1).one_or_none()

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data["success"], True)
         self.assertTrue(data["actor_id"])

    def test_update_404_if_actor_does_not_exist(self):
        res = self.client().patch("/actors/update/1000", json=self.update_actor, headers=self.header_cd)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    
    def test_delete_movie(self):
         res = self.client().delete("/movies/delete/4", headers=self.header_ep)
         data = json.loads(res.data)

         movie = Movie.query.filter(Movie.id == 4).one_or_none()

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data["success"], True)
         self.assertTrue(data["deleted"])

    def test_404_if_movie_does_not_exist(self):
        res = self.client().delete("/movies/delete/1000", headers=self.header_ep)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_delete_actor(self):
         res = self.client().delete("/actors/delete/15", headers=self.header_cd)
         data = json.loads(res.data)

         actor = Actor.query.filter(Actor.id == 15).one_or_none()

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data["success"], True)
         self.assertTrue(data["deleted"])

    def test_404_if_actor_does_not_exist(self):
        res = self.client().delete("/actors/1000", headers=self.header_cd)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    
    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()