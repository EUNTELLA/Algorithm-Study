select i.id , n.fish_name, i.length
from fish_info i
join fish_name_info n on i.fish_type = n.fish_type
WHERE 
    (I.FISH_TYPE, I.LENGTH) IN (
        SELECT FISH_TYPE, MAX(LENGTH)
        FROM FISH_INFO
        GROUP BY FISH_TYPE
    )
ORDER BY 
    I.ID ASC
