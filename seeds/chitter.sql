-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    full_name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    posted_on date,
    peep VARCHAR(255),
    user_name VARCHAR(255),
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (user_name, full_name, email, password) VALUES ('tim.cook', 'Tim Cook', 'tim@apple.com', '12345');
INSERT INTO users (user_name, full_name, email, password) VALUES ('elon.musk', 'Elon Musk', 'elon@spacex.com', '12345');
INSERT INTO users (user_name, full_name, email, password) VALUES ('mickey.mouse', 'Mickey Mouse', 'mickey@email.com', '12345');
INSERT INTO users (user_name, full_name, email, password) VALUES ('test.user', 'Test User', 'test@email.com', '12345');

INSERT INTO peeps (posted_on, peep, user_name, user_id) VALUES ('08/15/2023','Blah blah blah blah blah etc.....', 'tim.cook', 1);
INSERT INTO peeps (posted_on, peep, user_name, user_id) VALUES ('08/16/2023', 'Another blah blah peep etc.....', 'elon.musk', 2);
INSERT INTO peeps (posted_on, peep, user_name, user_id) VALUES ('08/17/2023', 'Peep peep peep peep peep etc.....', 'mickey.mouse', 3);
INSERT INTO peeps (posted_on, peep, user_name, user_id) VALUES ('08/17/2023', 'Cat pics', 'test.user', 4);
INSERT INTO peeps (posted_on, peep, user_name, user_id) VALUES ('08/17/2023', 'Food pics', 'test.user', 4);

