#gmaps = googlemaps.Client(key='AIzaSyAvHrKFbATTJDhRqGqQrlYnmHp__UoGNHY')
from flask import Flask, render_template, request, send_from_directory
import sqlite3
import googlemaps
from fpdf import FPDF
import os

app1 = Flask(__name__)
app1.config['SECRET_KEY'] = 'your-secret-key'

# Replace 'your-api-key' with your actual Google Maps API key
gmaps = googlemaps.Client(key='AIzaSyAvHrKFbATTJDhRqGqQrlYnmHp__UoGNHY')

# Set the default origin address
DEFAULT_ORIGIN = 'Yliopistokatu, Oulu, Finland'


def get_db_connection():
    conn = sqlite3.connect('invoice.db')
    conn.row_factory = sqlite3.Row
    return conn


def close_db_connection(conn):
    conn.close()


@app1.route('/')
def index():
    destination = 'Enter Destination'  # Placeholder for destination in the template
    return render_template('index_invoice.html', default_origin=DEFAULT_ORIGIN, destination=destination)


@app1.route('/calculate', methods=['POST'])
def calculate():
    destination = request.form['destination']

    try:
        # Get the directions using Google Maps API
        directions = gmaps.directions(DEFAULT_ORIGIN, destination)

        # Extract the distance from the directions response
        distance = directions[0]['legs'][0]['distance']['text']
        

        # Save the invoice details to the database
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO invoices (origin, destination, distance) VALUES (?, ?, ?)',
                  (DEFAULT_ORIGIN, destination, distance))
        conn.commit()
        close_db_connection(conn)

        return render_template('result.html', distance=distance)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('result.html', error=error_message)


@app1.route('/invoice', methods=['POST'])
def invoice():
    # Retrieve invoice details from the database
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM invoices ORDER BY id DESC LIMIT 1')
    invoice_data = c.fetchone()
    close_db_connection(conn)

    if invoice_data:
        invoice_id, origin, destination, distance= invoice_data

        # Create a PDF invoice
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, f'Invoice #{invoice_id}', ln=True)
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, f'Origin: {origin}', ln=True)
        pdf.cell(0, 10, f'Destination: {destination}', ln=True)
        pdf.cell(0, 10, f'Distance: {distance}', ln=True)

        # Save the PDF in the "pdfs" directory
        pdf_dir = 'pdfs'
        if not os.path.exists(pdf_dir):
            os.makedirs(pdf_dir)
        pdf_path = os.path.join(pdf_dir, f'invoice_{invoice_id}.pdf')
        pdf.output(pdf_path)

        # Return a link to download the PDF
        return render_template('download.html', invoice_id=invoice_id)

    else:
        return 'No invoices found.'


@app1.route('/download/<invoice_id>')
def download(invoice_id):
    pdf_dir = 'pdfs'
    pdf_path = os.path.join(pdf_dir, f'invoice_{invoice_id}.pdf')
    return send_from_directory(directory=pdf_dir, filename=f'invoice_{invoice_id}.pdf', as_attachment=True)


if __name__ == '__main__':
    app1.run(debug=True)