from sqlalchemy import create_engine
from dao.credentials import *
from sqlalchemy.orm import sessionmaker
import psycopg2


class PostgresDB(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            try:
                # connection = psycopg2.connect(username, password, "{0}:{1}/{2}".format(host, port, database_name))
                connection = psycopg2.connect(
                    dbname=database_name,
                    user=username,
                    password=password,
                    host=host,
                    port=port
                )
                cursor = connection.cursor()

                cursor.execute('SELECT version();')
                db_version = cursor.fetchone()

                print("New connection to {} created".format(db_version[0]))

                connection_string = 'postgresql://{username}:{password}@{hostname}:{port}/{database}'

                engine = create_engine(
                    connection_string.format(
                        username=username,
                        password=password,
                        hostname=host,
                        port=port,
                        database=database_name,
                    )
                )

                Session = sessionmaker(bind=engine)
                session = Session()

                PostgresDB._instance.connection = connection
                PostgresDB._instance.cursor = cursor
                PostgresDB._instance.sqlalchemy_session = session
                PostgresDB._instance.sqlalchemy_engine = engine

            except Exception as error:
                print('Error: connection not established {}'.format(error))

        else:
            print('Connection already established')

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor
        self.sqlalchemy_session = self._instance.sqlalchemy_session
        self.sqlalchemy_engine = self._instance.sqlalchemy_engine

    def execute(self, query):
        try:
            result = self.cursor.execute(query)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        self.sqlalchemy_session.close()


if __name__=="__main__":
    db = PostgresDB()