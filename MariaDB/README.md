# MariaDB Reference Notes (MySql)

## About MySql
MySQL is a Swedish company. The name of the parent company that created this DB is MySQL AB. The first version of the software was launched in May 1995. Currently, MySQL is managed by Oracle.

## About MariaDB
MariaDB is forked out of MySQL. So, there are lot of similarities between these two databases. 

## Common Data Types
|Data Type| Description|
|----------|---------|
|char (Character) |Fixed width string value. Values of this type is enclosed in single quotes. For ex. Anu’s will be written as ‘Anu’ ‘s’.|
|varchar |Variable width character string. This is similar to char except the size of the data entry vary considerably.|
|dec (Decimal)|It represents a fractional number such as 15.12, 0.123 etc. Here the size argument consist of two parts : precision and scale. The precision indicates how many digits the number may have and the scale indicates the maximum number of digits to the right of the decimal point. The size (5, 2) indicates precision as 5 and scale as 2. The scale cannot exceed the precision.
|numeric|It is same as decimal except that the maximum number of digits may not exceed the precision argument.|
|int (Integer)|It represents a number without a decimal point. Here the size argument is not used.
|smallint |It is same as integer but the default size may be smaller than Integer.
|float|It represents a floating point number in base 10 exponential notation and may define a precision up to a maximum of 64.
|real |It is same as float, except the size argument is not used and may define aprecision up to a maximum of 64.|
|double|Same as real except the precision may exceed 64.|
|DATE| It is used to specify date format YYYY-MM-DD. Its supported range is from '1000-01-01' to '9999-12-31'.|

## About SQL Commands
**Five types of SQL queries:**
1) Data Definition Language (DDL)
2) Data Manipulation Language (DML)
3) Data Control Language(DCL)
4) Transaction Control Language(TCL)
5) Data Query Language (DQL)

**DDL commands:**
`CREATE`, `DROP`, `ALTER`, `TRUNCATE`, `RENAME`

**DQL command:**
`SELECT`

**DML commands:**
`INSERT`, `UPDATE`, `DELETE`

**DCL commands:**
`GRANT`, `REVOKE`

**TCL commands:**
`COMMIT`, `ROLLBACK`, `SAVEPOINT`, `SET TRANSACTION`

## Basic SQL Commands

#### CREATE
`CREATE` is as keyword to create database and table
```sql
MariaDB [(none)]> CREATE DATABASE dbms_sample;
Query OK, 1 row affected (0.024 sec)
```
Here, the `dbms_sample` is a user-defined name (Any name can be given but database name with lower case is recommended)

#### SHOW DATABASES
`SHOW DATABASES` is a query to list all databases in the server
```sql
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| dbms_sample        |
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
6 rows in set (0.062 sec)
```

#### USE
`USE` is a keyword to use a specified table.
```sql
MariaDB [(none)]> USE dbms_sample;
Database changed
MariaDB [dbms_sample]>
```

#### CREATE TABLE
`CREATE TABLE` is a keyword to create table(s) inside the database
```sql
MariaDB [dbms_sample]> CREATE TABLE sample (number int, name char(25));
Query OK, 0 rows affected (0.297 sec)
```
Here, the `dbms_sample`, `number`, `name` is a user-defined name (Any name can be given to table name and column name but it is recommended to name with lower case)

#### SHOW TABLES
`SHOW TABLES` is a query to list all tables in the server
```sql
MariaDB [dbms_sample]> SHOW tables;
+-----------------------+
| Tables_in_dbms_sample |
+-----------------------+
| sample                |
+-----------------------+
1 row in set (0.001 sec)
```

#### DESC
`DESC` is a keyword to describe the table. Alternatively, we can use `DESCRIBE` and `EXPLAIN`.
```language
MariaDB [dbms_sample]> DESC sample;
+--------+----------+------+-----+---------+-------+
| Field  | Type     | Null | Key | Default | Extra |
+--------+----------+------+-----+---------+-------+
| number | int(11)  | YES  |     | NULL    |       |
| name   | char(25) | YES  |     | NULL    |       |
+--------+----------+------+-----+---------+-------+
2 rows in set (0.002 sec)

```

#### INSERT
`INSERT` is a keyword to add data into the table. 
```sql
MariaDB [dbms_sample]> INSERT INTO sample values(1, "Manoj");
Query OK, 1 row affected (0.057 sec)
```
Inserting data to particular column only
```sql
MariaDB [dbms_sample]> INSERT INTO sample (name) values ("Paramsetti");
Query OK, 1 row affected (0.058 sec)
```

