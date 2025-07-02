from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    number = random.randint(1, 10)

    if request.method == "POST":
        try:
            user_guess = int(request.form["guess"])
            if user_guess == number:
                result = f" GOOD JOB! You guessed it right. (Number: {number})"
            else:
                result = f" TRY NEXT TIME! The correct number was {number}."
        except ValueError:
            result = " Please enter a valid number!"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
