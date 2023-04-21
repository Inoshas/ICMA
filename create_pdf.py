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

