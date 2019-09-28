CREATE KEYSPACE IF NOT EXISTS discipline_tests WITH replication = {
	'class': 'SimpleStrategy',
	'replication_factor': '1'
};


CREATE TYPE IF NOT EXISTS discipline_tests.general_info (
 first_name text,
 last_name text,
 age int,
 address text,
 phone_number text,
 city text
);

CREATE TABLE IF NOT EXISTS discipline_tests.users (
 user_id int,
 role text,
 email text,
 generals frozen<general_info>,
 created_at timestamp,
 updated_at timestamp,
 PRIMARY KEY (user_id),
);

CREATE TABLE IF NOT EXISTS discipline_tests.disciplines_with_blocks (
 discipline_id int,
 discipline_name text,
 block_id int,
 block_name text,
 block_description text,
 created_at timestamp,
 updated_at timestamp,
 PRIMARY KEY ((discipline_id), block_id)
);

CREATE TABLE IF NOT EXISTS discipline_tests.test_by_block (
 discipline_id int,
 block_id int,
 block_name text,
 test_id int,
 test_name text,
 test_description text,
 meta map<text,frozen <list<text>>>,
 created_at timestamp,
 updated_at timestamp,
 PRIMARY KEY ((discipline_id, block_id), test_name)
);

CREATE TABLE IF NOT EXISTS discipline_tests.test_stats(
 discipline_id int,
 block_id int,
 test_id int,
 question_counter counter,
 PRIMARY KEY ((discipline_id, block_id), test_id)
);

CREATE TABLE IF NOT EXISTS discipline_tests.question_with_variant_by_test(
 test_id int,
 question_id int,
 question_text text,
 answer_variant_id int,
 answer_variant_text text,
 is_true boolean,
 PRIMARY KEY ((test_id), question_id, answer_variant_id)
);

CREATE TABLE IF NOT EXISTS discipline_tests.test_answers_by_user (
 user_id int,
 test_id int,
 question_id int,
 answer_variant_id int,
 is_test_done boolean STATIC,
 created_at timestamp,
 updated_at timestamp,
 PRIMARY KEY ((user_id, test_id), question_id)
);


