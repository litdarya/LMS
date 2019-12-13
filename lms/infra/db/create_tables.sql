CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TYPE degree_t as enum('bachelor', 'master', 'specialist');
CREATE TYPE study_form_t as enum('fulltime', 'extramural', 'evening');
CREATE TYPE education_form_t as enum('budget', 'contract');


CREATE TABLE users (
    user_id serial PRIMARY KEY,
    name VARCHAR (200) NOT NULL,
    -- auth
    hashed_password VARCHAR (200),
    email VARCHAR (100) UNIQUE,
    -- register info
    verification_code UUID DEFAULT uuid_generate_v4(),
    -- info
    telephone VARCHAR (20),
    city VARCHAR (50),
    info TEXT,
    vk_link VARCHAR (100),
    instagram_link VARCHAR (100),
    fb_link VARCHAR (100),
    linkedin_link VARCHAR (100)
);

CREATE table student_group (
    group_name VARCHAR (50) PRIMARY KEY,
    department VARCHAR (50) NOT NULL,
    course_no integer NOT NULL,
    CONSTRAINT valid_course_no CHECK (0 <= course_no and course_no <= 10)
);

CREATE table student(
    user_id integer REFERENCES users (user_id) UNIQUE NOT NULL,
    PRIMARY KEY (user_id),
    group_name VARCHAR (50) REFERENCES student_group (group_name) NOT NULL,
    entry_year     integer,
    CONSTRAINT valid_entry_year CHECK (1900 <= entry_year and entry_year <= 2100),
    degree         degree_t,
    study_form     study_form_t,
    education_form education_form_t
);

CREATE TABLE professors(
     user_id integer REFERENCES users (user_id) UNIQUE NOT NULL,
     PRIMARY KEY (user_id)
);

CREATE TABLE course(
    course_id serial PRIMARY KEY,
    name VARCHAR (50) NOT NULL,
    description TEXT
);

CREATE TABLE course_material (
    course_id integer REFERENCES course (course_id) NOT NULL,
    PRIMARY KEY (course_id),
    name VARCHAR (50) NOT NULL,
    description TEXT,
    add_time DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE course_to_professor (
    course_id integer REFERENCES course (course_id) NOT NULL,
    professor_id integer REFERENCES professors (user_id) NOT NULL,
    PRIMARY KEY (course_id, professor_id)
);

CREATE TABLE course_to_editor (
    course_id integer REFERENCES course (course_id) NOT NULL,
    user_id integer REFERENCES users (user_id),
    PRIMARY KEY (course_id, user_id)
);

CREATE TABLE group_to_course (
    group_name VARCHAR (50) REFERENCES student_group (group_name) NOT NULL,
    course_id integer REFERENCES course (course_id) NOT NULL,
    PRIMARY KEY (group_name, course_id)
);

CREATE TABLE assignee (
    course_id integer REFERENCES course (course_id) NOT NULL,
    start_time DATE NOT NULL,
    end_time DATE NOT NULL,
    desciption TEXT
);
