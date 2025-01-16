from oauth_login import LoginInfo
from pymongo import MongoClient
from flask import Flask, session
import os

class UserManagement:
    def __init__(self, flask_obj: Flask, app_config: dict):
        self.mongo = MongoClient(host=os.environ['MONGO_SERVER_ADDR'], port=int(os.environ['MONGO_SERVER_PORT']))
        self.db_name = "sh33p-blog"
        self.user_data_collection = "user-data"

        # permanent session configuration
        self.set_session_permanent = app_config['permanent_session']
        if self.set_session_permanent:
            from datetime import timedelta
            flask_obj.permanent_session_lifetime = \
                timedelta(seconds= app_config['permanent_session_duration'])

    def __uid_from_email(email: str) -> str:
        from hashlib import sha256
        return sha256(email.encode()).digest().hex()

    def is_logged_in(self):
        uid = session.get('uid')
        return uid is not None
    
    def get_user_data(self):
        uid = session.get('uid')
        if uid is None:
            return None
        
        users = self.mongo[self.db_name][self.user_data_collection]
        user = users.find_one({'uid': uid})

        return {
            'name': user['first_name'],
            'surname': user['last_name'],
            'email': user['email'],
            'picture': user['picture']
        }

    def login(self, login_data: LoginInfo):
        self.__register_user(login_data)

        uid = UserManagement.__uid_from_email(login_data.email)
        users = self.mongo[self.db_name][self.user_data_collection]
        user = users.find_one({'uid': uid})
        if user['logged_in']:
            self.logout()

        session['uid'] = uid
        session.permanent = self.set_session_permanent
        users.update_one({'uid': uid}, {'$set' : {'logged_in': True}})

    def logout(self):
        uid = session.get('uid')
        if uid is None:
            return

        users = self.mongo[self.db_name][self.user_data_collection]
        user = users.find_one({'uid': uid})
        if not user['logged_in']:
            return
        
        session.pop('uid')
        session.permanent = False
        users.update_one({'uid': uid}, {'$set' : {'logged_in': False}})

    def __register_user(self, login_data: LoginInfo) -> bool:
        users = self.mongo[self.db_name][self.user_data_collection]

        uid = UserManagement.__uid_from_email(login_data.email)
        if users.find_one({'uid': uid}) is not None:
            return False
        
        new_user = {
            'uid': uid,
            'logged_in': False,
            'email': login_data.email,
            'name': login_data.name,
            'first_name': login_data.first_name,
            'last_name': login_data.last_name,
            'picture': login_data.picture,
        }

        users.insert_one(new_user)
        return True