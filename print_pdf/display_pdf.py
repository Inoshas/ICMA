#mport pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
import sqlite3
import fitz
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import os




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
pdf.cell(80, 20, "Product Name")
pdf.cell(80, 20, "Price")
pdf.cell(80, 20, "Quantity")
pdf.ln()


# Add table rows
for row in rows:
    pdf.cell(80, 20, str(row[2]))
    pdf.cell(80, 20, str(row[1]))
    pdf.cell(80, 20, str(row[3]))
    pdf.ln()

# Save the PDF file with variable names
product_name = 'Inventory'
pdf.output(f"{product_name}.pdf")

current_dir = os.path.dirname(os.path.abspath(__file__))

# create the path to the file
file_name = f"{product_name}.pdf"
pdf_file = os.path.join(current_dir, file_name)


#pdf_file = f"/Users/tirtha/Desktop/Python-Group-Project/Python-Group-Project/{product_name}.pdf"  #'path/to/myfile.pdf

print(pdf_file)


doc = fitz.open(pdf_file)
page = doc.load_page(0)
pix = page.get_pixmap()

# convert the pixmap to a PIL image
img = Image.open(BytesIO(pix.tobytes()))  # use png instead of get_png_data()

# display the PIL image using matplotlib
plt.imshow(img)
plt.axis('off')
plt.show()

# Close the cursor and the database connection
cursor.close()
conn.close()