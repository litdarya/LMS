-- groups:
INSERT INTO student_group (group_name, department, course_no)
VALUES ('595', 'DIHT', 5);
INSERT INTO student_group (group_name, department, course_no)
VALUES ('596', 'DIHT', 5);
INSERT INTO student_group (group_name, department, course_no)
VALUES ('597', 'DIHT', 5);
INSERT INTO student_group (group_name, department, course_no)
VALUES ('631', 'DCAM', 4);
INSERT INTO student_group (group_name, department, course_no)
VALUES ('632', 'DCAM', 4);

-- users:
INSERT INTO users (user_id, name)
VALUES (1, 'user1');
INSERT INTO users (user_id, name)
VALUES (2, 'user2');
INSERT INTO users (user_id, name)
VALUES (3, 'user3');
INSERT INTO users (user_id, name)
VALUES (4, 'user4');
INSERT INTO users (user_id, name)
VALUES (5, 'user5');
INSERT INTO users (user_id, name)
VALUES (6, 'professor6');
INSERT INTO users (user_id, name)
VALUES (7, 'professor7');
INSERT INTO users (user_id, name)
VALUES (8, 'professor8');

INSERT INTO professors (user_id)
VALUES (6);
INSERT INTO professors (user_id)
VALUES (7);
INSERT INTO professors (user_id)
VALUES (8);

-- students
INSERT INTO student (user_id, group_name, entry_year, degree)
VALUES (1, '595', 2015, 'bachelor');
INSERT INTO student (user_id, group_name, entry_year, degree)
VALUES (2, '595', 2015, 'bachelor');
INSERT INTO student (user_id, group_name, entry_year, degree)
VALUES (3, '595', 2015, 'bachelor');
INSERT INTO student (user_id, group_name, entry_year, degree)
VALUES (4, '596', 2015, 'bachelor');
INSERT INTO student (user_id, group_name, entry_year, degree)
VALUES (5, '596', 2015, 'bachelor');

-- courses
INSERT INTO course (course_id, name, description)
VALUES (1, 'CV', 'computer vision');
INSERT INTO course (course_id, name, description)
VALUES (2, 'ALGO', 'algorithms');
INSERT INTO course (course_id, name, description)
VALUES (3, 'ARCH', 'software architecture');


-- adding 595, 596 to cv, 595 to ALGO, 596 to ARCH
INSERT INTO group_to_course (group_name, course_id)
VALUES ('595', 1);
INSERT INTO group_to_course (group_name, course_id)
VALUES ('596', 1);
INSERT INTO group_to_course (group_name, course_id)
VALUES ('595', 2);
INSERT INTO group_to_course (group_name, course_id)
VALUES ('596', 3);

-- CV: 6, 7; ALGo: 7, 8; ARCH: 8
INSERT INTO course_to_professor (course_id, professor_id)
VALUES (1, 6);
INSERT INTO course_to_professor (course_id, professor_id)
VALUES (1, 7);
INSERT INTO course_to_professor (course_id, professor_id)
VALUES (2, 7);
INSERT INTO course_to_professor (course_id, professor_id)
VALUES (2, 8);
INSERT INTO course_to_professor (course_id, professor_id)
VALUES (3, 8);