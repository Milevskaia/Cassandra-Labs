from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators

from dao.db import PostgresDB
from dao.orm.model import ormTest, ormQuestion

db = PostgresDB()


def test_choices():
    return db.session.query(ormTest).all()


def test_question_choices():
    return db.session.query(ormQuestion).all()


class TestForm(FlaskForm):
    test_name = StringField("Name: ", [validators.DataRequired(), validators.Length(max=63)])
    test_variant = IntegerField('Variant: ')
    submit = SubmitField("Save")


class QuestionForm(FlaskForm):
    question_text = StringField("Name: ", [validators.DataRequired(), validators.Length(max=63)])
    test_id = IntegerField()
    submit = SubmitField("Save")


class QuestionVariantForm(FlaskForm):
    answer_variant_text = StringField("Name: ", [validators.DataRequired(), validators.Length(max=511)])
    question_id = IntegerField()
