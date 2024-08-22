from flask import Flask, render_template, url_for, request
import json, random
from generate_review import Persona


app = Flask(__name__)


def generate_review_dict(service_title, service_content):
    with open("./full_persona.jsonl", "r") as f1:
        persona_dicts = [json.loads(l) for l in f1.readlines()]
        persona_index = random.randint(0, len(persona_dicts) - 1)
        persona = Persona(persona_dicts[persona_index])
        generate_persona_flag = True
        while generate_persona_flag:
            try:
                persona = Persona(persona_dicts[persona_index])
                review = persona.generate_review(service_title, service_content) #reviewはdict型, jsonで返ってくる
                generate_persona_flag = False
            except Exception as e:
                print(e)
    return review


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method == "POST":
        if request.referrer.split('/')[-1] == "":
            service_title = request.form.get('service-title')
            service_content = request.form.get('service-content')
            service_dict = {"service_title": service_title, "service_content": service_content}
            review_dict = generate_review_dict(service_title, service_content)
            return render_template("output.html", review_dict=review_dict, service_dict=service_dict)
            
        elif request.referrer.split('/')[-1] == "output":
            service_dict = json.loads(request.form.get('service_dict').replace("'", '"'))
            service_title = service_dict["service_title"]
            service_content = service_dict["service_content"]
            service_dict = {"service_title": service_title, "service_content": service_content}
            review_dict = generate_review_dict(service_title, service_content)
            return render_template("output.html", review_dict=review_dict, service_dict=service_dict)
        
        else:
            return render_template("error.html")
    else:
        return render_template("output.html", review_dict=review_dict, service_dict=service_dict)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/use_case")
def use_case():
    return render_template("use_case.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()