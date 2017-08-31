declare 
	cursor c is select * from new_table;
	roll_V Number;
	name_v varchar2(20);
	gender_v char(5);
	flag number(5);
begin
	flag :=0;
	open c;
	loop
	fetch c into roll_v,name_v,gender_v;
	flag:=0;
	for i in (select * from old_table) loop
		
		if(roll_v = i.ROLL and name_v = i.Name) then 
			dbms_output.put_line('Entry Found');
			flag := 1;
		end if;
		
	end loop;
	if(flag = 0) then
		insert into old_table values(roll_v,name_v,gender_v);
	end if;
	exit when c%notfound;
	end loop;
	
	end;
