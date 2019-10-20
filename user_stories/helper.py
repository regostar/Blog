from user_stories.models import User, Comment
from django.db import IntegrityError

def save_users(users):
    print(users)



def save_comments(comments):
    status = 'ok'
    try:
        for comment in comments:
            new_comment = Comment()
            new_comment.name = comment['name']
            new_comment.email = comment['email']
            new_comment.id = comment['id']
            new_comment.postId = comment['postId']
            new_comment.body = comment['body']
            new_comment.save()
    except IntegrityError:
        print("Data is already in the DB cannot add duplicate username and email they are UNIQUE!")
        status = 'existing'
    except Exception as e:
        print("Error " + str(e))
        status = 'error'
    finally:
        return status

