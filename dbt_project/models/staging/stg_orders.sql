-- stg_orders.sql
-- This model cleans up the raw orders data

select
    -- IDs
    "Invoice" as invoice_id,
    "StockCode" as stock_code,
    "Customer ID" as customer_id,

    -- Timestamps
    "InvoiceDate" as invoice_date,

    -- Order details
    "Quantity" as quantity,
    "Price" as unit_price,
    "Description" as description,
    "Country" as country

from {{ source('raw_data', 'raw_orders') }}
where "Customer ID" is not null
  and "Quantity" > 0