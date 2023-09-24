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
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_movies_empty(self):
         res = self.client().get("/movie")
         data = json.loads(res.data)

         self.assertEqual(res.status_code, 404)
         self.assertEqual(data["success"], False)
         self.assertEqual(data["message"], "resource not found")

    def test_get_actors(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_actors_empty(self):
         res = self.client().get("/actor")
         data = json.loads(res.data)

         self.assertEqual(res.status_code, 404)
         self.assertEqual(data["success"], False)
         self.assertEqual(data["message"], "resource not found")

    def test_create_new_movie(self):
        res = self.client().post("/movies/add", json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie_id"])
        

    def test_405_if_movie_creation_not_allowed(self):
        res = self.client().get("/movies/add", json=self.new_movie)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")

    
    def test_create_new_actor(self):
        res = self.client().post("/actors/add", json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor_id"])
        

    def test_405_if_actor_creation_not_allowed(self):
        res = self.client().get("/actors/add", json=self.new_actor)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")


    def test_update_movie(self):
         res = self.client().patch("/movies/update/2", json=self.update_movie)
         data = json.loads(res.data)

         movie = Movie.query.filter(Movie.id == 2).one_or_none()

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data["success"], True)
         self.assertTrue(data["movie_id"])

    def test_update_404_if_movie_does_not_exist(self):
        res = self.client().patch("/movies/update/1000", json=self.update_movie)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_update_actor(self):
         res = self.client().patch("/actors/update/1", json=self.update_actor)
         data = json.loads(res.data)

         actor = Actor.query.filter(Actor.id == 1).one_or_none()

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data["success"], True)
         self.assertTrue(data["actor_id"])

    def test_update_404_if_actor_does_not_exist(self):
        res = self.client().patch("/actors/update/1000", json=self.update_actor)
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    
    def test_delete_movie(self):
         res = self.client().delete("/movies/delete/16")
         data = json.loads(res.data)

         movie = Movie.query.filter(Movie.id == 16).one_or_none()

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data["success"], True)
         self.assertTrue(data["deleted"])

    def test_404_if_movie_does_not_exist(self):
        res = self.client().delete("/movies/delete/1000")
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_delete_actor(self):
         res = self.client().delete("/actors/delete/11")
         data = json.loads(res.data)

         actor = Actor.query.filter(Actor.id == 11).one_or_none()

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data["success"], True)
         self.assertTrue(data["deleted"])

    def test_404_if_actor_does_not_exist(self):
        res = self.client().delete("/actors/1000")
        data = res.data.decode('utf-8')  # Decode the response data to a string
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    
    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()