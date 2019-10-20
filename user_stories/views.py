from django.shortcuts import render
from user_stories.models import User
from django.db import IntegrityError
import requests
from user_stories.helper import save_comments, save_users
# from django.db import transaction


def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    # print(users)
    users_refined = []
    status = 'ok'
    for user in users:
        try:
            new_user = User()
            new_user.name = user['name']
            new_user.email = user['email']
            new_user.username = user['username']
            new_user.email = user['email']
            new_user.address = str(user['address']) # sqlite 3 cannot store json value directly!
            new_user.phone = user['phone']
            new_user.website = user['website']
            # company optional
            new_user.save()
            users_refined.append({'name': user['name'], 'email': user['email']})
        except IntegrityError:
            print("Data is already in the DB cannot add duplicate username and email they are UNIQUE!")
            status = 'existing'
        except Exception as e:
            print("Error " + str(e))
            status = 'error'
    return render(request, 'user_stories/home.html', {
        'status': status,
        'users': users_refined,
    })


def user_comments(request):
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    comments = response.json()
    status = save_comments(comments)
    return render(request, 'user_stories/comments.html', {
        'status': status
    })

