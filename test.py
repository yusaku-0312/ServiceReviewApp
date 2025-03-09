from edit_pdf import make_html_file
from generate_review import Persona
import json, random, time

# review = [{"このサービスを使おうと思ったきっかけ": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "良かった点": "222", "悪い点": "333", "総評": "444"}, 
#           {"このサービスを使おうと思ったきっかけ": "aaa", "良かった点": "bbb", "悪い点": "ccc", "総評": "ddd"}, 
#           {"このサービスを使おうと思ったきっかけ": "あああ", "良かった点": "いいい", "悪い点": "ううう", "総評": "えええ"}]
# for rev in review:
#     make_html_file("abckaisya", rev)

service_title = "仮想ペルソナ事業シミュレーション"
service_content = "新規事業を仮想ペルソナが実際に体験してみる。そしてその感想を返す"
with open("./full_persona.jsonl", "r") as f1:
    persona_dicts = [json.loads(l) for l in f1.readlines()]
    
    a = 0
    while a < 10:
        persona_index = random.randint(0, len(persona_dicts) - 1)
        generate_persona_flag = True
        while generate_persona_flag:
            try:
                persona = Persona(persona_dicts[persona_index])
                review = persona.generate_review(service_title, service_content) #reviewはdict型, jsonで返ってくる
                generate_persona_flag = False
                make_html_file("abckaisya", review)
                print(service_content)
                a += 1
            except Exception as e:
                print("エラーs", e)