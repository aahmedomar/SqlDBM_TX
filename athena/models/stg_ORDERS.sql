SELECT
    ORDERS.ID AS "ID",
    ORDERS.USER_ID AS "USER_ID",
    ORDERS.ORDER_DATE AS "ORDER_DATE",
    ORDERS.STATUS AS "STATUS",
    current_date() AS "__load_date"
FROM {{ref('My Location', 'ORDERS')}} "ORDERS"