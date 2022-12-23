DELIMITER $$
CREATE TRIGGER 库存大于等于零 after update on backendapp_repo
    for each row
    begin
        if (new.repo < 0) then
            signal sqlstate '65666' set message_text = '库存不能小于0';
        end if;
    end $$
DELIMITER ;