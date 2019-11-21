CREATE TABLE student_group(
   group_id serial PRIMARY KEY,
   name VARCHAR (50) UNIQUE NOT NULL,
   department VARCHAR (50) NOT NULL,
   course_num NUMERIC NOT NULL
);

-- add to table

INSERT INTO student_group (name, department, course_num)
VALUES ('CV', 'DIHT', 5);

-- select example
SELECT *
FROM student_group
WHERE user = ? AND item = ?
LIMIT 5;

-- example
SELECT name,department, course_num  FROM student_group;