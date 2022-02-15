from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,BooleanField,SelectField,TextAreaField

from wtforms.validators import input_required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

choices=['love','sport','entertainment','travel','coding']

class PostForm(FlaskForm):
    title=StringField("Post Title",validators=[input_required(message='Title required')],render_kw={"placeholder":"Post Title"})
    category=SelectField("Post Category",choices=choices,validate_choice=True)
    content=StringField("Post body",validators=[input_required(message='Body required')],render_kw={"placeholder":"Post body"})
    submit=SubmitField("POST")  

class CommentForm(FlaskForm):

     comment=StringField("Post comment",validators=[input_required(message='Body required')],render_kw={"placeholder":"Post comment"}) 
     submit=SubmitField("Comment")

class UpdateForm(FlaskForm):                                                                                       
    bio = TextAreaField("Your Biography", validators=[input_required(message='Biography field is required')])
    submit = SubmitField("Update Profile")       