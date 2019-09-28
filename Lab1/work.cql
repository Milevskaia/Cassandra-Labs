INSERT INTO discipline_tests.users (user_id, role, email, generals,created_at, updated_at)
VALUES (1, 'STANDART' , 'ss@gmail.com', {"first_name":'Sam',"last_name": 'Smith',"age":33,"address":'USA,CA',"phone_number":'076397722',"city": 'Los Angeles'}, dateof(now()), dateof(now()));
INSERT INTO discipline_tests.users (user_id, role, email, generals,created_at, updated_at )
VALUES (2, 'STANDART' , 'rose@gmail.com', {"first_name":'Rosie',"last_name": 'Whitley',"age":35,"address":'USA,TX',"phone_number":'039848992',"city": 'Austin'}, dateof(now()), dateof(now()));
INSERT INTO discipline_tests.users (user_id, role, email, generals,created_at, updated_at )
VALUES (3, 'ADMIN' , 'polly@gmail.com', {"first_name":'Pole',"last_name": 'Aaron',"age":26,"address":'USA,VA',"phone_number":'085756637',"city": 'Virginia'}, dateof(now()), dateof(now()));

SELECT * FROM discipline_tests.users;


INSERT INTO discipline_tests.disciplines_with_blocks (discipline_id, discipline_name, block_id, block_name, block_description, created_at, updated_at)
VALUES (1, 'History', 1, 'WW1', 'Block about First World War', dateof(now()), dateof(now()));
INSERT INTO discipline_tests.disciplines_with_blocks (discipline_id, discipline_name, block_id, block_name, block_description, created_at, updated_at)
VALUES (1, 'History', 2, 'WW2', 'Block about Second World War', dateof(now()), dateof(now()));
INSERT INTO discipline_tests.disciplines_with_blocks (discipline_id, discipline_name, block_id, block_name, block_description,created_at, updated_at)
VALUES (1, 'History', 3, 'GCW', 'Block about German Civil War', dateof(now()), dateof(now()));

SELECT * FROM discipline_tests.disciplines_with_blocks;


INSERT INTO discipline_tests.test_by_block ( discipline_id, block_id, block_name, test_id, test_name, test_description, meta, created_at, updated_at)
VALUES (1, 1, 'WW1', 1, 'WW1', 'Test contains questions about First World War', {'tags': ['#war', '#world', '#first'], 'keywords': ['War', 'First World War']}, dateof(now()), dateof(now()));
INSERT INTO discipline_tests.test_by_block ( discipline_id, block_id, block_name, test_id, test_name, test_description, meta, created_at, updated_at)
VALUES (1, 2, 'WW2', 1, 'WW2', 'Test contains questions about Second World War', {'tags': ['#war', '#world', '#second'], 'keywords': ['War', 'Second World War']}, dateof(now()), dateof(now()));
INSERT INTO discipline_tests.test_by_block ( discipline_id, block_id, block_name, test_id, test_name, test_description, meta, created_at, updated_at)
VALUES (1, 3, 'GCW', 1, 'GCW', 'Test contains questions about German Civil War', {'tags': ['#war', '#civil', '#germany'], 'keywords': ['War', 'Civil War', 'Germany']}, dateof(now()), dateof(now()));

SELECT * FROM discipline_tests.test_by_block;


INSERT INTO discipline_tests.question_with_variant_by_test (test_id, question_id, question_text, answer_variant_id, answer_variant_text, is_true)
VALUES (1, 1, 'When was First World War?', 1, '1914-1918', true);
INSERT INTO discipline_tests.question_with_variant_by_test (test_id, question_id, question_text, answer_variant_id, answer_variant_text, is_true)
VALUES (1, 1, 'When was First World War?', 2, '1912-1917', false);
INSERT INTO discipline_tests.question_with_variant_by_test (test_id, question_id, question_text, answer_variant_id, answer_variant_text, is_true)
VALUES (1, 1, 'When was First World War?', 3, '1917-1920', false);

SELECT * FROM discipline_tests.question_with_variant_by_test;


INSERT INTO discipline_tests.test_answers_by_user (user_id, test_id, question_id, answer_variant_id, is_test_done, created_at, updated_at)
VALUES(2, 1, 1, 2, false, dateof(now()), dateof(now()) );

SELECT * FROM discipline_tests.test_answers_by_user;


UPDATE discipline_tests.users
SET
	generals ={
 				 first_name:'Leon',
				 last_name:'King',
				 age:42,
				 address:'USA,NY',
				 phone_number:'064738292',
				 city:'New Jercy'
				},
	email = 'leo@gmail.com'
WHERE user_id = 1 IF EXISTS;

SELECT * FROM discipline_tests.users;


UPDATE discipline_tests.users
SET role = 'ADMIN'
WHERE user_id = 2 IF EXISTS;

SELECT * FROM discipline_tests.users;


UPDATE discipline_tests.test_answers_by_user
SET is_test_done = true
WHERE user_id = 2 AND test_id = 1;

SELECT * FROM discipline_tests.test_answers_by_user;

SELECT user_id, role, email, generals
FROM discipline_tests.users;


SELECT discipline_id, discipline_name, block_id,  block_name, block_description
FROM discipline_tests.disciplines_with_blocks
WHERE discipline_id = 1;


SELECT  discipline_id, block_id, block_name, test_id, test_name, test_description, meta
FROM discipline_tests.test_by_block;


SELECT test_id, question_id, question_text, answer_variant_id, answer_variant_text, is_true
FROM discipline_tests.question_with_variant_by_test
WHERE test_id = 1;


SELECT user_id, test_id, question_id, answer_variant_id, is_test_done
FROM discipline_tests.test_answers_by_user
WHERE user_id = 3 and test_id = 1 and question_id = 1;

DELETE email
FROM discipline_tests.users
WHERE user_id = 3;

SELECT * FROM discipline_tests.users;

DELETE block_description
FROM discipline_tests.disciplines_with_blocks
WHERE discipline_id = 1 AND block_id = 2;

SELECT * FROM discipline_tests.disciplines_with_blocks;


DELETE is_true
FROM question_with_variant_by_test
WHERE test_id = 1 AND question_id =1 AND answer_variant_id = 3;

SELECT * FROM  question_with_variant_by_test;