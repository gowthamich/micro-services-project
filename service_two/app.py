from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/api/status")
def status():
    return jsonify(
        {
            "service": "service-two",
            "status": "running",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)