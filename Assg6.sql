declare
cursor cur is select * from N_RollCall;
roll integer;
sname varchar(20);
cell number(10);
begin
open cur;
loop
fetch cur into roll,sname,cell;
for i in (select * from O_RollCall) loop
if(roll = i.rollno) then
dbms_output.put_line(roll || 'is already present');
else
insert into O_RollCall values(roll,sname,cell);
end if;
end loop;
exit when cur%notfound;
end loop;
close cur;
end;
