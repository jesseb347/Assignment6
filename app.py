from flask import Flask, Response, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Serve CSV data as JSON
@app.route('/get-csv-data')
def get_csv_data():
    df = pd.read_csv('projects_feedback.csv')
    return jsonify(df.to_dict(orient='records'))

# Directly serve the CSV file
@app.route('/download-csv')
def download_csv():
    csv_path = 'projects_feedback.csv'
    with open(csv_path, 'r') as f:
        csv_content = f.read()
    return Response(
        csv_content,
        mimetype='text/csv',
        headers={"Content-disposition": "attachment; filename=projects_feedback.csv"})

# Directly serve the ZIP file
@app.route('/download-zip')
def download_zip():
    zip_path = 'content.zip'
    with open(zip_path, 'rb') as f:
        zip_content = f.read()
    return Response(
        zip_content,
        mimetype='application/zip',
        headers={"Content-disposition": "attachment; filename=content.zip"})

if __name__ == '__main__':
    app.run(debug=True)