#### SELECT
`SELECT` is a keyword to show table(s)
```sql
MariaDB [dbms_sample]> SELECT * FROM sample;
+--------+------------+
| number | name       |
+--------+------------+
|      1 | Manoj      |
|   NULL | Paramsetti |
+--------+------------+
2 rows in set (0.014 sec)
```

#### UPDATE
`UPDATE` is a keyword to update a value in table
```sql
MariaDB [dbms_sample]> UPDATE sample SET number=2 WHERE name="Paramsetti";
Query OK, 1 row affected (0.094 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [dbms_sample]> SELECT * FROM sample;
+--------+------------+
| number | name       |
+--------+------------+
|      1 | Manoj      |
|      2 | Paramsetti |
+--------+------------+
2 rows in set (0.001 sec)
```
If `WHERE` is not specified all the tuples will be updated

#### DELETE
`DELETE` is a keyword to remove tuples.
```sql
MariaDB [dbms_sample]> DELETE FROM sample WHERE number=2;
Query OK, 1 row affected (0.054 sec)

MariaDB [dbms_sample]> SELECT * FROM sample;
+--------+-------+
| number | name  |
+--------+-------+
|      1 | Manoj |
+--------+-------+
1 row in set (0.001 sec)
```

#### ALTER
`ALTER` is a keyword to modify the structure of the table.<br>
In alter we can do with 4 things
- `ADD COLUMN`
- `MODIFY`
- `RENAME COLUMN`
- `DROP COLUMN`
- `RENAME` | (Table Name)
##### ALTER (ADD COLUMN)
```sql
MariaDB [dbms_sample]> ALTER TABLE sample ADD department varchar(5);
Query OK, 0 rows affected (0.094 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [dbms_sample]> EXPLAIN sample;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| number     | int(11)     | YES  |     | NULL    |       |
| name       | varchar(25) | YES  |     | NULL    |       |
| department | varchar(5)  | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
3 rows in set (0.002 sec)
```
##### ALTER (MODIFY)
```sql
MariaDB [dbms_sample]> ALTER TABLE sample MODIFY department varchar(40);
Query OK, 0 rows affected (0.122 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [dbms_sample]> DESCRIBE sample;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| number     | int(11)     | YES  |     | NULL    |       |
| name       | varchar(25) | YES  |     | NULL    |       |
| department | varchar(40) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
3 rows in set (0.002 sec)
```
##### ALTER (RENAME)
```sql
MariaDB [dbms_sample]> ALTER TABLE sample RENAME COLUMN department TO class;
Query OK, 0 rows affected (0.171 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [dbms_sample]> DESC sample;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| number | int(11)     | YES  |     | NULL    |       |
| name   | varchar(25) | YES  |     | NULL    |       |
| class  | varchar(40) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
3 rows in set (0.138 sec)
```

##### ALTER (RENAME TABLE NAME)
```sql
MariaDB [dbms_sample]> ALTER TABLE sample RENAME TO class;
Query OK, 0 rows affected (0.200 sec)

MariaDB [dbms_sample]> SHOW tables;
+-----------------------+
| Tables_in_dbms_sample |
+-----------------------+
| class                 |
+-----------------------+
1 row in set (0.231 sec)
```

##### ALTER (DROP COLUMN)
```sql
MariaDB [dbms_sample]> ALTER TABLE sample DROP COLUMN class;
Query OK, 0 rows affected (0.110 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [dbms_sample]> DESC sample;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| number | int(11)     | YES  |     | NULL    |       |
| name   | varchar(25) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
2 rows in set (0.002 sec)
```

#### TRUNCATE
`TRUNCATE` will delete all the data but it will not modify the structre of the table
```sql
MariaDB [dbms_sample]> TRUNCATE class;
Query OK, 0 rows affected (0.703 sec)

MariaDB [dbms_sample]> SELECT * FROM class;
Empty set (0.116 sec)
```

#### DROP TABLE
`DROP TABLE` will delete all the data including the structre of the table.
<br>It is not recommened to use `DROP TABLE` everytime, `TRUNCATE` first and then use `DROP TABLE`
```sql
MariaDB [dbms_sample]> DROP TABLE class;
Query OK, 0 rows affected (0.093 sec)

MariaDB [dbms_sample]> SHOW TABLES;
Empty set (0.001 sec)
```

### Comments
Comment part will be ignored in the sql. we can use this to 
describe the commands.

##### In SQL it has two types of comments
1) Single line comments
2) Multi line comments

#### Single Line Comments
Single line comments will igrone the complete one line. We have 
to add `--` in the start to represent it is a comment.
```sql
MariaDB [dbms_sample]> --create table with name as char with the length of 25 and register number with the interger type
MariaDB [dbms_sample]> CREATE TABLE student (name char(25), registerName int);
Query OK, 0 rows affected (0.714 sec)
```
Here the SQL ignored the first line completely.

