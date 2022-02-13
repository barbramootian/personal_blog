# from flask_wtf import FlaskForm
# from wtforms import SubmitField,StringField,PasswordField,BooleanField,SelectField,TextAreaField

# from wtforms.validators import input_required,Email,EqualTo
# from ..models import User
# from wtforms import ValidationError

# choices=['love','sport','entertainment','travel']

# class PostForm(FlaskForm):
#     title=StringField("Post Title",validators=[input_required(message='Title required')],render_kw={"placeholder":"Pitch Title"})
#     category=SelectField("Post Category",choices=choices,validate_choice=True)
#     content=StringField("Post body",validators=[input_required(message='body required')],render_kw={"placeholder":"Pitch body"})
#     submit=SubmitField("POST PITCH")

# class CommentForm(FlaskForm):


#      comment=StringField("Pitch comment",validators=[input_required(message='body required')],render_kw={"placeholder":"Pitch comment"}) 
#      submit=SubmitField("Comment")