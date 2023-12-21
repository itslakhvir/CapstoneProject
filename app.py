
from flask import Flask, request, jsonify, render_template
import utils  # Importing the utility functions
import model  # Importing the model handling
# import nltk
import os
nltk_data_path = "C:\\home\\codespace\\nltk_data\\tokenizers\\punkt\\PY3\\english.pickle"
os.environ["NLTK_DATA"] = nltk_data_path

app = Flask(__name__)

@app.route('/')
def index():
    # Rendering the main page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extracting the text from the request
    text = request.form['text']
    
    # Making a prediction using the model
    prediction = model.predict_stress(text)

    # Returning the prediction as JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
