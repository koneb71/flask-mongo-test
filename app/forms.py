from bson import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, fields, widgets
from wtforms.validators import DataRequired


class ObjectIdField(fields.Field):
    widget = widgets.TextInput()

    def process_formdata(self, valuelist):
        fields.Field.process_formdata(self, valuelist)
        if valuelist and len(valuelist[0]) == 24:
            try:
                self.data = ObjectId(valuelist[0])
            except:
                self.data = None
        else:
            self.data = None


class CategoryForm(FlaskForm):
    name = StringField('Category', validators=[DataRequired()])


class ProductForm(FlaskForm):
    category_id = ObjectIdField('Category', validators=[DataRequired()])
    name = StringField('Category', validators=[DataRequired()])
    price = FloatField('Category', validators=[DataRequired()])
