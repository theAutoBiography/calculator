from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            number1 = float(request.form["number1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = number1 + num2
            elif operation == "subtract":
                result = number1 - num2
            elif operation == "multiply":
                result = number1 * num2
            elif operation == "divide":
                result = number1 / num2 if num2 != 0 else "Error: Division by zero"

        except ValueError:
            result = "Error: Invalid input"

    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
