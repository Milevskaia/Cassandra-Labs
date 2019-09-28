from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from batch import batch_execute, list_of_batch_statement


connection = Cluster().connect('discipline_tests')


def execute_file(filename, consistency_level, split_char=';'):
    print('Start exec {}'.format(filename))
    with open(filename, 'r') as file:
        data = file.read()
        for query in data.split(split_char):
            query = query.strip()
            if query:
                statement = SimpleStatement(
                    query,
                    consistency_level=consistency_level,
                )
                connection.execute(statement)
    print('End of exec {}'.format(filename))


def main():
    execute_file('drop.cql', ConsistencyLevel.QUORUM)
    execute_file('create.cql', ConsistencyLevel.ALL)
    execute_file('work.cql', ConsistencyLevel.ONE)
    batch_execute(list_of_batch_statement)


if __name__ == '__main__':
    main()
