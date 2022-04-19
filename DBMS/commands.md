# DBMS Commands

[**GO DIRECTLY COPY**](https://docs.google.com/document/d/1f4thlZTo8w-6DyQJ-KChLDnKdpVvWHFseYginBm9Af8/edit?usp=sharing)

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

**DROP COLUMN**
- alter table example drop SEX;
  
**RENAME A COLUMN**
- alter table example rename column sex to gender;

**ADD Constraint**
- alter table example alter Salary set Default 10000;

## 2. DML Commands (Data Manipulation Language)
   
- **insert** into example values (1,"XYZ","1919-12-12","MALE");
- **select** * from example;
- **delete** from example where id =2;
- **update** example set name = "PQRS" where id= 1;
- select name from example;
- select distinct gender from example;
- select count(distinct gender) from example;
  // FOR DEFAULT VALUE CASE 
- insert into example (id,name,DOB,gender) values ( 1,"MANI","2020-12-23","MALE"); 
- DELETE FROM example; //Deleting all rows and keeping the table
- select name from class  where Roll between 1 **and** 4;
-  select Roll from class where name="Ram" **or** name="Krish";
-  select * from class where marks **is null**;
-  select * from class where marks **is not null**;


## 3. Constraints

- NOT NULL - Ensures that a column cannot have a NULL value
- UNIQUE - Ensures that all values in a column are different
- PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
  
- FOREIGN KEY - Prevents actions that would destroy links between tables
- CHECK - Ensures that the values in a column satisfies a specific condition, The CHECK constraint is used to limit the value range that can be placed in a column.
- DEFAULT - Sets a default value for a column if no value is specified
- CREATE INDEX - Used to create and retrieve data from the database very quickly
- create table person (id int not null);
-  alter table class modify roll int not null;
-   alter table class modify section varchar(10) primary key;
-   CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    UNIQUE (ID)
);
- create table person2 ( id int not null , age int, Unique (age));
- alter table person2 add Unique (id);
- create table person (id int Primary key Not null);
- CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);
-  alter table person add primary key (id);
-  alter table person drop primary key;

The `FOREIGN KEY` constraint is used to prevent actions that would destroy links between tables.

A `FOREIGN KEY` is a field (or collection of fields) in one table, that refers to the `PRIMARY KEY` in another table.

The table with the foreign key is called the `child table`, and the table with the primary key is called the `referenced` or `parent table`.

- create table orders ( OrderId int NOT NULL , PersonID int , Foreign Key (PersonID) References Persons(PersonID) ); //Keep in mind PersonID should be Primary Key in Persons Table.

- ALTER TABLE Persons
ADD CHECK (Age>=18);

-CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255),
    CONSTRAINT CHK_Person CHECK (Age>=18 AND City='Sandnes')
);

- create table persons (id int Primary key ,age int, constraint check_p check (age>0 and age<100)) ;
- alter table person2 add check (age>0);
-   create table person (id int default 1);
-   ALTER TABLE Persons
- ALTER City SET DEFAULT 'Sandnes';
- ALTER TABLE Persons
  ALTER City DROP DEFAULT;

  ### Agregate Functions 

  1. select **max**(marks) from class;
  2. select **min**(marks) from class;
  3. select **avg**(marks) from class;
  4. select **sum**(marks) from class;
  5. select **count**(marks) from class;

### LIKE 

WHERE CustomerName LIKE 'a%' ->	Finds any values that start with "a"

WHERE CustomerName LIKE '%a' ->	Finds any values that end with "a"

WHERE CustomerName LIKE '%or%' -> Finds any values that have "or" in any position

WHERE CustomerName LIKE '_r%' ->	Finds any values that have "r" in the second position

WHERE CustomerName LIKE 'a_%' ->Finds any values that start with "a" and are at least 2 characters in length

WHERE CustomerName LIKE 'a__%' ->	Finds any values that start with "a" and are at least 3 characters in length

WHERE ContactName LIKE 'a%o' ->	Finds any values that start with "a" and ends with "o"

eg - `SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';`

# IMP Topics

### Joins ( For more help look at this [Link](https://www.w3schools.com/sql/sql_join.asp))

1. Inner Joins
   `SELECT table1.column1,table1.column2,table2.column1,....
FROM table1 
INNER JOIN table2
ON table1.matching_column = table2.matching_column;`

`REST ON NET`

## Misc

1. The `IN` operator allows you to specify multiple values in a WHERE clause.

The IN operator is a shorthand for multiple OR conditions.

2. [SUB_QUERIES](https://www.javatpoint.com/dbms-sql-sub-queries)

3. [Views](https://www.javatpoint.com/dbms-sql-view)














