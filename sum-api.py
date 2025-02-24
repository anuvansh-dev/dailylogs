from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api", methods= ["POST"])
def sum():
    data = request.get_json()
    a = float(dict(data)['a'])
    b = float(dict(data)['b'])

    return jsonify(a + b)

if __name__ == "__main__":
    app.run(debug=True)
