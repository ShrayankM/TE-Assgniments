
declare
    roll_numberI number(5);
    RollNumber number(5);
    no_of_days number(5);
    no_of_daysT number(5);
    Name_of_Book varchar2(20);
    BookName varchar2(20);
    datet date;
    fineV number(5);
    fine number(5);
    issueN char(5);
    dateVar date := to_date(sysdate);

begin

    roll_numberI := &RollNumber;
    Name_of_Book := &BookName;

    issueN :=&issueN;

    select DATEOFISSUE into datet from BorrowerN where ROLLIN = roll_numberI
        and NAMEOFBOOK = Name_of_Book;

        no_of_days := dateVar - datet;
        dbms_output.put_line(no_of_days);
    if(no_of_days > 15 and no_of_days < 30) then
      fineV := (no_of_days - 15) * 15;
    end if;

    if(no_of_days > 30) then
      no_of_daysT := no_of_days;
      no_of_days := no_of_days - 30;
      fineV := (no_of_days) * 50;
      fineV := fineV + (15*5);
    end if;


    insert into FineN values(roll_numberI,dateVar,fineV);
    if(issueN = 'R') then
      update BorrowerN set Status = 'R' where ROLLIN = roll_numberI
      and NAMEOFBOOK = Name_of_Book;
    end if;


    if(issueN = 'I') then
        update BorrowerN set Status = 'I',DATEOFISSUE=dateVar where ROLLIN = roll_numberI
        and NAMEOFBOOK = Name_of_Book;
    end if;
end;
