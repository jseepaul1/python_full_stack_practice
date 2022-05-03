from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class User:
    def __init__(self, user_data):
        self.id = user_data['id']
        self.name = user_data['name']
        self.username = user_data['username']
        self.password = user_data['password']
        self.created_at = user_data['created_at']
        self.updated_at = user_data['updated_at']
        self.users_and_wishes = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

        user_results = connectToMySQL("wish_list").query_db(
            query
        )
        users = []
        for user in user_results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (name, username, password) VALUES (%(name)s,%(username)s, %(password)s);"
        return connectToMySQL("wish_list").query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        print('data - ', data)
        query = "SELECT * FROM users WHERE id = %(id)s"
        result_from_db = connectToMySQL("wish_list").query_db(query, data)
        print('result_from_db - ', result_from_db)
        return cls(result_from_db[0])

    @classmethod
    def get_by_username(cls, data):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        results = connectToMySQL("wish_list").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        results = connectToMySQL("wish_list").query_db(query, user)
        # print('user -', user)
        is_valid = True
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters!", "registration")
            is_valid = False
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters!", "registration")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters to register!",
                "registration")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Sorry password does not match!", "registration")
            is_valid = False
        return is_valid
