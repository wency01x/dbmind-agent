# Business Rules

- users: is_active=false means the account is soft deleted, never show these users
- orders: status can be 'pending', 'paid', 'cancelled', 'refunded'
- orders: always filter by user_id when fetching a specific user's orders
- order_items: price column is the price at time of purchase, not current product price
- products: stock=0 means out of stock