"""Forms for web ui."""

from flask import request, session
from flask_wtf import FlaskForm
from wtforms import (BooleanField, FormField, HiddenField, IntegerField,
                     PasswordField, RadioField, SelectField,
                     SelectMultipleField, StringField, SubmitField,
                     TextAreaField, validators)

# from schematics.models import FieldDescriptor


def make_form(model):
    """Make a form from a model, dynamically."""

    class CustomForm(FlaskForm):
        pass

    for k, v in vars(model).items():
        print(v)
        # if isinstance(v, FieldDescriptor):
        #     print(dir(v))
        # print(v._type)

    setattr(CustomForm, 'submit', SubmitField('Search'))
    return CustomForm
