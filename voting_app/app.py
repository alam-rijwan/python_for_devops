from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        age = int(request.form["age"])
        if age >= 18:
            result = "✅ You are eligible to vote."
        else:
            result = "❌ You are NOT eligible to vote."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)