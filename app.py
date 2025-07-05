from flask import Flask, request, jsonify
import pickle
import pandas as pd
import sklearn
app = Flask(__name__)

with open('best_client_classification_model_final.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    feature_names = model.feature_names_in_
    return jsonify({
        "Required Params": list(feature_names)
    })
    

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)[0]
        result = "Best Client for Promotion" if prediction == 1 else "Not Recommended"

        return jsonify({
            "prediction": result,
            "raw_prediction": int(prediction),
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run()
