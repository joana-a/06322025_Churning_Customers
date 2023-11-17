from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
import pickle

app = Flask(_name_)

# Load the pre-trained Keras model
model = load_model("mlp_keras.h5", "rb")
scaler = pickle.load(open("scaler.pkl","rb"))

# Define label mappings
contract_mapping = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
payment_method_mapping = {'Bank transfer (automatic)': 0, 'Credit card (automatic)': 1, 'Electronic check': 2, 'Mailed check': 3}
online_backup_mapping = {'No': 0, 'No internet service': 1, 'Yes': 2}

# Define the route for the home page
@app.route('/churn_index.html')
def home():
    return render_template('churn_index.html')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get user inputs from the form
    total_charges = float(request.form['total_charges'])
    monthly_charges = float(request.form['monthly_charges'])
    tenure = int(request.form['tenure'])
    contract = request.form['contract']
    payment_method = request.form['payment_method']
    online_backup = request.form['online_backup']

    # Manual encoding based on label mappings
    contract_encoded = contract_mapping.get(contract, -1)
    payment_method_encoded = payment_method_mapping.get(payment_method, -1)
    online_backup_encoded = online_backup_mapping.get(online_backup, -1)

    # Check if any encoding failed
    if contract_encoded == -1 or payment_method_encoded == -1 or online_backup_encoded == -1:
        return render_template('error.html')

    # Prepare the input data for prediction
    input_data = np.array([[total_charges, monthly_charges, tenure, contract_encoded, payment_method_encoded, online_backup_encoded]])


    prediction = model.predict(input_data)

    predicted_class = np.argmax(prediction)

    predicted_label = "Churn" if predicted_class == 1 else "No Churn"

    # Render the prediction result
    return render_template('churn_result.html', prediction=predicted_label)

if _name_ == '_main_':
    app.run(debug=True)