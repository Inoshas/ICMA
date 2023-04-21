#mport pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF

import sqlite3



# Connect to the database
conn = sqlite3.connect('Inventory_and_price.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to fetch all data from the 'Inventory' table
cursor.execute('SELECT * from Inventory')

# Fetch all the rows from the query result
rows = cursor.fetchall()


# Define PDF document properties

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add table header
pdf.cell(40, 10, "Product Name")
pdf.cell(40, 10, "Price")
pdf.cell(40, 10, "Quantity")
pdf.ln()


# Add table rows
for row in rows:
    pdf.cell(40, 10, str(row[2]))
    pdf.cell(40, 10, str(row[1]))
    pdf.cell(40, 10, str(row[3]))
    pdf.ln()

# Save the PDF file with variable names
product_name = 'Inventory'
pdf.output(f"{product_name}.pdf")

# Close the cursor and the database connection
cursor.close()
conn.close()
'''
# Connect to the database
conn = sqlite3.connect('Inventory_and_price.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to fetch all data from the 'Inventory' table
cursor.execute('SELECT * FROM Inventory')
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()


df = pd.DataFrame()
df['Question'] = ["Q1", "Q2", "Q3", "Q4"]
df['Charles'] = [3, 4, 5, 3]
df['Mike'] = [3, 3, 4, 4]

title("Professor Criss's Ratings by Users")
xlabel('Question Number')
ylabel('Score')

c = [2.0, 4.0, 6.0, 8.0]
m = [x - 0.5 for x in c]

xticks(c, df['Question'])

bar(m, df['Mike'], width=0.5, color="#91eb87", label="Mike")
bar(c, df['Charles'], width=0.5, color="#eb879c", label="Charles")

legend()
axis([0, 10, 0, 8])
savefig('barchart.png')

pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 12)
pdf.cell(60)
pdf.cell(75, 10, "A Tabular and Graphical Report of Professor Criss's Ratings by Users Charles and Mike", 0, 2, 'C')
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-40)
pdf.cell(50, 10, 'Question', 1, 0, 'C')
pdf.cell(40, 10, 'Charles', 1, 0, 'C')
pdf.cell(40, 10, 'Mike', 1, 2, 'C')
pdf.cell(-90)
pdf.set_font('arial', '', 12)
for i in range(0, len(df)):
    pdf.cell(50, 10, '%s' % (df['Question'].iloc[i]), 1, 0, 'C')
    pdf.cell(40, 10, '%s' % (str(df.Mike.iloc[i])), 1, 0, 'C')
    pdf.cell(40, 10, '%s' % (str(df.Charles.iloc[i])), 1, 2, 'C')
    pdf.cell(-90)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-30)
pdf.image('barchart.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
pdf.output('test.pdf', 'F')
'''

