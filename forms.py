from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, Regexp, EqualTo


class Registration(FlaskForm):
    fname = StringField("First name", validators=[DataRequired(),length(min = 2, max = 30)])
    lname = StringField("Last name", validators=[DataRequired(),length(min = 2, max = 30)])
    username = StringField("Username", validators=[DataRequired(),length(min = 2, max = 30)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
    "Password",
    validators=[
        DataRequired(),
        Regexp(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
        ),
    ],
)
    confirm_password = PasswordField("confirmpassword", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("sign up")

class login(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
    "Password",
    validators=[
        DataRequired()
    ]
)
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")
