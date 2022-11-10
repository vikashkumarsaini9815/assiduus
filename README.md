# assiduus


# Setup project
~~~
git clone https://github.com/vikashkumarsaini9815/assiduus
~~~
# installation
~~~
cd ass_project
pip install -r requairments.txt
~~~~
# Setup DB migration
~~~
create a Users and Message Tables

run commands
python manage.py makemigrations
python manage.py migrate
~~~
# Runserver
~~~
python manage.py runserver
~~~
# Rest api for Message
~~~
http://127.0.0.1:8000/api/messages/

First Time 

Request Body :
  {"username":"Rahul","email":"Rahul123@gmail.com","message":"Hi i am Rhul Kumar "}
  
Second Time 

Request Body :

{"username":"Rahul","email":"Rahul123@gmail.com","message":"Hi i am Rhul Kumar ","Token":"f7188670-5f67-11ed-a640-99a89bd258b7"}


Response Body :
{
    "id": 14,
    "message": "Hi i am Rhul Kumar ",
    "created_at": "2022-11-10T16:49:08.678913Z",
    "updated_at": "2022-11-10T16:49:08.678913Z",
    "created_by": {
        "id": 5,
        "username": "Rahul",
        "email": "Rahul123@gmail.com"
    }
}
~~~
