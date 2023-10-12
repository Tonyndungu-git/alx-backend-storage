-- selects bandname and year with glamrock
SELECT band_name, 
     (IFNULL(split, '2020') - formed) as lifespan
FROM metal_bands
WHERE style = FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC;
