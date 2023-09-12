from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SigilForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Generate Sigil')