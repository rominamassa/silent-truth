from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route: your approved introduction remains in index.html
@app.route("/")
def home():
    return render_template("index.html")

# /start route: When the user clicks "Begin Investigation" on index.html,
# they are taken here. This route directly renders examine_file.html.
@app.route("/start")
def start():
    return render_template("examine_file.html")

@app.route("/examine-file")
def examine_file():
    return render_template("examine_file.html")

@app.route("/inspect-notes")
def inspect_notes():
    return render_template("inspect_notes.html")

@app.route("/question", methods=["GET", "POST"])
def question():
    if request.method == "POST":
        answer = request.form.get("answer")
        # Assuming "1" (old factory district) is the correct answer from the first question.
        if answer == "1":
            return redirect(url_for("old_factory"))
        else:
            return redirect(url_for("wrong"))
    return render_template("question.html")

@app.route("/correct")
def correct():
    return render_template("correct.html")

@app.route("/wrong")
def wrong():
    return render_template("wrong.html")

# --- Routes for the Old Factory District and Subsequent Questions ---

@app.route("/old-factory")
def old_factory():
    """
    The detective moves to the old factory district, where he notices hazardous working conditions.
    While there, he overhears someone mention 'bus line 73.'
    """
    return render_template("old_factory.html")

@app.route("/question2", methods=["GET", "POST"])
def question2():
    """
    First question in the old factory district: Identify the human right violation.
    The correct answer (option "2") corresponds to Article 23.
    """
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == "2":
            return redirect(url_for("correct2"))
        else:
            return redirect(url_for("wrong2"))
    return render_template("question2.html")

@app.route("/correct2")
def correct2():
    """
    Feedback for correctly identifying the violation.
    The page includes a link to the next question about where to continue the investigation.
    """
    return render_template("correct2.html")

@app.route("/wrong2")
def wrong2():
    return render_template("wrong2.html")

@app.route("/bus_question", methods=["GET", "POST"])
def bus_question():
    """
    Second question: Based on the overheard clue ("bus line 73"), decide where to go next.
    The correct answer is the nearby bus station.
    """
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == "1":
            return redirect(url_for("bus_correct"))
        else:
            return redirect(url_for("bus_wrong"))
    return render_template("bus_question.html")

@app.route("/bus_correct")
def bus_correct():
    return render_template("bus_correct.html")

@app.route("/bus_wrong")
def bus_wrong():
    return render_template("bus_wrong.html")

# --- Routes for the Bus Station Encounter and Human Right Min