#### Multi Line Comments
Multi line comment will ignore some part of lines with 
`/*COMMENT*/`. we can ignore only some part of text in one line which will not consider the full line as comment
```sql
MariaDB [dbms_sample]> DESC student /*describing the table*/;
+--------------+----------+------+-----+---------+-------+
| Field        | Type     | Null | Key | Default | Extra |
+--------------+----------+------+-----+---------+-------+
| name         | char(25) | YES  |     | NULL    |       |
| registerName | int(11)  | YES  |     | NULL    |       |
+--------------+----------+------+-----+---------+-------+
2 rows in set (0.110 sec)
```

Here the `/*describing the table*/` part is ignored
```sql
MariaDB [dbms_sample]> /* Insert 2 students data inside the student table
   /*> Name: Manoj, Reg No: 40110901
   /*> Name: Paramsetti, Reg No: 40110902
   /*> */
MariaDB [dbms_sample]> INSERT INTO student values ("Manoj", 40110901);
Query OK, 1 row affected (0.144 sec)

MariaDB [dbms_sample]> INSERT INTO student values ("Paramsetti", 40110902);
Query OK, 1 row affected (0.340 sec)
```

Here the below lines are comments
```sql
/* Insert 2 students data inside the student table
   /*> Name: Manoj, Reg No: 40110901
   /*> Name: Paramsetti, Reg No: 40110902
   /*> */
```

## Keys & Constraints
Constraint will allow data with some condition

#### There are two ways of constraining:
>1) Column constraint: **Column constraint** will constraints only to column at a time

>2) Table constraint: **Table constraint** will declare the
contraints the two or more column at same time

#### Types of constraints:
- `UNIQUE`
- `PRIMARY KEY`
- `DEFAULT`
- `CHECK`
- `NOT NULL`
- `FOREIGN KEY`
- `ALTERNATE KEY`
- `COMPOSITE KEY` (Table constraint)

#### NOT NULL
`NOT NULL` will not allow null values in the specified column
```sql
MariaDB [dbms_sample]> CREATE TABLE student (registerNo int(8) NOT NULL, name char(30));
Query OK, 0 rows affected (0.197 sec)


MariaDB [dbms_sample]> INSERT INTO student (registerNo, name) VALUES (40110901, "Manoj");
Query OK, 1 row affected (0.353 sec)

MariaDB [dbms_sample]> INSERT INTO student (name) VALUES ("Manoj");
ERROR 1364 (HY000): Field 'registerNo' doesn't have a default value
```
Here, In third line we haven't passed registerNo data. So, the tuple is not inserted into the table

#### UNIQUE
`UNIQUE` Constarint will allow duplication in the specified column and shows warning
```sql
MariaDB [dbms_sample]> CREATE TABLE student1 (name char(25), registerNumber int UNIQUE);
Query OK, 0 rows affected (0.749 sec)

MariaDB [dbms_sample]> INSERT INTO student1 values ("Paramsetti", 40110901);
Query OK, 1 row affected (0.173 sec)

MariaDB [dbms_sample]> INSERT INTO student1 values ("Manoj", 40110901);
ERROR 1062 (23000): Duplicate entry '40110901' for key 'registerNumber'
```

#### ALTERNATE KEY
Alternate key is method to have one or more columns has unique to represent one tuple.
but all the unique key can't have `PRIMARY KEY`. `PRIMARY KEY` is allotted to only one column

#### PRIMARY KEY
`PRIMARY KEY` Constarint will not allow duplication in the specified column. Primary key is allowed to only one column
```sql
MariaDB [dbms_sample]> CREATE TABLE student2 (name char(25), registerNumber int NOT NULL PRIMARY KEY);
Query OK, 0 rows affected (0.234 sec)

MariaDB [dbms_sample]> INSERT INTO student2 values ("Manoj", 40110901);
Query OK, 1 row affected (0.053 sec)

MariaDB [dbms_sample]> INSERT INTO student2 values ("Paramsetti", 40110902);
Query OK, 1 row affected (0.044 sec)

MariaDB [dbms_sample]> INSERT INTO student2 values ("Param", 40110902);
ERROR 1062 (23000): Duplicate entry '40110902' for key 'PRIMARY'

MariaDB [dbms_sample]> INSERT INTO student2 values ("Param");
ERROR 1136 (21S01): Column count doesn't match value count at row 1
```

