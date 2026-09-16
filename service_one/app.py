from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/api/greeting")
def greeting():
    return jsonify(
        {
            "service": "service-one",
            "message": "Hello from service one",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)