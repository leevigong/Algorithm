-- 코드를 작성해주세요
select i.item_id, i.item_name
from item_info i
inner join item_tree t on t.item_id = i.item_id 
where t.parent_item_id is NULL
order by i.item_id asc


