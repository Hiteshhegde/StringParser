


from flask_wtf import FLaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


#Create your forms here
#String Parsing request form 
class StringParseForm(FlaskForm):
  info = StringField('String to be parsed', validators=[Length(min=5, max=1000)])
  submit = SubmitField('Parse')
