import pandas as pd
from flask import Flask, jsonify, render_template, request
import sys
import logging

# Add your backorder project to system path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
#sys.path.append('C:\\Users\\adith\\Desktop\\backorder\\src')

from src.backorder_project import pipeline
from src.backorder_project.entity import DataIngestionConfig

# Initialize Flask app
app = Flask(__name__)

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO)

# Initialize pipeline objects
ingestion_config = DataIngestionConfig()
training = pipeline.Training()
prediction = pipeline.Prediction()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train_model', methods=['POST'])
def train_model():
    app.logger.info("Training started...")  # Log the start of training
    try:
        training.initiate()  # Start training process
        app.logger.info("Training completed.")  # Log the completion of training
        return render_template('train_completed.html', message='Model Training Completed!')
    except Exception as e:
        app.logger.error(f"Error during training: {e}")  # Log any error that occurs
        return jsonify({'error': f"An error occurred during training: {e}"})

@app.route('/predict')
def predict():
    return render_template(
        'predict.html',
        num_cols=ingestion_config.num_cols,
        cat_cols=ingestion_config.cat_cols,
    )

@app.route('/one_prediction', methods=['POST'])
def one_prediction():
    form_data = dict(request.form)
    df = pd.DataFrame([form_data.values()], columns=list(form_data.keys()))
    try:
        prediction_result = pipeline.Prediction.one_prediction(df)
        result = list(prediction_result.T.to_dict().values())[0]
        return render_template('prediction_result.html', result=result)
    except Exception as e:
        app.logger.error(f"Error during one_prediction: {e}")
        return jsonify({'error': f"Error during prediction: {e}"})

@app.route('/batch_prediction', methods=['POST'])
def batch_prediction():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    try:
        df = pd.read_csv(file.stream, low_memory=False)
        prediction_fp = prediction.batch_prediction(df)
        return render_template('batch_prediction_result.html', prediction_path=prediction_fp.absolute().as_uri())
    except Exception as e:
        app.logger.error(f"Error during batch prediction: {e}")
        return jsonify({'error': f"Error occurred: {e}"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
