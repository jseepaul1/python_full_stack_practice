from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


class Item:
    def __init__(self, item_data):
        self.id = item_data['id']
        self.item = item_data['item']
        self.created_at = item_data['created_at']
        self.updated_at = item_data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO items (item) VALUES (%(item)s);"
        return connectToMySQL('wish_list').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM items;"

        item_results = connectToMySQL("wish_list").query_db(
            query
        )
        items = []
        for item in item_results:
            items.append(cls(item))
        return items

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM items WHERE id = %(id)s;"
        item_from_db = connectToMySQL('wish_list').query_db(query, data)
        print('result_from_db - ', item_from_db)
        return cls(item_from_db[0])

    @staticmethod
    def validate_item(item):
        is_valid = True
        if len(item['item']) == 0:
            is_valid = False
            flash("No Empty Entries", "item")
        # if len(item['item']) < 3:
        #     is_valid = False
        #     flash("Item must be more 3 characters!", "item")
        return is_valid

    @classmethod
    def get_items_by_user_id(cls, data):
        query = "SELECT * FROM items LEFT JOIN users_and_items ON items.id = users_and_items.item_id LEFT JOIN users ON users.id = users_and_items.user_id WHERE users.id = %(id)s;"
        item_results = connectToMySQL('wish_list').query_db(query, data)
        items = []
        for row in item_results:
            # print('row - ', row)
            print('users_and_items.id - ', row['users_and_items.id'])
            item_data = {
                "id": row['id'],
                "item": row['item'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "wishlist_id": row['users_and_items.id'],
            }
            print('item_data - ', item_data)
            items.append(item_data)
        return items

    @classmethod
    def get_users_by_item_id(cls, data):
        query = "SELECT * FROM items LEFT JOIN users_and_items ON items.id = users_and_items.item_id LEFT JOIN users ON users.id = users_and_items.user_id WHERE items.id = %(id)s;"
        item_results = connectToMySQL('wish_list').query_db(query, data)
        items = []
        for row in item_results:
            # print('row - ', row)
            item_data = {
                "id": row['id'],
                "item": row['item'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_name": row['name']
            }
            items.append(item_data)
        return items

    @classmethod
    def get_other_users_items(cls, data):
        query = """
            SELECT * FROM items
            LEFT JOIN users_and_items ON items.id = users_and_items.item_id
            LEFT JOIN users ON users.id = users_and_items.user_id
            WHERE users.id <> %(id)s
            AND items.id NOT IN
            (
                SELECT items.id FROM items
                LEFT JOIN users_and_items ON items.id = users_and_items.item_id
                LEFT JOIN users ON users.id = users_and_items.user_id
                WHERE users.id = %(id)s
            );
        """
        item_results = connectToMySQL('wish_list').query_db(query, data)
        items = []
        for row in item_results:
            print('row - ', row)
            item_data = {
                "id": row['id'],
                "item": row['item'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_name": row['name'],
            }
            items.append(item_data)
        return items

    @classmethod
    def add_to_whishlist(cls, data):
        query = "INSERT INTO users_and_items (user_id, item_id) VALUES (%(user_id)s, %(item_id)s);"
        wishlist_result = connectToMySQL('wish_list').query_db(query, data)
        print('wishlist_result - ', wishlist_result)
        return wishlist_result

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users_and_items WHERE id = %(id)s;"
        print('deletubg ddi = ', data)
        return connectToMySQL('wish_list').query_db(query, data)