#### DEFAULT
`DEFAULT` is a keyword to add default value for a column. If the value is not specified, it will take the default value.
```sql
MariaDB [dbms_sample]> CREATE TABLE college (collegeName char(25) DEFAULT "Sathyabama", registerNumber int(10));
Query OK, 0 rows affected (0.375 sec)

MariaDB [dbms_sample]> DESC college;
+----------------+----------+------+-----+------------+-------+
| Field          | Type     | Null | Key | Default    | Extra |
+----------------+----------+------+-----+------------+-------+
| collegeName    | char(25) | YES  |     | Sathyabama |       |
| registerNumber | int(10)  | YES  |     | NULL       |       |
+----------------+----------+------+-----+------------+-------+
2 rows in set (0.051 sec)

MariaDB [dbms_sample]> INSERT INTO college (registerNumber) VALUES (40110901);
Query OK, 1 row affected (0.130 sec)

MariaDB [dbms_sample]> SELECT * FROM college;
+-------------+----------------+
| collegeName | registerNumber |
+-------------+----------------+
| Sathyabama  |       40110901 |
+-------------+----------------+
1 row in set (0.062 sec)
```

#### CHECK
`CHECK` is a keyword to allow only the specified data for a particular table
```sql
MariaDB [dbms_sample]> CREATE TABLE batch24 (registerNumber int, age int(2) CHECK (age = 19));
Query OK, 0 rows affected (0.315 sec)

MariaDB [dbms_sample]> INSERT INTO batch24 VALUES (40110901, 19);
Query OK, 1 row affected (0.066 sec)

MariaDB [dbms_sample]> INSERT INTO batch24 VALUES (40110901, 18);
ERROR 4025 (23000): CONSTRAINT `batch24.age` failed for `dbms_sample`.`batch24`
```

#### FOREIGN KEY
`FOREIGN KEY` is used to take only the primary key values presented in mentioned column. This values can be duplicated but it should contain in dervied table

```sql
MariaDB [dbms_sample]> desc student2;
+----------------+----------+------+-----+---------+-------+
| Field          | Type     | Null | Key | Default | Extra |
+----------------+----------+------+-----+---------+-------+
| name           | char(25) | YES  |     | NULL    |       |
| registerNumber | int(11)  | NO   | PRI | NULL    |       |
+----------------+----------+------+-----+---------+-------+
2 rows in set (0.002 sec)

MariaDB [dbms_sample]> CREATE TABLE student4 (registerNo int, FOREIGN KEY (registerNo) REFERENCES student2(registerNumber));
Query OK, 0 rows affected (0.215 sec)

MariaDB [dbms_sample]> select * from student2;
+------------+----------------+
| name       | registerNumber |
+------------+----------------+
| Manoj      |       40110901 |
| Paramsetti |       40110902 |
+------------+----------------+
2 rows in set (0.001 sec)

MariaDB [dbms_sample]> INSERT INTO student4 VALUES (40110901);
Query OK, 1 row affected (0.042 sec)

MariaDB [dbms_sample]> select * from student4;
+------------+
| registerNo |
+------------+
|   40110901 |
+------------+
1 row in set (0.001 sec)

MariaDB [dbms_sample]> INSERT INTO student4 VALUES (40110903);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`dbms_sample`.`student4`, CONSTRAINT `student4_ibfk_1` FOREIGN KEY (`registerNo`) REFERENCES `student2` (`registerNumber`))

```

## Clauses
#### query inside query
```sql
MariaDB [dbms_sample]> SELECT * FROM student1;
+------------+----------------+
| name       | registerNumber |
+------------+----------------+
| Paramsetti |       40110901 |
+------------+----------------+
1 row in set (0.001 sec)

MariaDB [dbms_sample]> SELECT * FROM student2;
+------------+----------------+
| name       | registerNumber |
+------------+----------------+
| Manoj      |       40110901 |
| Paramsetti |       40110902 |
+------------+----------------+
2 rows in set (0.001 sec)

MariaDB [dbms_sample]> SELECT * FROM student1 WHERE registerNumber=(SELECT registerNumber FROM student2 WHERE registerNumber=40110901); 
+------------+----------------+
| name       | registerNumber |
+------------+----------------+
| Paramsetti |       40110901 |
+------------+----------------+
1 row in set (0.043 sec)
```

## References
[SQL Tutorial - JavaPoint](https://www.javatpoint.com/sql-tutorial)
<br>
[MariaDB vs MySql - softwaretestinghelp](https://www.softwaretestinghelp.com/mariadb-vs-mysql/)
<br>
[SQL (ddl, dql, dml, dcl, tcl commands) - Geeks for geeks](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/)
<br>
[12th Computer Science - Samacheer kavli](https://drive.google.com/file/d/1JCjwGNrGbdlsg82xucbQ0E8LdzWTLnjr/view)