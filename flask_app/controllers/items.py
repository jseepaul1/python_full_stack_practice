from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.item import Item


@app.route("/new/item")
def new_item():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    items = Item.get_all()
    return render_template('create_item.html', user=User.get_by_id(data), items=items)


@app.route('/create/wishlist', methods=['POST'])
def create_wishlist():
    print("request form-", request.form)
    data = {
        'user_id': request.form['user_id'],
        'item_id': request.form["item_id"]
    }
    Item.add_to_whishlist(data)
    return redirect(f"/dashboard")


@app.route('/item/<int:id>')
def show_item(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("dashboard.html", item=Item.get_one(data), user=User.get_by_id(user_data))

@app.route('/display/item/<int:id>')
def display_item(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    user_who_liked_same_item = Item.get_users_by_item_id(data)
    return render_template("wish_items.html", item=Item.get_one(data), user=User.get_by_id(user_data), user_who_liked_same_item=user_who_liked_same_item)


@app.route('/destroy/item/<int:id>')
def destroy_item(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    print('destroying....')
    Item.destroy(data)
    return redirect('/dashboard')
