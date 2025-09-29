import pandas as pd 
import sqlite3 
import matplotlib.pyplot as plt 

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT o.order_id,
    SUM(p.price * l.quantity) AS total_price 
FROM orders o
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY o.order_id 
ORDER BY o.order_id 
"""

df = pd.read_sql_query(query, conn)
conn.close ()

if df.empty:
    print("No order data found.")
else:
    df['cumulative'] = df['total_price'].cumsum()
    
    ax = df.plot(
        x='order_id',
        y='cumulative',
        kind='line',
        marker='o',
        title='Cumulative Revenue by Order ID',
        xlabel='Order ID',
        ylabel='Cumulative Revenue ($)',
        color='green'
    )

plt.grid(True)
plt.tight_layout()
plt.show()