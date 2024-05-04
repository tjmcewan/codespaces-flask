"""
wrap the cli app with a gui to keep VCAA happy :/
"""

from flask import Flask, render_template, request, send_from_directory
import cli.main as CLI

app = Flask(__name__)


@app.route("/")
def index(items=None):
    """show the index page with the upload form"""
    if items is None:
        items = []
    return render_template("index.html", title="Upload", items=items)


@app.route("/upload_file", methods=["POST"])
def upload_file():
    """receive the uploaded file and call the CLI package"""
    file = request.files["file"]
    file.save(f"tmp/{file.filename}")

    items = CLI.main(f"tmp/{file.filename}")

    return index(items)


@app.route("/items-test")
def items_test():
    """for testing results display styling"""
    return index(["Octocat.png", "Octocat.png"])


@app.route("/output/<path:path>")
def output(path):
    """serve static files from output dir"""
    return send_from_directory("output", path)
