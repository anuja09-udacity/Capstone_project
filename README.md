# Casting Agency Capstone Project
Webpage for the final project can be accessed at 

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


### JWT Tokens for each role:
* Casting Assistant - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZhMjZlYTgyNWVmNGY1ZmFiNjYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1NTc2MTQxLCJleHAiOjE2OTU1ODMzNDEsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.QXN0eDmrN6hj8Pkow1DEqRttggnBAdw1139FKY-Ihyy3OisG8nDYC-JatYjc_qr6qHSq8xBIbdC3qASne59MDIEGx2_tvBsXyxGCR7huYIvU-XBgf6M0TwtJu5sXMBaSWz6f_qnzBUSg44jiMQQUX8zTm7ZYZoqS7-ujXHFVfBU5WnHEq_ndzB-uWegrN8DenOCl1mTA6clsY1D6Ux8Wxvc1seq2tY4OQrMlMyrYQNH_dzT1G8uVHW_MBO7Jf2XYhFrGi_vSY7BX0vtzlZzoVDQUHVdQzBXLXdAfJla0t45_DTkSkcxyMTKIDVoO_Vj4j6ySV2CYqGDnmcH8bcRjsQ```

* Casting Director- ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZkOTcwZDNjZmU3ZWM4MmMxZGEiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1NTc4OTUyLCJleHAiOjE2OTU1ODYxNTIsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.RtdDHjhvNoGRgiwVWYA6x22phvJ0QAWkPlwhKbVf5Qq1XndfPY3IKgxEY5HBweqAYOvx2uW06xF37I8kYn4Enw2ajxnOMuCpuPYjDkAFs68JpjyI55CEHvtPxbZB-pX-z5zoxjiUEnQfU6pR5Ww1MAzsf78-ULTDzKdyFQl5bkWRoiEM6GBb6ZzmTsjd0Xkp3oaocAsMrpI8AA1a-W818WrcZfBUhYibASiK8rGZnqsJQ_lsSqL0YLkbL4tkmJBfBYta3cBPHyxCj7R2wPS1SrIijcRpbs_HekqndtEW5_TRdjXA8e6M0s0CQwblAk78p70yV4pDv1pCnoL4-Kki_Q```

* Executive Producer - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZmMzdmZDQ4YWU0OTEwZTJkOTYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1NTgwNDA2LCJleHAiOjE2OTU1ODc2MDYsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.KXWV9peYPVGgrXUUCkvt-6pkTD5_PqxCZXpgOMQYqoCBJCem356zhAKS-PfImrMncAy-5fi7MWXDGBn9lT9TYUBBSoApTFKOMuIKFxagPpXXEpnttvY-aZhCr8rJZXl0gQbbcluJGaWbaeS9kvelpvTacTPoaheRhp0YnLIQz4I5TeOqsMmaXcNVfHQo3QmUXbioIObUhW0f2qolmTsRbhMNaCwq9FRZMbwnJc9U7g_sbioWGwofDeDjY57hUxUDj_syi6O3tsjrF5wEYts5tR7xanSLajFMpQ0hnqsOfO28rqmJV6kPWsRW-Y9avFsNde7lhvXjT6vetPOvFKx_aw```

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