#オブジェクト指向でお願いします。
import google.generativeai as genai
import json, re ,os, random
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def extract_json(text):
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    if match:
        return match.group(0)
    else:
        print("kokokokokokokokok")
        return None
    
class Persona:
    def __init__(self, persona_dict):
        self.persona_dict = persona_dict
        #self.job = persona_dict["job"]
        self.age = persona_dict["age"]
        self.gender = persona_dict["gender"]
        #self.address = persona_dict["address"]
        self.education_level = persona_dict["education_level"]
        self.family = persona_dict["family"]
        self.salary = persona_dict["salary"]
        self.health = persona_dict["health"]
        self.daily_routine = persona_dict["daily_routine"]
        self.purchasing_behavior = persona_dict["purchasing_behavior"]
        self.internet_usage = persona_dict["internet_usage"]
        self.hobbies = persona_dict["hobbies"]
        self.interests = persona_dict["interests"]
        self.values = persona_dict["values"]
        self.lifestyle = persona_dict["lifestyle"]
        self.tech_proficiency = persona_dict["tech_proficiency"]
        self.cultural_background = persona_dict["cultural_background"]
        self.current_challenges = persona_dict["current_challenges"]
        self.goals = persona_dict["goals"]
        self.needs = persona_dict["needs"]
        self.model = genai.GenerativeModel('gemini-2.0-flash-lite')

#ありきたりな感想はやめましょう！！ 良結果
    def generate_review(self, service_titile, service_content):
        magic_words = ["メタ認知", "マイノリティな視点", "珍しい視点", "使いやすさ", "コストパフォーマンス", "デザイン", "機能性", "サービスの信頼性", "顧客サポート", "スピード", "革新性", "パーソナライズ性", "直感的な操作性", "品質", "安定性", "安全性", "利便性", "持続性", "他社サービスとの比較", "効果・結果", "サービスの柔軟性", "学習曲線", "使い心地", "バグや問題の頻度", "対応範囲の広さ", "生活への影響", "モチベーションの向上", "感情的な満足度", "提供される情報の質", "コミュニティサポート", "エンターテインメント性", "社会的な影響", "長期的な価値", "アクセスのしやすさ", "アフターサービス", "使用頻度", "専門性", "カスタマイズのしやすさ", "アカウント管理のしやすさ"]
        magic_word = random.choice(magic_words)

        prompt = f"""
        {self.persona_dict}
        これはあなたのペルソナです。あなたは今から{service_titile}というサービスを利用します。サービス内容の詳細は次の通りです。{service_content}
        このサービスを利用した上でのレビューを書いてください。
        ペルソナの個性や生活スタイルを参考に、感情や体験に基づいた具体的なエピソードを含めることを重視してください。また、サービスを使って印象に残った瞬間や、特に心に残った機能、体験した感情の変化など、感情面も含めた多様な視点からレビューを行ってください。文体に変化を持たせ、他のサービスとの比較も自由に行ってください。
        （（{magic_word}））という視点を大切にしてください
        
        以下はレビューに加える内容とその出力例です。json形式で出力し、キーの内容について書き込んでください。
        {{"このサービスを使おうと思ったきっかけ": "", "良かった点": "", "悪い点": "", "総評": ""}}
        """
        print("-"*30)
        print(magic_word)
        print("-"*30)
        review = self.model.generate_content(prompt)
        review_dict = extract_json(review.text)
        return json.loads(review_dict)

"""
ChatGPTに顧客心理を考えさせたいときは「～～に帰結することが納得できる思考回路を言語化してください」と指示すると良い。
顧客の心の動きをステップごとに言語化してくれるのでマーケティングプランやセールスプランの策定に非常に役に立つ。
"""