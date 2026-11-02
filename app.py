import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(
    page_title="저녁 메뉴 추천기",
    page_icon="🍽️"
)

st.title("🍽️ 오늘의 저녁 메뉴 추천")
st.write("오늘 저녁 뭐 먹을지 고민된다면?")
st.write("버튼을 눌러 랜덤으로 메뉴를 추천받아 보세요!")

st.divider()

menus = {
    "한식": ["김치찌개", "불고기", "비빔밥", "제육볶음", "삼겹살"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부"],
    "일식": ["초밥", "돈카츠", "라멘", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거"]
}

category = st.selectbox(
    "어떤 종류의 음식이 먹고 싶나요?",
    ["전체"] + list(menus.keys())
)

if st.button("🎲 저녁 메뉴 추천받기"):
    if category == "전체":
        menu_list = sum(menus.values(), [])
    else:
        menu_list = menus[category]

    recommended_menu = random.choice(menu_list)

    st.success(f"오늘의 추천 메뉴는 **{recommended_menu}** 입니다!")

    components.html("""
    <style>
    .particle {
        position: fixed;
        bottom: -20px;
        width: 10px;
        height: 14px;
        z-index: 999999;
        pointer-events: none;
        animation: launch 2s ease-out forwards;
    }

    @keyframes launch {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(-700px) rotate(720deg);
            opacity: 0;
        }
    }
    </style>

    <div id="effect"></div>

    <script>
    const effect = document.getElementById("effect");
    const colors = [
        "#ff4b4b", "#ffd43b", "#51cf66",
        "#339af0", "#cc5de8", "#ff922b"
    ];

    for (let i = 0; i < 100; i++) {
        const p = document.createElement("div");
        p.className = "particle";
        p.style.left = Math.random() * 100 + "%";
        p.style.background =
            colors[Math.floor(Math.random() * colors.length)];
        p.style.animationDelay = Math.random() * 0.5 + "s";
        effect.appendChild(p);
    }
    </script>
    """, height=0)

st.divider()
st.caption("오늘도 맛있는 저녁 드세요! 😊")