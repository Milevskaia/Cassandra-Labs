import psycopg2

conn = psycopg2.connect(
    host="localhost", port="5432", database="disciplines_db", user="disciplines_user", password="qwerty123"
)

cursor = conn.cursor()

# cursor.execute(
#     'SHOW server_version;'
# )
#
# print(cursor.fetchall())