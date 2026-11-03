"""Một góc nhỏ vui vẻ dành cho Thanh Phương."""

import random

import streamlit as st


st.set_page_config(page_title="Hế Lô Thanh Phương 🌷", page_icon="🌷", layout="centered")

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');
html, body, [class*="st-"], button {font-family: 'Be Vietnam Pro', sans-serif;}
.stApp {background: radial-gradient(ellipse at top left, #ffe5ee, transparent 55%),
    radial-gradient(ellipse at bottom right, #e8e0ff, transparent 55%), #fffaf5; color: #46334e;}
.block-container {max-width: 790px; padding-top: 3rem; padding-bottom: 3rem;}
.eyebrow {color: #9e5d81; font-size: .75rem; font-weight: 700; letter-spacing: .18em; text-align: center;}
.hero {text-align: center; padding: 1.6rem 0 1.4rem;}
.hero .flower {font-size: 4.2rem; display: inline-block; animation: sway 4s ease-in-out infinite;}
.hero h1 {font-size: clamp(2rem, 6vw, 3.5rem); font-weight: 800; letter-spacing: -.05em;
    color: #693c73; line-height: 1.25; margin: .5rem 0; padding: 0;}
.hero p {color: #876e8c; line-height: 1.8; font-size: .95rem;}
.letter {background: #ffffffcc; border: 1px solid #f0deeb; border-radius: 24px;
    padding: 1.7rem; box-shadow: 0 12px 35px #7d426a09; margin: 1rem 0 1.5rem; text-align: center;}
.letter small {color: #a66c88; font-size: .7rem; letter-spacing: .14em; font-weight: 700;}
.letter p {font-size: 1.12rem; line-height: 1.8; color: #654768; margin: .9rem 0 .2rem;}
.section-label {color: #76567c; font-weight: 600; margin: 1rem 0 .5rem;}
.footer {text-align: center; color: #a48da8; font-size: .75rem; margin-top: 2.5rem; line-height: 1.9;}
div.stButton > button {border-radius: 14px; min-height: 3.1rem; border-color: #ead8e9; transition: transform .15s;}
div.stButton > button:hover {transform: translateY(-2px); border-color: #bf87b3; color: #86578b;}
@keyframes sway {0%,100% {transform: rotate(-8deg);} 50% {transform: rotate(8deg);}}
@media (prefers-reduced-motion: reduce) {.hero .flower {animation: none;}}
</style>
""")

MESSAGES = (
    "Hôm nay có thể bình thường, nhưng Thanh Phương thì luôn đặc biệt. 🌷",
    "Gửi bạn một chút nắng, một chút thương và thật nhiều điều dễ mến. ☀️",
    "Không cần hoàn hảo đâu, chỉ cần là Thanh Phương thôi là đủ xinh rồi! ✨",
    "Nếu hôm nay hơi mệt, nghỉ một chút nhé. Những điều tốt đẹp vẫn đang đợi bạn. ☁️",
    "Chúc Thanh Phương gặp toàn chuyện nhỏ xíu mà vui thiệt lâu. 🍀",
    "Một chiếc ôm từ xa vừa được giao đến. Người nhận: Thanh Phương! 🧸",
)
MOODS = {
    "Vui tưng bừng ☀️": "Tuyệt quá! Cất niềm vui này vào túi, rồi mang đi khắp ngày nhé. 💛",
    "Hơi mệt một xíu ☁️": "Thả lỏng vai, uống chút nước và hít thở chậm nào. Bạn đã cố gắng nhiều rồi. 🤍",
    "Cần được yêu thương 🧸": "Gửi Thanh Phương một chiếc ôm thật ấm. Bạn xứng đáng được quan tâm. 💗",
}

if "message" not in st.session_state:
    st.session_state.message = MESSAGES[0]
if "joy" not in st.session_state:
    st.session_state.joy = 0

st.html("""
<div class="eyebrow">MỘT GÓC NHỎ, THẬT NHIỀU NIỀM VUI</div>
<div class="hero">
  <div class="flower" aria-hidden="true">🌷</div>
  <h1>Hế Lô Thanh Phương</h1>
  <p>Chào mừng bạn đến trạm sạc niềm vui.<br>Để những điều dễ thương tìm đến bạn hôm nay nhé!</p>
</div>
""")

# Render after the actions so the new message appears in the same interaction.
letter = st.empty()
left, right = st.columns(2)
with left:
    if st.button("💌 Nhận một lời dễ thương", use_container_width=True, type="primary"):
        st.session_state.message = random.choice(
            [message for message in MESSAGES if message != st.session_state.message]
        )
        st.session_state.joy += 1
with right:
    if st.button("🎈 Thả một trời bóng bay", use_container_width=True):
        st.session_state.joy += 1
        st.balloons()

letter.html(f"""
<div class="letter">
  <small>LỜI NHẮN DÀNH RIÊNG CHO BẠN</small>
  <p>{st.session_state.message}</p>
</div>
""")

st.html('<div class="section-label">Hôm nay Thanh Phương cảm thấy thế nào?</div>')
mood = st.selectbox("Chọn tâm trạng của bạn", options=list(MOODS), index=None,
                    placeholder="Chọn một chiếc tâm trạng…", label_visibility="collapsed")
if mood:
    st.info(MOODS[mood])

st.caption(f"✨ Đã gom được {st.session_state.joy} chút niềm vui trong lần ghé thăm này.")
st.html('<div class="footer">Làm bằng một chút code và rất nhiều dễ thương ♡<br>Chúc bạn một ngày dịu dàng.</div>')
