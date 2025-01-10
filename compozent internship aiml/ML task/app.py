from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('C:/Users/User/Desktop/compozent internship aiml/ML task/netflix_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        type_value = int(request.form['type'])
        director_value = int(request.form['director'])
        country_value = int(request.form['country'])
        release_year_value = int(request.form['release_year'])
        rating_value = float(request.form['rating'])
        
        features = np.array([type_value, director_value, country_value, release_year_value, rating_value]).reshape(1, -1)
        
        predicted_title = model.predict(features)[0]
        
        return render_template('index.html', prediction=predicted_title)
    
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
