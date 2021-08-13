from flask import request, flash, redirect, url_for

from app import db
from app.forms import CategoryForm
from app.utils import page_render, get_form_payload


def categories():
    items = db.categories.find({}).sort("name")
    ctx = {
        'title': 'Categories',
        'items': items
    }
    return page_render('categories/list.html', ctx)


def new_category():
    form = CategoryForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        data = get_form_payload(form)
        db.categories.replace_one({"name": data["name"]}, data, upsert=True)
        flash("New Category Added!", 'success')
    else:
        flash("Something went wrong!", 'danger')
    return redirect(url_for('categories'))


def edit_category(id):
    form = CategoryForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        data = get_form_payload(form)
        db.categories.update_one({"_id": id}, {"$set": data})
        flash("Updated Category!", 'success')
    else:
        flash("Something went wrong!", 'danger')
    return redirect(url_for('categories'))


def delete_category(id):
    db.categories.delete_one({"_id": id})
    flash("Category deleted!", 'success')
    return redirect(url_for('categories'))
