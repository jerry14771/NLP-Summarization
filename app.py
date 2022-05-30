from flask import Flask,render_template,url_for
from flask import request
import requests
import json


app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route('/Summarize',methods=["GET","POST"])

def Summarize():
    if request.method =="POST":
        headers = {"Authorization": f"Bearer Bearer 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"}
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

        data_sent = request.form["data"]

        
        maxL = int(request.form["maxL"])
        minL = maxL//4
        def query(payload):
            data = json.dumps(payload)
            response = requests.request("POST", API_URL, headers=headers, data=data)
            return json.loads(response.content.decode("utf-8"))


        

        data = query(
            {
                "inputs": data_sent,
                "parameters": {"do_sample": False, "min_length": minL, "max_length": maxL},
            }
        )

        return render_template("index.html", result = data[0]['summary_text'])
    else:
        render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()