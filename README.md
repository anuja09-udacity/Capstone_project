# Introduction
The Casting Agency API allows users to query the database for movies and actors. There are three different user roles 


# Motivation
As part of Udacity Fullstack Developer Nanodegree Capstone Project which is the final project to combine all of the concepts and the skills taught in the course to build a complete API

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

### Test AUTH locally
* To test the Auth locally, use the access tokens generated against the local host URL 
* Create test cases for each role and endpoint as a Postman Collection
* Map the access token as Bearer token against each role and run the collection


### Render Deployment
* To deploy the app in render, create a database and copy its internal connection URL
* Create a Webservice in render by pointing to the GitHub repo and use the database internal URL as environment variable
* Include pip install -r requirements.txt as a Build command under the Settings tab of Webservice 
* Save AUTH0_DOMAIN, AUTH0_AUDIENCE as environment variables
* Deploy the code and once build is successful, copy the URL created
* Use AUTH0 to get access tokens for each role and use this access token in Postman against the Render deployed app URL to test the application

Bearer Tokens for Render
Casting Assistant
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZhMjZlYTgyNWVmNGY1ZmFiNjYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTg0MzM0LCJleHAiOjE2OTYwNzA3MzQsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.fEcj13re3uksSiBK5vyKjzaR5sLf9fv0HjUE63cQrGtx8COuDk7Q7gKw0PsuSxMlD30VxFPftMZQorKauyx5ZIC3PXToKl3uuswbUKuIjU8pA0CFyT_uIXRwvVBHIZNKieusuRpScilRCgrJfYDmjeyuep6_vOYNXttrUk1lNCySKgA6Map7P7kpPpZA6FwLB0HKorkBK68y1HwZLcTsYEfxz3sM-jO9KFTfJh3iAA6YQV1Dghf7uiO61vOUOOZKblk_em8fPgAfLdu8S_J_yT0lUtaScZfi22AtKD66J9mVtwCdlAsun8FMtMhBmWwjlp35CXyCiMHZ-PXorUWBUg

Casting Director
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZkOTcwZDNjZmU3ZWM4MmMxZGEiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTk0MTY4LCJleHAiOjE2OTYwODA1NjgsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.WSw1mrh-YCjGMXH97GXLyaYbvlxK_CJwLVAWvVztEQQjZD1hxQcgSoHqPTG_EPGdaZcLEkqrO9Q2ngunOZQyMZ32zWJT6L1QOt326y62tTZwkiDqoQP9d68tKwK5we9CHPJVxllkqs5yMPG0d_I7u92q-NPHbxls_GeEPOqqFS4f_Ymo9vxe8TPorn4HnvxOxe6J9FI3YD4k-tg2zdS_B5qHFa-CgvQ5FHsY_PgehmNLc-hQQDxFBLKglr1NOTYXbf39RhNgWHtc9J5SI2lEB1Cv-2ck8Np_KOSYyqnuyKnvCSAZie0mUZDYo4viq4FTghmNbtjPk1szDQHH9BNL-g

Executive producer
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZmMzdmZDQ4YWU0OTEwZTJkOTYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTk0MjY3LCJleHAiOjE2OTYwODA2NjcsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.DC-jr6a3MZPM71m1Vjlkm06BBHiEUV6S1TOVSfNdlH-F9-2I9WWKRcFxayT3y6G2Ji2xxC2Mae8iPubhUXkTdByvHKWZ4y0Ba4GUGSLaTKNDU_OyHG9VLM4TH7Qe_QlvXHXZYqN6fDPSI3ZN-xXWV_SugtkpC7hMOKlROngnZVobaa21l7JydDJBfLC8q_qeeq6v4GC7MrPE9IGzmOi_RXzL5ogQk1iBHjZoM6cYkxbCyoFHwtbrVQx3SOY6Ii6mjleH_xu2mvJo9FDhO3PifLBph_ZWtxEEOl-RAnFi5hs2cA-PmQha-P08lm-NHAL5M4ePNvo006J-THsVDqfuYw
