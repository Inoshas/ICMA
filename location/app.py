"""
from flask import Flask

import googlemaps

app = Flask(__name__)

# Initialize the Google Maps API client
gmaps = googlemaps.Client(key='API key')

# Define a route to display the distance between two addresses
@app.route('/')
def distance():
    start_address = 'Tapiotie, Oulu, Finland'
    end_address = 'Koulukatu, Oulu, Finland'
    result = gmaps.distance_matrix(start_address, end_address)
    distance = result['rows'][0]['elements'][0]['distance']['text']
    return f"The distance between {start_address} and {end_address} is {distance}."


if __name__ == '__main__':
    app.run()
"""
from flask import Flask, request
import googlemaps

app = Flask(__name__)
gmaps = googlemaps.Client(key='API KEY')

@app.route('/', methods=['GET', 'POST'])
def distance():
    if request.method == 'POST':
        start_address = 'Tapiotie, Oulu, Finland'
        end_address = request.form['end_address']
        result = gmaps.distance_matrix(start_address, end_address)
        distance = result['rows'][0]['elements'][0]['distance']['text']
        return f"The distance between {start_address} and {end_address} is {distance}."
    return '''
        <form method="post">
            <label for="end_address">End Address:</label>
            <input type="text" id="end_address" name="end_address" required>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
