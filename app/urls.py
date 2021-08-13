from app import app

from app.views.categories import categories, new_category, edit_category, delete_category
from app.views.products import products, new_product, edit_product, delete_product

# Categories
app.add_url_rule('/categories', view_func=categories)
app.add_url_rule('/categories/new', view_func=new_category, methods=['POST'])
app.add_url_rule('/categories/edit/<ObjectId:id>', view_func=edit_category, methods=['POST'])
app.add_url_rule('/categories/delete/<ObjectId:id>', view_func=delete_category, methods=['POST'])

# Products
app.add_url_rule('/products', view_func=products)
app.add_url_rule('/products/new', view_func=new_product, methods=['POST'])
app.add_url_rule('/products/edit/<ObjectId:id>', view_func=edit_product, methods=['POST'])
app.add_url_rule('/products/delete/<ObjectId:id>', view_func=delete_product, methods=['POST'])
