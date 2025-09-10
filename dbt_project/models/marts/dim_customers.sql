-- dim_customers.sql

with source as (
    -- Get the raw data from the staging model
    select
        customer_id,
        country,
        invoice_date
    from {{ ref('stg_orders') }}
),

ranked as (
    -- For each customer, rank their orders by date, with the newest being #1
    select
        customer_id,
        country,
        -- This is a window function. It partitions the data by customer
        -- and orders it by date to find the most recent record for each.
        row_number() over (partition by customer_id order by invoice_date desc) as rank_num
    from source
)

-- Final selection: only take the most recent record for each customer
select
    customer_id,
    country
from ranked
where rank_num = 1