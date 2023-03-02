from flask import Flask, render_template, request, session
import random
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/capitals_quiz", methods=['GET', 'POST'])
def rute_capitals_quiz():
    if request.method == "GET":
        # Use RESTcountries API to get a random country
        response = requests.get("https://restcountries.com/v2/all")
        countries = response.json()
        random_country = countries[random.randint(0, len(countries)-1)]
        
        # Use RESTcountries API to get the capital of the random country
        correct_answer = random_country['capital']
        
        # Use RESTcountries API to get the names of four random countries
        country_names = []
        for i in range(4):
            country_names.append(countries[random.randint(0, len(countries)-1)]['name'])
        
        # Make sure the name of the random country is one of the answer choices
        if random_country['name'] not in country_names:
            country_names[0] = random_country['name']
        
        # Use RESTcountries API to get the capitals of the four random countries
        capitals = []
        for country_name in country_names:
            response = requests.get(f"https://restcountries.com/v2/name/{country_name}")
            capital = response.json()[0]['capital']
            capitals.append(capital)
        
        # Shuffle the list of answer choices so they're not always in the same order
        random.shuffle(capitals)
        
        # Render the quiz template with the question and answer choices
        return render_template("capitals_quiz.html", question=random_country['name'], 
                               answer_choices=capitals)
    else:
        # Get the user's answer from the form submission
        user_answer = request.form['answer']
        
        # Use RESTcountries API to get the correct answer
        response = requests.get(f"https://restcountries.com/v2/name/{request.form['question']}")
        correct_answer = response.json()[0]['capital']
        
        # Check if the user's answer is correct and return the appropriate message
        if user_answer == correct_answer:
            message = "Correct!"
        else:
            message = "Feil!"
        
        # Render the results template with the user's answer and the appropriate message
        return render_template("results.html", user_answer=user_answer, message=message)




@app.route("/flag_quiz")
def rute_flag_quiz():
    return render_template("flag_quiz.html")

@app.route("/domains_quiz")
def rute_domains_quiz():
    return render_template("domains_quiz.html")

@app.route("/mix_quiz")
def rute_mix_quiz():
    return render_template("mix_quiz.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)