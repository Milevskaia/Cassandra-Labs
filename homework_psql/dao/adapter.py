from dao.db import PostgresDB


class OwnerHelper:

    def __init__(self):
        self.db = PostgresDB()

    def getCarData(self, car_number=None):

        if car_number:
            car_number = "'{0}'".format(car_number)
        else:
            car_number = 'null'

        query = "select * from table(orm_owner_car.GetCarData({0}))".format(car_number)

        result = self.db.execute(query)
        return result.fetchall()
