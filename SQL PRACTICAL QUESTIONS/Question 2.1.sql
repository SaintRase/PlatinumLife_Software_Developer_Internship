SELECT SUM(CASE WHEN S < 0 THEN S ELSE 0 END) AS negative_sum, SUM(CASE WHEN S > 0 THEN S ELSE 0 END) AS positive_sum
FROM Numbers;
