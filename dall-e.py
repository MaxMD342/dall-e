import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from PIL import Image
import requests

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Image.create(
            prompt = animal, 
            n=1,
            size="512x512"
        )
        return redirect(url_for("index", result=response['data'][0]['url']))
    result = request.args.get("result")
    return render_template("index.html", result=result)