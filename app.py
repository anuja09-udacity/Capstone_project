import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import db
import random

from auth import AuthError, requires_auth
from models import setup_db, Movie, Actor


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available movies.
    """
    @app.route('/movies')
    @requires_auth('view:movies')
    def get_movies(jwt):
        movies = Movie.query.all()

        if not movies:
            abort(404)

        movies = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': movies
        })
    
    """
    @TODO:
    Create an endpoint to handle GET requests for actors
    """
    @app.route('/actors')
    @requires_auth('view:actors')
    def get_actors(jwt):
        actors = Actor.query.all()

        if not actors:
            abort(404)

        actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors
        })


    """
    @TODO:
    Create an endpoint to ADD a new movie.
    """
    @app.route('/movies/add', methods=['POST'])
    @requires_auth('add:movies')
    def add_movie(jwt):

        body = request.get_json()

        title = body['title']
        release_year = body['release_year'] 

        if not (title and release_year):
            abort(422)   

        try:
            movie = Movie(title=title, release_year=release_year)
            movie.insert()  

            return jsonify({
                'success': True,
                'movie_id': movie.id
            })
        except BaseException:  
            abort(405)
            


    """
    @TODO:
    Create an endpoint to ADD an actor against a movie id.
    """
    @app.route('/actors/add', methods=['POST'])
    @requires_auth('add:actors')
    def add_actor(jwt):
        body = request.get_json()

        if body is None:
            abort(400)

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')
        movie_id = body.get('movie_id')
    #    print(name, age, gender, movie_id)

        if not (name and age and gender and movie_id):
            abort(422)

        try:
            actor = Actor(name=name,
                          age=age,
                          gender=gender,
                          movie_id=movie_id)
            actor.insert()

            return jsonify({
                'success': True,
                'actor_id': actor.id
            })
        except BaseException as e:
            print(e)
            abort(405)


    """
    @TODO:
    Create an endpoint to update details of a movie for the selected id
    """

    @app.route('/movies/update/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movies(jwt, movie_id):
        movie = Movie.query.get(movie_id)

        if movie:
            try:
                body = request.get_json()

                title = body.get('title')
                release_year = body.get('release_year')

                if title:
                    movie.title = title
                if release_year:
                    movie.release_year = release_year

                movie.update()

                return jsonify({
                    'success': True,
                    'movie_id': movie.id
                })
            except BaseException as e:
                print(e)
                abort(422)
        else:
            abort(404)

    
    """
    @TODO:
    Create an endpoint to update details of an actor for the selected id
    """

    @app.route('/actors/update/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actors(jwt, actor_id):
        actor = Actor.query.get(actor_id)

        if actor:
            try:
                body = request.get_json()

                name = body.get('name')
                age = body.get('age')
                gender = body.get('gender')
                movie_id = body.get('movie_id')
                if name:
                    actor.name = name
                if age:
                    actor.age = age
                if gender:
                    actor.gender = gender
                if movie_id:
                    actor.movie_id = movie_id

                actor.update()

                return jsonify({
                    'success': True,
                    'actor_id': actor.id
                })

            except BaseException:
                abort(422)

        else:
            abort(404)

    """
    @TODO:
    Create an endpoint to delete a movie for the selected id
    """
    @app.route('/movies/delete/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)

        if movie:
            try:
                movie.delete()

                return jsonify({
                    'success': True,
                    'deleted': movie_id
                })
            except BaseException:
                abort(422)
        else:
            abort(404)

    """
    @TODO:
    Create an endpoint to delete an actor for the selected id
    """
    @app.route('/actors/delete/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwt, actor_id):
        actor = Actor.query.get(actor_id)

        if actor:
            try:
                actor.delete()

                return jsonify({
                    'success': True,
                    'deleted': actor_id
                })
            except BaseException:
                abort(422)
        else:
            abort(404)


    
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "resource not found"
            }), 404
    
    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            "success": False, 
            "error": 405,
            "message": "method not allowed"
            }), 405
            
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
        }), 422
    
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app

