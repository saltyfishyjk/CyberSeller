use CyberSeller_db1;
DELIMITER $$
CREATE FUNCTION getPrice(price integer) RETURNS varchar(3)
DETERMINISTIC
BEGIN
    case
        when (price >= 5000) then return '昂贵';
        when (price >= 2000) then return '一般';
        else return '廉价';
    end case;
END $$
DELIMITER ;