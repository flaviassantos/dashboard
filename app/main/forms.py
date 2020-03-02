from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FloatField, DateField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me',
                             validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class ProjectForm(FlaskForm):
    submit = SubmitField('Save Project')
    date = DateField('Date when work was completed (format: YYYY/MM/DD)', format='%Y/%m/%d', validators=[DataRequired()])
    client = StringField('Client', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    platform = StringField('Choose platform from: SJ, Lua, Private or Other', validators=[DataRequired()])
    income = FloatField('Income (Kr-)', validators=[DataRequired()])
    cost = FloatField('Cost (Kr-)', validators=[DataRequired()])
    comment = TextAreaField('Comment',
                            validators=[Length(min=0, max=140)])
    submit = SubmitField('Save Project')


class SearchForm(FlaskForm):
    q = StringField('Search', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)