import pandas as pd 
import sqlite3 
import matplotlib.pyplot as plt 

conn = sqlite3.connect("../db/lesson.db")


query = """
SELECT last_name, 
       SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

employee_results = pd.read_sql_query(query, conn)
print(employee_results)
print(employee_results.dtypes)


conn.close()

# Plotting with pandas
ax = employee_results.plot(
    kind='bar',
    x='last_name',
    y='revenue',
    color='skyblue',
    legend=False 
)

# customize plot 
ax.set_title("Revenue by Employee")
ax.set_xlabel("Employee Last Name")
ax.set_ylabel("Total Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# show plot 
plt.show()
