from db.connection import conn
from load_dataset import parse_data_from_file

# populate disciplines

data = parse_data_from_file('/home/mykhailo/PycharmProjects/disciplines/data/test_data.json')

disciplines = list(set([item['discipline'] for item in data]))
cursor = conn.cursor()
for i, discipline in enumerate(disciplines):
    try:
        cursor.execute(
            "INSERT INTO disciplines (id, name) values ({}, '{}');".format(
                i+1, str(discipline)
            )
        )
        conn.commit()
    except Exception as e:
        print(e.args)

# populate questions

for item in data:
    try:
        cursor.execute(
            "INSERT INTO questions (text, discipline_id) values ('{}', {});".format(
                item.get('question').replace("'", ''), int(disciplines.index(item.get('discipline').replace('\n', ''))) + 1
            )
        )
        conn.commit()
    except Exception as e:
        print(e.args)
