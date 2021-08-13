from flask import request, flash, redirect, url_for

from app import db
from app.forms import ProductForm
from app.utils import page_render, get_form_payload, serialize_data


def products():
    items = db.products.aggregate([
        {
            '$lookup': {
                'from': 'categories',
                'localField': 'category_id',
                'foreignField': '_id',
                'as': 'category'
            }
        }
    ])
    categories = db.categories.find({}).sort("name")

    ctx = {
        'title': 'Products',
        'categories': serialize_data(categories),
        'items': items
    }
    return page_render('products/list.html', ctx)


def new_product():
    form = ProductForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        data = get_form_payload(form)
        db.products.insert_one(data)
        flash("New Product Added!", 'success')
    else:
        flash("Something went wrong!", 'danger')
    return redirect(url_for('products'))


def edit_product(id):
    form = ProductForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        data = get_form_payload(form)
        db.products.update_one({"_id": id}, {"$set": data})
        flash("Updated Product!", 'success')
    else:
        flash("Something went wrong!", 'danger')
    return redirect(url_for('products'))


def delete_product(id):
    db.products.delete_one({"_id": id})
    flash("Product deleted!", 'success')
    return redirect(url_for('products'))
