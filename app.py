from flask import Flask, redirect, url_for, render_template
from routes import web_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(web_bp, url_prefix="/web")

# Root "/" → landing page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
