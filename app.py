from flask import Flask, render_template, request, redirect, jsonify, session
import pickle
import pandas as pd

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- LOAD DATASET ----------------
df = pd.read_csv("training.csv")

# Remove unwanted columns like 'Unnamed'
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Remove target column
symptom_list = [col for col in df.columns if col != "prognosis"]

print("Total symptoms:", len(symptom_list))

# ---------------- DOCTOR MAPPING ----------------
doctor_map = {
    "Fungal infection": "Dermatologist",
    "Allergy": "General Physician",
    "GERD": "Gastroenterologist",
    "Chronic cholestasis": "Hepatologist",
    "Drug Reaction": "General Physician",
    "Peptic ulcer diseae": "Gastroenterologist",
    "AIDS": "Infectious Disease Specialist",
    "Diabetes": "Endocrinologist",
    "Gastroenteritis": "Gastroenterologist",
    "Bronchial Asthma": "Pulmonologist",
    "Hypertension": "Cardiologist",
    "Migraine": "Neurologist",
    "Cervical spondylosis": "Orthopedic",
    "Paralysis (brain hemorrhage)": "Neurologist",
    "Jaundice": "Hepatologist",
    "Malaria": "General Physician",
    "Chicken pox": "General Physician",
    "Dengue": "General Physician",
    "Typhoid": "General Physician",
    "Tuberculosis": "Pulmonologist",
    "Common Cold": "General Physician",
    "Pneumonia": "Pulmonologist",
    "Heart attack": "Cardiologist",
    "Varicose veins": "Vascular Surgeon",
    "Hypothyroidism": "Endocrinologist",
    "Hyperthyroidism": "Endocrinologist",
    "Hypoglycemia": "Endocrinologist",
    "Osteoarthristis": "Orthopedic",
    "Arthritis": "Orthopedic",
    "Acne": "Dermatologist",
    "Urinary tract infection": "Urologist",
    "Psoriasis": "Dermatologist",
    "Impetigo": "Dermatologist"
}

# ---------------- USER STORAGE ----------------
users = {}

# ---------------- HOME ----------------
@app.route('/')
def home():
    return redirect('/login')

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username in users:
            return "User already exists"

        users[username] = password

        return redirect('/login')

    return render_template('register.html')

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:

            session['user'] = username

            return redirect('/dashboard')

        else:
            return "Invalid credentials"

    return render_template('login.html')

# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    return render_template(
        'dashboard.html',
        user=session['user'],
        symptoms=symptom_list
    )

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/login')

# ---------------- PREDICT ----------------
@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = request.json['symptoms']

        print("Received input length:", len(data))

        # Check input size
        if len(data) != len(symptom_list):

            return jsonify({
                "error": "Invalid input size"
            })

        # No symptoms selected
        if sum(data) == 0:

            return jsonify({
                "error": "Please select at least one symptom"
            })

        # ---------------- GET SELECTED SYMPTOMS ----------------
        selected_symptoms = [
            symptom_list[i]
            for i in range(len(data))
            if data[i] == 1
        ]

        print("Selected Symptoms:", selected_symptoms)

        # ---------------- HEART ATTACK RULE ----------------
        heart_symptoms = [
            "chest_pain",
            "fast_heart_rate",
            "breathlessness"
        ]

        # If all important heart symptoms selected
        if all(symptom in selected_symptoms for symptom in heart_symptoms):

            prediction = "Heart attack"

        else:

            # ML prediction
            prediction = model.predict([data])[0]

        # ---------------- DOCTOR RECOMMENDATION ----------------
        doctor = doctor_map.get(prediction, "General Physician")

        return jsonify({
            "disease": prediction,
            "doctor": doctor
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "error": str(e)
        })

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)