from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.adapter import OwnerHelper


class SearchForm(Form):

    car_number = StringField('Car number: ')
    submit = SubmitField('Search')

    def get_result(self):
        helper = OwnerHelper()
        return helper.getCarData(self.car_number.data)


if __name__ == "__main__":
    helper = OwnerHelper()
    print(helper.getCarData('123ABC'))
