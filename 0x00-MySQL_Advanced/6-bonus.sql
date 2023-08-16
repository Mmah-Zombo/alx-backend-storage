-- creates a stored procedure AddBonus
-- that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS AddBonus(user_id INT, project_name VARCHAR(225), score FLOAT)
BEGIN
    UPDATE users
END $$
DELIMITER ;
