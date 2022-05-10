## PL/ SQL FOR  CALCULATING FACTORIAL OF A NUMBER 

```
declare 
fact number(10):=1;
n number(10);
begin
n:=&n;
while(n>=1)
loop
fact:=fact*n;
n:=n-1;

end loop

dbms_output.put_line('Answer='||fact);

end;
```