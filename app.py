# from flask import Flask
from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
# @app.route('/')
# def welcome():
#     return "Hello World"


# @app.route('/home')
# def home():
#     return "this is home page again and again"


# from controller import userController, productContriller 

# Read CSV file
def read_csv(file_path):
    return pd.read_csv(file_path)

# Search function
def search_data(data, criteria):
    return data[data['domain'] == criteria]


@app.route('/api/data', methods=['GET'])
def get_csv_data():
    # Read CSV file
    csv_data = read_csv('data.csv')
    return jsonify(csv_data.to_dict(orient='records'))


@app.route('/api/search', methods=['GET'])
def search_csv_data():
    criteria = request.args.get('criteria')
    if not criteria:
        return jsonify({'error': 'Criteria parameter is missing'}), 400
    
    # Read CSV file
    csv_data = read_csv('data.csv')
    
    # Search data
    result = search_data(csv_data, criteria)
    
    return jsonify(result.to_dict(orient='records'))

# ******************************************************
def read_csv(file_path):
    return pd.read_csv(file_path)
# Search function
def desc_data(data, domain_criteria, uni_name_criteria):
   return data[(data['Domain'] == domain_criteria) & (data['Uni Name'] == uni_name_criteria)]

@app.route('/api/description', methods=['GET'])
def desc_csv_data():
    domain_criteria = request.args.get('domain_criteria')
    uni_name_criteria = request.args.get('uni_name_criteria')
    
    if not domain_criteria or not uni_name_criteria:
        return jsonify({'error': 'Domain or Uni Name criteria parameter is missing'}), 400
    
    # Read CSV file
    csv_data = read_csv('data2.csv')
    
    # Search data
    result = desc_data(csv_data, domain_criteria, uni_name_criteria)
    
    return jsonify(result.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)