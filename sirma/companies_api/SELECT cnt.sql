SELECT cnt.name AS country, co.name AS company,
 co.phone, co.email,
 case when co.status = 1 then 'Important' 
    when co.status = 0  then 'Not Important' 
    else 'Normal' end as status
 , type.contact_type,
  c.date, res.contact_result

FROM companies_contact AS c
JOIN companies_company AS co ON c.company_id = co.id
JOIN companies_country AS cnt ON co.country_id = cnt.id
JOIN companies_contacttype AS type ON c.typ_id = type.id
JOIN companies_contactresult AS res ON c.result_id = res.id
WHERE co.user_id = 2
order by cnt.name, co.name , c.date 
-- group by cnt.name, co.name
;
