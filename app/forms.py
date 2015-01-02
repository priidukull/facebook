from flask.ext.wtf import Form
from wtforms import PasswordField
from wtforms.validators import DataRequired
from app.models import User


class LoginForm(Form):
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user = User().get(1)
        if not self.password.data == 'liam':
            self.password.errors.append('Invalid password')
            return False
        self.user = user
        return True

