from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, Length, NumberRange

species = ['dog', 'cat', 'porcupine']

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet Name cannot be blank")])
    
    species = SelectField('Species', 
                        choices=[(sp, sp) for sp in species])
    
    photo_url = StringField("Photo URL", validators=[
                        Optional(), URL()])
    
    age = IntegerField("Age", validators=[
                        Optional(), NumberRange(min=0, max=30)])
    
    notes = TextAreaField("Notes", validators=[
                        ptional(), Length(min=10)])



class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    notes = TextAreaField(
        "Notes",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
