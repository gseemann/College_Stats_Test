SELECT * FROM colleges.payscale_colleges;
DROP TABLE colleges.movies_1;
SELECT * FROM colleges.college_info;

CREATE TABLE colleges.colleges_inner AS 
	(SELECT 
		*
	FROM 
		colleges.college_info
		INNER JOIN 
			colleges.payscale_colleges
			ON 
				college_info.college = payscale_colleges.uni);
                
ALTER TABLE colleges.colleges_inner DROP uni;

SELECT
	*
FROM
	colleges.colleges_inner;
