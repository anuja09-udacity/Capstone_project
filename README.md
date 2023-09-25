# Casting Agency Capstone Project
Webpage for the final project can be accessed at https://castingagency-project.onrender.com

##### Project Dependencies
* __Flask__ - Slim python web library.
* __SQLAlchemy__ - Python ORM library
* __Render__ - Platform for easy hosting of web apps
* __Postman__ - API testing tool

### Installation instructions
* Clone project to directory of your choice.
* Create a virtualenv in project directory
* run ```pip install -r requirements.txt``` to install project dependencies
* create a setup.sh bash file and add export statements for Auth0 Domain and Audience
* run ```export FLASK_APP=app.py```
* type ```flask run``` in terminal

###Endpoints:
* GET /actors and /movies
* DELETE /actors/ and /movies/
* POST /actors and /movies and
* PATCH /actors/ and /movies/

### Roles
* Casting Assistant
    * GET /actors and /movies

* Casting Director
    * GET /actors and /movies
    * ADD /actors/add and DELETE /actors/delete
    * PATCH /actors/update and /movies/update
    
* Executive Producer
    * GET /actors and /movies
    * ADD /actors/add and DELETE /actors/add
    * PATCH /actors/update and /movies/update
    * ADD /movies/delete and DELETE /movies/delete



## API Endpoints

In the next few subsections, we'll cover how the API works and what you can expect back in the results.


### GET Endpoints

#### GET /movies
Displays all movies listed in the database.

Sample response:
```
{
    "movies": [
        {
            "id": 1,
            "release_year": 2008,
            "title": "Healer"
        },
        {
            "id": 2,
            "release_year": 2019,
            "title": "Extraordinary You"
        },
    ],
    "success": true
}
```

#### GET /actors
Displays all actors / actresses listed in the database.

Sample response:
```
{
    "actors": [
        {
            "age": 28,
            "gender": "female",
            "id": 1,
            "movie_id": 2,
            "name": "Dan Oh"
        },
        {
            "age": 34,
            "gender": "male",
            "id": 2,
            "movie_id": 1,
            "name": "Gong Yoo"
        },
    ],
    "success": true
}
```

### POST Endpoints

#### POST /movies/add
Creates a new movie entry in the database.

Sample response:
```
{
    "movie_id": 8,
    "success": true
}
```

#### POST /actors/add
Creates a new actor / actress entry in the database.

Sample response:
```
{
    "actor_id": 7,
    "success": true
}
```

### PATCH Endpoints

#### PATCH /movies/update/<movie_id>
Updates movie information given a movie_id and newly updated attribute info.

Sample response:
```
{
    "movie_id": 2,
    "success": true
}
```

#### PATCH /actors/update/<actor_id>
Updates actor information given a actor_id and newly updated attribute info.

Sample response:
```
{
    "actor_id": 2,
    "success": true
}
```

### DELETE Endpoints

#### DELETE /movies/delete/<movie_id>
Deletes a movie entry from the database given the inputted movie_id.

Sample response:
```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /actors/delete/<actor_id>
Deletes an actor / actress entry from the database given the inputted actor_id.

Sample response:
```
{
    "deleted": 1,
    "success": true
}
```