from flask import Flask, jsonify


app = Flask(__name__)

 # 1. commented out the status endpoint for service one
@app.get("/api/greeting")
def greeting():
    return jsonify(
        {
            "service": "service-one",
            "message": "Hello from service one Gowthami",
        }
    )
@app.route('/')
def home():
    return "Service One is running!"
 # 2. added a new endpoint for service one
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)