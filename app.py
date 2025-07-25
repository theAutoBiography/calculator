from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            number2 = float(request.form["number2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + number2
            elif operation == "subtract":
                result = num1 - number2
            elif operation == "multiply":
                result = num1 * number2
            elif operation == "divide":
                result = num1 / number2 if number2 != 0 else "Error: Division by zero"
        except ValueError:
            result = "Error: Invalid input"

    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
