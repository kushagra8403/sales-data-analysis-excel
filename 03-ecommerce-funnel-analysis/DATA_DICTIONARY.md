# Data Dictionary

| Field | Type | Meaning |
|---|---|---|
| session_id | string | Unique web session |
| traffic_source | category | Acquisition source |
| device | category | Device used for the session |
| product_view | integer | 1 if a product was viewed |
| add_to_cart | integer | 1 if an item was added to cart |
| checkout | integer | 1 if checkout was reached |
| purchase | integer | 1 if a purchase occurred |
| revenue | numeric | Revenue attributed to the session |

**Grain:** one row per session.
