from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model/phishing_model.pkl')  # Load your trained model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_phishing():
    email_content = request.form['email_content']
    prediction = model.predict([email_content])
    result = 'Phishing' if prediction[0] == 1 else 'Not Phishing'
    return render_template('index.html', result=result, email_content=email_content)

if __name__ == '__main__':
    app.run(debug=True)
