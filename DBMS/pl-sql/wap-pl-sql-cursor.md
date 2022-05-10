## WAP ON PL/SQL CURSOR

```
DECLARE 

Total_rows number(2);
BEGIN

UPDATE customers

SET salary = salary + 5000;

if sql%notfound THEN
Dbms_outline.put_line("no customers updated")

ELSIF sql%found THEN

total_rows:=sql%rowcount;

Dbms_outline.put_line(totalrows || "customers updated");

END IF;
END;