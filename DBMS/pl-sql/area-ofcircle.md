## AREA OF CIRCLE

```
declare 
radius number(3);
area number(20,3);
pi constant number(3,2):=3.14;

begin

radius:=5;

while(radius<=10)
loop

area:=pi*radius*radius;

insert into areas values(radius,area);
radius:=radius + 1;
end loop

END;
```