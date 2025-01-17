from oauth_login import LoginInfo
from pymongo import MongoClient
from flask import Flask, session
import os

class UserData:
    def __init__(self, db_entry: dict):
        self.uid = db_entry.get('uid')
        self.name = db_entry.get('first_name')
        self.surname = db_entry.get('last_name')
        self.email = db_entry.get('email')
        self.picture = db_entry.get('picture')
        self.personal_page = db_entry.get('personal_page')

        # blog author data
        self.author_id = db_entry.get('author_id')

    def new_user(uid, name, surname, email, picture):
        return {
            'uid': uid,
            'first_name': name,
            'last_name': surname,
            'email': email,
            'picture': picture
        }

class UserDataUpdateBuilder:
    def __init__(self):
        self.updates = {}

    def to_update_command(self) -> dict:
        return {"$set" : self.updates}

    def update_name(self, new_name: str):
        self.updates['first_name'] = new_name
    
    def update_surname(self, new_surname: str):
        self.updates['last_name'] = new_surname

    def update_email(self, new_email: str):
        self.updates['email'] = new_email
    
    def update_picture(self, new_picture_path: str):
        self.updates['picture'] = new_picture_path

    def update_personal_page(self, new_personal_page: str | None):
        self.updates['personal_page'] = new_personal_page

    def update_author_id(self, new_author_id: str | None):
        self.updates['author_id'] = new_author_id

class UserManagement:
    def __init__(self):
        self.mongo = MongoClient(host=os.environ['MONGO_SERVER_ADDR'], port=int(os.environ['MONGO_SERVER_PORT']))
        self.db_name = "sh33p-blog"
        self.user_data_collection = "user-data"
    
    def setup(self, flask_obj: Flask, app_config: dict):
        # permanent session configuration
        self.set_session_permanent = app_config['permanent_session']
        if self.set_session_permanent:
            from datetime import timedelta
            flask_obj.permanent_session_lifetime = \
                timedelta(seconds= app_config['permanent_session_duration'])

    def __uid_from_email(email: str) -> str:
        from hashlib import sha256
        return sha256(email.encode()).digest().hex()
    
    def __user_from_db(self, uid: str) -> dict:
        users = self.mongo[self.db_name][self.user_data_collection]
        return users.find_one({'uid': uid})

    def is_logged_in(self) -> bool:
        uid = session.get('uid')
        return uid is not None
    
    def get_user_data(self) -> UserData | None:
        uid = session.get('uid')
        if uid is None:
            return None
        
        users = self.mongo[self.db_name][self.user_data_collection]
        user = users.find_one({'uid': uid})

        return UserData(user)

    def login(self, login_data: LoginInfo):
        self.__register_user(login_data)

        if self.is_logged_in():
            self.logout()

        uid = UserManagement.__uid_from_email(login_data.email)

        session['uid'] = uid
        session.permanent = self.set_session_permanent

    def logout(self):
        if not self.is_logged_in():
            return
        
        session.pop('uid')
        session.permanent = False

    def __register_user(self, login_data: LoginInfo) -> bool:
        uid = UserManagement.__uid_from_email(login_data.email)
        if self.__user_from_db(uid) is not None:
            return False
        
        new_user = UserData.new_user(
            uid,
            login_data.first_name,
            login_data.last_name,
            login_data.email,
            login_data.picture
        )

        users = self.mongo[self.db_name][self.user_data_collection]
        users.insert_one(new_user)
        return True
    
    def update_user(self, uid: str, update_data: UserDataUpdateBuilder):
        users = self.mongo[self.db_name][self.user_data_collection]
        users.update_one({'uid': uid}, update_data.to_update_command())
        