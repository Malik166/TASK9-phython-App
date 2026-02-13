from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
    return "Pipeline is working LIVE! ✅"

# Optional: for local run (not used in prod)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
=======
    return "Hello Malik enjoy.....: ! CI/CD working!"
>>>>>>> 52dc545 (trigger pipeline)
