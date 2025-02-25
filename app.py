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

# --- Routes for the Bus Station Encounter and Human Right Mini-Case ---

@app.route("/bus_station")
def bus_station():
    """
    At the bus station, the detective meets a character who recounts an incident.
    A bus station attendant (Maria) explains that a commuter was recently refused
    boarding because of his appearance, despite having a valid ticket.
    """
    return render_template("bus_station.html")

@app.route("/bus_hr_question", methods=["GET", "POST"])
def bus_hr_question():
    """
    This route presents a question asking which human right is being violated
    by the incident described at the bus station.
    """
    if request.method == "POST":
        answer = request.form.get("answer")
        # Correct answer is assumed to be "1" (Article 13: Right to Freedom of Movement)
        if answer == "1":
            return redirect(url_for("bus_hr_correct"))
        else:
            return redirect(url_for("bus_hr_wrong"))
    return render_template("bus_hr_question.html")

@app.route("/bus_hr_correct")
def bus_hr_correct():
    """
    Feedback for correctly identifying the human right violation.
    """
    return render_template("bus_hr_correct.html")

@app.route("/bus_hr_wrong")
def bus_hr_wrong():
    """
    Feedback for an incorrect answer, prompting the player to try again.
    """
    return render_template("bus_hr_wrong.html")

# --- Routes for the Civic Center Encounter and Final Mini-Case ---

@app.route("/civic_center")
def civic_center():
    return render_template("civic_center.html")

@app.route("/civic_center_question", methods=["GET", "POST"])
def civic_center_question():
    """
    Presents the final mini-case question at the civic center.
    The protest is a demonstration of the right to freedom of expression (Article 19).
    """
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == "1":  # Correct answer: Article 19
            return redirect(url_for("civic_center_correct"))
        else:
            return redirect(url_for("civic_center_wrong"))
    return render_template("civic_center_question.html")

@app.route("/civic_center_correct")
def civic_center_correct():
    return render_template("civic_center_correct.html")

@app.route("/civic_center_wrong")
def civic_center_wrong():
    return render_template("civic_center_wrong.html")


if __name__ == "__main__":
    app.run(debug=True)
