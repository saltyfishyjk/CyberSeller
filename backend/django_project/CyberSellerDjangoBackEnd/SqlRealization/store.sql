# 存储过程
use CyberSeller_db1;
drop procedure if exists searchGood;
delimiter $$
create procedure searchGood(in input varchar(255))
begin
    select *
        from backendapp_good
            where name like concat('%', input);
end $$
delimiter ;