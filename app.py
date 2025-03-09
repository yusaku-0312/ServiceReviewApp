from flask import Flask, render_template, url_for, request
import json, random, time
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

# 内部用UI 
@app.route("/input")
def input():
    return render_template("my_home.html")

@app.route("/my_output", methods=["GET", "POST"])
def my_output():
    if request.method == "POST":
        company_name = request.form.get('company-name')
        service_title = request.form.get('service-title')
        service_content = request.form.get('service-content')
        generate_num = int(request.form.get('generate-number'))
        review_ls = []
        with open(f"/Users/shibayuusaku/Downloads/ServiceReviewApp/review_json/{company_name}_review.json", "w+", encoding="utf-8") as f:
            f.seek(0)  # ファイルポインタを先頭に戻す
            if f.read().strip() == "":  # ファイルが空の場合
                json_data = {"company-name": company_name, "generate-number": generate_num, "reviews": []}
            else:
                f.seek(0)  # もう一度ファイルポインタを先頭に戻してから読み込み
                #json_data = json.load(f)
            while len(review_ls) < generate_num:
                try:
                    review_dict = generate_review_dict(service_title, service_content)
                    #json_data["reviews"].append(review_dict)
                    review_ls.append(review_dict)
                    # print("-"*10, len(json_data["reviews"]) / json_data["generate_num"], "-"*10)
                except:
                    #json.dump(json_data, f, indent=3, ensure_ascii=False)
                    time.sleep(5)
        print("-"*20)
        print("-"*20)
        print("-"*20)
        for i in review_ls:
            print(i)
            # f.write(json_data)
        return render_template("my_output.html", review_ls=review_ls, company_name=company_name)
    else:
        return render_template("my_output.html", review_ls=review_ls, company_name=company_name)


if __name__ == "__main__":
    app.run()

