-- display the average temperature (in fahrenherit)

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperature`
GROUP BY `city`
ORDER BY `avg_temp` DESC;