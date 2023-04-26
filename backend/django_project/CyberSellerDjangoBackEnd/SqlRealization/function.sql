use CyberSeller_db1;
DROP FUNCTION IF EXISTS getPrice;
DELIMITER $$
CREATE FUNCTION getPrice(price integer) RETURNS varchar(3)
DETERMINISTIC
BEGIN
    case
        when (price >= 50) then return '昂贵';
        when (price >= 20) then return '一般';
        else return '廉价';
    end case;
END $$
DELIMITER ;

