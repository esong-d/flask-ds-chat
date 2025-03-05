import json
from flask import Flask, render_template, request, Response
from flask_cors import CORS

from deepseek_ai import DeepSeekAI

app = Flask(__name__)

CORS(app, supports_credentials=True)

client = DeepSeekAI(api_key="sk-ea07a76abe5d40ea9afe01fb869427dd")


def chat_response(model, messages):
    response = client.chat(model, messages)
    if not response:
        yield "请求失败"
        
    for chunk in response:
        yield chunk.choices[0].delta.content


@app.route('/chat', methods=['POST'])
def index():
    data = request.get_json()
    model = data.get("model")
    messages = data.get("messages")
    # 流式响应
    return Response(chat_response(model, messages), content_type='text/plain; charset=utf-8')

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)