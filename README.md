# Client Management System

This Application is developed with python's web framework DjangoRestFramework. \

### Project Requirements:
- Python 3.8.10
- SQLite

### Steps for setting up the project in local

1. Clone GitHub Repo: [https://github.com/Shreya412/client_management_django.git](https://github.com/Shreya412/client_management_django.git)
2. Create Virtual Env: ` python -m venv venv `
3. Activate venv: `source venv/bin/activate`(Linux) and `venv\Scripts\activate`(Windows)
4. Go Inside Project Folder: `cd client_management_django` and again `cd client_rest`
5. Download dependencies: `pip install -r requirements.txt`
6. Create `.env` file with following keys:
```bash
JWT_SECRET_KEY='asdfghjkl'
```
7. Run project: `python manage.py runserver` 
8. App will start on you local: [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)


### Database Design
![DatabaseDesign](./images/database.jpg)


### Access Level
 - **Admin access:**   can create, edit and delete users
 - **User access:** can create, update, view and delete their client

##
## End Points
### User Authentiation

```
POST    /api/auth/login/
to login
Authentication: Public
Request Data:
{
    Email: EmailStr
    password: str
}
Errors:
403 Invalid Credentials
Response:
{
    access_token: str
}
```

```
POST   /api/auth/register/ 
to create user
Request Data:
{
username: str
email: EmailStr
password: str
}
Authentication: Public Level
Errors: 
400 Email Already in Use
422 Invalid Request data
Response: 201
```

### Clients

```
GET   /api/v1/movie/list/
To get the list of all the movies
Query Params:                                                                                      
limit: int -> to limit the number of return value (default=10)
skip: int -> to skip initial return value (default=0)
search: str -> search movies by name 
Authentication: Public Level
Errors:
400 Bad Request
Response:
[{
    movie_id: int
    name: str 
    director: str
    popularity: float
    imdb_score: float
    genre: str
}]
```
```
GET   /api/v1/movie/{movie_id}/
To get specific movie with Id
Authentication: Public Level
Errors:
400 Bad Request
404 No Movie with request movie_id
Response:
{
    movie_id: int
    name: str 
    director: str
    popularity: float
    imdb_score: float
    genre: str
}
```
```
POST   /api/v1/movie/create/
To create movie
Authentication: Admin Level
Request Data:
{
    name: str
    director: str
    popularity: float
    imdb_score: Optional[float] (default=0)
    genre: str
}
Errors:
400 Movie already exists
401 Not Authorized
422 Invalid request data
Response: 201
```
```
PUT   /api/v1/movie/update/{movie_id}/
To update movie values
Authentication: Admin Level
Request Data:
{
    name: str
    director: str
    popularity: float
    imdb_score: Optional[float] (default=0)
    genre: str
}
Errors:
401 Not Authorized
404 No Movie with request movie_id
Response:
{
    movie_id: int
    name: str 
    director: str
    popularity: float
    imdb_score: float
    genre: str
}
```
```
DELETE   /api/v1/movie/delete/{movie_id}/
To update movie values
Authentication: Admin Level
Errors:
401 Not Authorized
404 No Movie with request movie_id
Response: 204
```

