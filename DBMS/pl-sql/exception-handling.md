### Exception Handling 

``` 
declare 
c_id customers.id%type:=8;
c_name customers.address%type;

BEGIN

select name ,address INTO c_name, c_addr

FROM customers

where id = c.id

Dbms_outline.put_line("Name:"|| c_name);
Dbms_outline.put_line("Address:" c_addr);

EXCEPTION

WHEN no_data_found THEN

Dbms_outline.put_line("No such customer");

WHEN others THEN

Dbms_outline.put_line("Error");

END;
```