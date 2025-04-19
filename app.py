from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    age = data.get("age")
    income = data.get("income")

    if age is None or income is None:
        return jsonify({"error": "Missing age or income"}), 400

    # Prosta reguła decyzyjna
    if age >= 18 and income >= 3000:
        decision = "Approved"
    else:
        decision = "Rejected"

    return jsonify({"decision": decision})

if __name__ == "__main__":
    app.run(debug=True)