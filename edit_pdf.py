import os
#ファイル作成
def make_html_file(company_name,review_data):
    dir_path = "/Users/shibayuusaku/Downloads/ServiceReviewApp/review_data"
    index = len(os.listdir(dir_path))
    file_name = company_name + f"00{index+1}.html"
    file_path = os.path.join(dir_path, file_name)
    if index == 0:
        header = "<h1>Experience Simulation</h1>"
    else:
        header="ggggg"
    #繰り返し呼び出すなら、ファイル名にインデックス打たないと上書きされ続けて、HTMLファイルが一個しかできない
    with open(file_path, "w") as f:
        html = f"""
            <!DOCTYPE html>
            <html lang="ja">
                <head>
                    <meta charset="utf-8">
                    <title>Experience Simulation</title>
                    <style>
                        body {{
                            width: 700px;
                            height: 900px;
                            margin: 10px, 20px;
                            padding: 0;
                            font-family: Arial, sans-serif;
                            background-color: #ffffff;
                        }}
                        .header {{
                            height: 100px;
                        }}
                        .container {{
                            height: 700px;
                            margin: 0px 10px; 
                            overflow: hidden;        /* はみ出た部分を隠す */
                            word-wrap: break-word;    
                        }}
                        .container-key {{
                            text-align: center;
                        }}
                        h1 {{
                            text-align: center;
                            color: black;
                        }}
                        p {{
                            text-align: center;
                            color: #666;
                        }}
                    </style>
                </head>
                <body>
                    <div class="header">
                        <h1>{header}</h1>
                    </div>
                    <div class="container">
                        <h3 class="container-key">"このサービスを使おうと思ったきっかけ"</h3>
                        {review_data["このサービスを使おうと思ったきっかけ"]}
                        <h3 class="container-key">"良かった点"</h3>
                        {review_data["良かった点"]}
                        <h3 class="container-key">"悪い点"</h3>
                        {review_data["悪い点"]}
                        <h3 class="container-key">"総評"</h3>
                        {review_data["総評"]}
                    </div>
                </body>
            </html>
        """
        f.write(html)
