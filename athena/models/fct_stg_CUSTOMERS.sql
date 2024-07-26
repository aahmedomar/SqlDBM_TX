SELECT
    stg_CUSTOMERS.ID AS "ID",
    stg_CUSTOMERS.FIRST_NAME AS "FIRST_NAME",
    stg_CUSTOMERS.LAST_NAME AS "LAST_NAME",
    stg_CUSTOMERS.__load_date AS "__load_date",
    current_date() AS "__load_date_1"
FROM {{ref('My Location', 'stg_CUSTOMERS')}} "stg_CUSTOMERS"