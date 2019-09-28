from cassandra.cluster import Cluster
from cassandra.query import BatchStatement

connection = Cluster().connect('discipline_tests')

list_of_batch_statement = [
    '''
    UPDATE discipline_tests.users
    SET role = 'ADMIN'
    WHERE user_id = 2;
    ''',
    '''
    UPDATE discipline_tests.test_answers_by_user
    SET is_test_done = true
    WHERE user_id = 2 AND test_id = 1;
    '''
]


def batch_execute(statement_list):
    print('Start exec batch statement')
    batch = BatchStatement()
    for query in statement_list:
        batch.add(query)
    connection.execute(batch)
    print('End of exec batch statement')




