-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID 
from online_sale
group by USER_ID,PRODUCT_ID
having count(*) >=2
oRDER BY USER_ID ASC, PRODUCT_ID DESC;