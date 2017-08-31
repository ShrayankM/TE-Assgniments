declare 
	cursor c is select * from old_table;
	roll_V Number;
	name_v varchar2(20);
	gender_v char(5);
begin
	
	open c;
	fetch c into roll_v,name_v,gender_v;
	for i in (select * from new_table) loop
		if(roll_v = i.ROLL and name_v = i.Name) then 
			dbms_output.put_line('Entry Found');
		else
			insert into old_table values(i.ROLL,i.NAME,i.GENDER);
		end if;
	exit when c%notfound;
	end loop;
	end;
