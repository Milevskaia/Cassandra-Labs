CREATE TABLE user_tbl(
	user_id 		INT 			PRIMARY KEY NOT NULL,
	user_role 		TEXT 			DEFAULT 'STANDART' NOT NULL,
	user_name 		TEXT 			NOT NULL,
	user_age 		SERIAL,
	user_email 	 	VARCHAR(20) 	NOT NULL UNIQUE,
	phone_number 	VARCHAR(20)		NOT NULL UNIQUE,
	user_address 	VARCHAR(50),
	CHECK (user_role in ('STANDART', 'ADMIN'))
);


CREATE TABLE discipline(
	discipline_id 		INT 	PRIMARY KEY NOt NULL,
	discipline_name 	TEXT 	NOT NULL
);


CREATE TABLE block(
	block_id 		INT 	PRIMARY KEY NOT NULL,
	block_name 		TEXT 	NOT NULL,
	block_disc_fk 	INT 	REFERENCES discipline(discipline_id)
);


CREATE TABLE test(
	test_variant 	INT 	PRIMARY KEY NOT NULL,
	test_name 		TEXT 	NOT NULL,
	test_block_fk 	INT 	REFERENCES block(block_id)
);


CREATE TABLE question(
	question_id 		INT 	PRIMARY KEY NOT NULL,
	question_text 		TEXT 	NOT NULL,
	question_test_fk 	INT 	REFERENCES test(test_variant)
);


CREATE TABLE answer_variant(
	answer_var_id 		INT 		PRIMARY KEY NOT NULL,
	answer_text 		TEXT 		NOT NULL,
	answer_check		BOOLEAN 	NOT NULL,
	answer_quest_fk 	INT 		REFERENCES question(question_id)
);


CREATE TABLE user_answer(
	user_answer_id 	INT 	PRIMARY KEY NOT NULL,
	user_id_fk 		INT 	REFERENCES user_tbl(user_id),
	answ_var_id_fk 	INT 	REFERENCES answer_variant(answer_var_id)
);





























