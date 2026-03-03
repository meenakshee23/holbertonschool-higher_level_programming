learning SQL Better

 *SQL stand for Structured Query Language*

What is a relational database?
a table containing only one object representation

*DDL stand for Data Definition Language*

*DML stand for Data Manipulation Language*



## SQL Definition:
~ SQL (Structured Query Language) is the standardized, domain-specific programming language used to interact with and manage relational database management systems (RDBMS)



 ## What I learned:

 - Creating a database: I learned how to use `CREATE DATABASE IF NOT EXISTS` to safely create a new database without causing errors if it already exists

-  Deleting a database: I can remove a database using `DROP DATABASE IF EXISTS` without worrying about errors if the database is not there

- Listing tables: Using `SHOW TABLES`, I can see all the tables in a selected database

- Creating a table: I learned how to define a table and its columns with `CREATE TABLE IF NOT EXISTS`, ensuring it doesn’t fail if the table already exists

- Showing table structure: `SHOW CREATE TABLE` lets me view the full SQL used to create a table, which is helpful for understanding its structure

- Listing all rows: `With SELECT * FROM table_name`, I can display all the data stored in a table

- Inserting data: Using `INSERT INTO table_name (...) VALUES (...)`, I can add new rows to a table

- Counting rows: I can count rows that meet specific conditions using `SELECT COUNT(*) FROM table_name WHERE ....`


to be continued...