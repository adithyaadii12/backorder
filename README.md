# Backorder_prediction

***Overview***

The Backorder Prediction System is an end-to-end machine learning project designed to predict which products are at risk of going on backorder. By leveraging historical sales and inventory data, this model helps businesses manage their stock more efficiently, reducing the chances of running out of products and improving customer satisfaction.

This project covers everything from data collection and preprocessing to model development, evaluation, and deployment.

Prediction: The system will preprocess the data and use the trained model to predict which products are at risk of going on backorder.
Results: The results are displayed as a table with a column indicating whether a product is likely to go on backorder (Yes/No).

***Model training pipeline***
Data Collection: Historical sales, inventory, and supplier data are collected.
Data Preprocessing: Missing values are handled, categorical variables are encoded, and data is normalized.
Feature Engineering: New features are created from the raw data to enhance the predictive power of the model.
Model Training: Various machine learning algorithms (e.g., Random Forest, decision tree ) are trained, and hyperparameters are optimized using cross-validation.
Model Evaluation: Models are evaluated using metrics such as Model accuracy, training score , test score.
Model Saving: The best-performing model is saved for deployment.

The application is deployed using Flask and can be containerized with Docker. Continuous Integration/Continuous Delivery (CI/CD) pipelines are set up with GitHub Actions.

***Results***
Model accuracy : 95.63%
Train score: 0.99901
Tests score: 0.9985
