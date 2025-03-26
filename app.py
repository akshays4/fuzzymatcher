from flask import Flask, request, render_template, send_file
import csv
from fuzzywuzzy import fuzz
import io
import os

app = Flask(__name__)

# Function to perform fuzzy matching
def fuzzy_match(names, threshold=80):
    matches = []
    for name in names:
        for other_name in names:
            if name != other_name:  # Skip matching the name with itself
                similarity = fuzz.ratio(name, other_name)
                if similarity >= threshold:
                    matches.append([name, other_name, similarity])
    return matches

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Upload and process CSV
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400
    
    if file and file.filename.endswith('.csv'):
        # Read the CSV and perform fuzzy matching
        names = []
        csvfile = file.read().decode('utf-8').splitlines()
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            names.append(row[0])

        # Perform fuzzy matching
        matched_names = fuzzy_match(names)

        # Write matched results to a CSV file
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Name', 'Matched Name', 'Similarity (%)'])
        writer.writerows(matched_names)
        output.seek(0)

        # Send the file back to the user
        return send_file(io.BytesIO(output.getvalue().encode('utf-8')), attachment_filename='fuzzy_matches.csv', as_attachment=True)

    return "Invalid file format. Please upload a CSV file.", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
