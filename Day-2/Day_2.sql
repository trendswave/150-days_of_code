-- sedlects all column wishers table
SELECT * FROM wishers
-- further filtering using the time frame
WHERE wishes BETWEEN '2024-10-01' AND '2024-11-01';
--joins the(student*) and using A for ALX and F for FUTO
SELECT * FROM Alx_students AS A
JOIN Futo_students AS F ON A.student_id = F.student_id;
-- uses a case statement to conditionally genarate message based on type column on the individual table or type table
SELECT 
    CASE 
        WHEN type = 'student' THEN CONCAT('Thank you, let\'s continue to do hard things, God bless you From me PAUL CHINEDU MICHEAL to you.')
        WHEN type = 'family' OR type = 'mentor' THEN CONCAT('You have been the backbone of this journey, God bless you the more From me PAUL CHINEDU MICHEAL to you.')
        WHEN type = 'friends' THEN CONCAT('Thanks for being an inspiration, God bless you richly From me PAUL CHINEDU MICHEAL to you.')
        ELSE CONCAT('Thank you very much, may God richly bless you. From me PAUL CHINEDU MICHEAL to you.')
    END AS message
FROM individuals;
