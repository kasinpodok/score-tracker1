import streamlit as st
import pyrebase

# ⚙️ Firebase config (แทนค่าด้วยของคุณเอง)
firebase_config = {
    "apiKey": "AIzaSyCWNLqU3ZEYVlPbevwiYEr4JOfP6VNzwt8",
    "authDomain": "xxx.firebaseapp.com",
    "databaseURL": "https://xxx.firebaseio.com",
    "storageBucket": "xxx.appspot.com"
}

# 🔌 เชื่อมต่อ Firebase
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# ⚠️ อ่านคะแนนจาก Firebase
scores = db.child("scores").get().val()
if not scores:
    scores = {"กลุ่ม A": 0, "กลุ่ม B": 0, "กลุ่ม C": 0}
    db.child("scores").set(scores)

# 🔍 แสดงคะแนน
st.title("📊 คะแนนกลุ่ม")
for group, score in scores.items():
    st.write(f"{group}: {score} คะแนน")

# 🔧 ควบคุมคะแนน (รหัสผ่านง่าย ๆ)
password = st.text_input("กรอกรหัสควบคุม:", type="password")
if password == "admin123":
    selected = st.selectbox("เลือกกลุ่ม", list(scores.keys()))
    if st.button("➕ เพิ่ม 1"):
        scores[selected] += 1
        db.child("scores").update({selected: scores[selected]})
    if st.button("➖ ลด 1"):
        scores[selected] -= 1
        db.child("scores").update({selected: scores[selected]})
