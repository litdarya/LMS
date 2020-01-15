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
INSERT INTO users (user_id, name, verification_code)
VALUES (1, 'user1', '47d0e78d-2236-48ec-95db-dc50321fe3cc');
INSERT INTO users (user_id, name, verification_code)
VALUES (2, 'user2', '805b6558-1a5c-479c-8e28-344952c99f6a');
INSERT INTO users (user_id, name, verification_code)
VALUES (3, 'user3', '8e3adc33-7ba9-4035-943f-dbac996c4c42');
INSERT INTO users (user_id, name, verification_code)
VALUES (4, 'user4', 'a779fc73-eb48-4e2b-822b-4067eacc4151');
INSERT INTO users (user_id, name, verification_code)
VALUES (5, 'user5', '0788948b-2f48-4ea4-8611-426af37de7e6');
INSERT INTO users (user_id, name, verification_code)
VALUES (6, 'professor6', 'db91e29a-b6b6-489b-9ed6-e215b602d0d5');
INSERT INTO users (user_id, name, verification_code)
VALUES (7, 'professor7', 'd3a9f835-6767-4bf2-b535-198c9ab56194');
INSERT INTO users (user_id, name, verification_code)
VALUES (8, 'professor8', 'f5e8ffe5-65f1-445a-9aba-9856c04a6fed');

INSERT INTO professors (user_id)
VALUES (6);
INSERT INTO professors (user_id)
VALUES (7);
INSERT INTO professors (user_id)
VALUES (8);

-- students
INSERT INTO student (user_id, group_name, entry_year, degree, education_form)
VALUES (1, '595', 2015, 'bachelor', 'budget');
INSERT INTO student (user_id, group_name, entry_year, degree, education_form)
VALUES (2, '595', 2015, 'bachelor', 'budget');
INSERT INTO student (user_id, group_name, entry_year, degree, education_form)
VALUES (3, '595', 2015, 'bachelor', 'contract');
INSERT INTO student (user_id, group_name, entry_year, degree, education_form)
VALUES (4, '596', 2015, 'bachelor', 'budget');
INSERT INTO student (user_id, group_name, entry_year, degree, education_form)
VALUES (5, '596', 2015, 'bachelor', 'budget');

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