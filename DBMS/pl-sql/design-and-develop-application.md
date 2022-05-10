##  TO DESIGN AND DEVELOP APPICATION

```
DECLARE 
Veno emp.id %type;
Vnameemp.name%type

BEGIN

SELECT id,name,salary into Sno, vname,vsal
from EMP where EMP.id='%eno';

Dbms_outline.put_line('EMP no='||veno);
Dbms_outline.put_line('EMP name='||vname);
Dbms_outline.put_line('EMP salary='||vsal);

END;
```