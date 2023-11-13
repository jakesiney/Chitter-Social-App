# USER STORY:

STRAIGHT UP

As a user
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a user
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a user
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a user
So that I can post messages on Chitter as me
I want to sign up for Chitter

As a user
So that only I can post messages on Chitter as me
I want to log in to Chitter

As a user
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter

As a user
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep
```

```
Nouns:

post, user_name, time, message.
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record | Properties                  |
| ------ | --------------------------- |
| users  | user_name, full_name, email |
| posts  | posted_on, full_name, email |

1. Name of the first table (always plural): `users`

   Column names: `user_name`, `full_name`, 'email'

2. Name of the second table (always plural): `posts`

   Column names: `posted_one`, `full_name`,

```sql

-- Create the table without the foreign key first.
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    full_name VARCHAR(255),
    email VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    posted_on date,
    full_name VARCHAR(255),
    peep VARCHAR(255),
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

```
