from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, BooleanField, TextAreaField, StringField
from wtforms import PasswordField, DecimalField
from wtforms_components import IntegerField
from wtforms.fields.html5 import EmailField, DateTimeLocalField
from wtforms import validators
from .utils import pathologyChoices, userChoices

class PatientForm(FlaskForm):
    pathology = SelectField("Pathologie suspectées", validators = [validators.InputRequired()], id = "pathology", choices = pathologyChoices())
    user = SelectField("Médecin", validators = [validators.InputRequired()], id = "user", choices = userChoices())
    submit = SubmitField("Etape suivante")

class MedicForm(FlaskForm):
    submit = SubmitField("Valider")
