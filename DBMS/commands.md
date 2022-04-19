# DBMS Commands

## 1.  DDL Commands (Data Defination Language)

- CREATE DATABASE SRM
- USE SRM
- CREATE TABLE EXAMPLE (id int , name varchar, DOB date);
- desc example; --> Describel Table 
-  **Alter Table Commands**
1.  The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.

The ALTER TABLE statement is also used to add and drop various constraints on an existing table.

eg - 

**ALTER TABLE - ADD Column**
- alter table example add Sex varchar(10);

**ALTER TABLE - DROP COLUMN**
-  alter table example drop column Sex;

**ALTER TABLE - CHANGE DATATYPE OF COLUMN**
- alter table example Modify column id varchar(10);
`
