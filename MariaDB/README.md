# MariaDB Reference Notes (MySql)

## About MySql
MySQL is a Swedish company. The name of the parent company that created this DB is MySQL AB. The first version of the software was launched in May 1995. Currently, MySQL is managed by Oracle.

## About MariaDB
MariaDB is forked out of MySQL. So, there are lot of similarities between these two databases. 

## About SQL Commands
**Five types of SQL queries:**
1) Data Definition Language (DDL)
2) Data Manipulation Language (DML)
3) Data Control Language(DCL)
4) Transaction Control Language(TCL)
5) Data Query Language (DQL)

**DDL commands:**
`CREATE`, `DROP`, `ALTER`, `TRUNCATE`, `COMMENT`, `RENAME`

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
Here, the `dbms_sample` is a user-defined name (Any name can be given but table name with lower case is recommended)

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
MariaDB [dbms_sample]> CREATE TABLE sample (number int, name char);
Query OK, 0 rows affected (0.297 sec)
```

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


## References
https://www.softwaretestinghelp.com/mariadb-vs-mysql/ 
<br>
https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/
