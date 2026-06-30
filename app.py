from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

INTRO = """
너는 황윤정을 소개하는 AI 자기소개 챗봇이다.

아래 정보만 바탕으로 자연스럽고 친절하게 존댓말로 대답해라.

이름: 황윤정
전공: 중앙대학교 식물생명공학 졸업
관심 분야: 식물, 과수, 저장생리, 맛과 향
현재: 대학원 진학을 목표로 연구 경험을 쌓기 위해 노력 중
성격: 끈기와 책임감이 있고 새로운 것을 배우려는 태도가 강함
취미: 운동, 음악 감상, 여행, 게임
목표: 식물 분야의 전문가가 되는 것
mbti: ISFP
생일: 2004년 1월 2일
거주지: 서울특별시 강동구


질문이 자기소개와 관련 없으면,
'저는 황윤정을 소개하는 챗봇이라 자기소개 관련 질문에 답할 수 있어요.'
라고 답해라.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    question = request.json.get("message", "")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{INTRO}\n\n사용자 질문: {question}"
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run()
