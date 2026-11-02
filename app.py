import streamlit as st
import random

st.set_page_config(
    page_title="저녁 메뉴 추천기",
    page_icon="🍽️"
)

st.title("🍽️ 오늘의 저녁 메뉴 추천")
st.write("오늘 저녁 뭐 먹을지 고민된다면?")
st.write("버튼을 눌러 랜덤으로 메뉴를 추천받아 보세요!")

st.divider()

# 메뉴 목록
menus = {
    "한식": ["김치찌개", "불고기", "비빔밥", "제육볶음", "삼겹살"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부"],
    "일식": ["초밥", "돈카츠", "라멘", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거"]
}

# 음식 종류 선택
category = st.selectbox(
    "어떤 종류의 음식이 먹고 싶나요?",
    ["전체"] + list(menus.keys())
)

# 추천 버튼
if st.button("🎲 저녁 메뉴 추천받기"):

    # 선택한 종류에 따라 메뉴 목록 구성
    if category == "전체":
        menu_list = sum(menus.values(), [])
    else:
        menu_list = menus[category]

    # 메뉴 추천
    recommended_menu = random.choice(menu_list)

    st.success(f"오늘의 추천 메뉴는 **{recommended_menu}** 입니다!")

    # 파티클 효과
    st.html("""
    <style>
    .confetti-particle {
        position: fixed;
        bottom: -20px;
        width: 10px;
        height: 16px;
        border-radius: 2px;
        pointer-events: none;
        z-index: 999999;
        animation: confetti-burst 2.2s ease-out forwards;
    }

    @keyframes confetti-burst {
        0% {
            transform: translate(0, 0) rotate(0deg) scale(0.5);
            opacity: 1;
        }

        35% {
            opacity: 1;
        }

        100% {
            transform: translate(var(--drift), var(--rise))
                       rotate(var(--rotation)) scale(1);
            opacity: 0;
        }
    }
    </style>

    <div id="confetti-container"></div>

    <script>
    const container = document.getElementById("confetti-container");

    if (container) {
        const colors = [
            "#ff4b4b",
            "#ffd43b",
            "#51cf66",
            "#339af0",
            "#cc5de8",
            "#ff922b",
            "#f06595"
        ];

        // 양쪽 아래에서 위로 퍼지는 파티클 생성
        for (let i = 0; i < 120; i++) {
            const particle = document.createElement("div");

            particle.className = "confetti-particle";

            // 화면 하단의 여러 위치에서 시작
            particle.style.left = Math.random() * 100 + "vw";

            // 파티클 색상
            particle.style.backgroundColor =
                colors[Math.floor(Math.random() * colors.length)];

            // 좌우로 흩어지는 거리
            const drift = (Math.random() - 0.5) * 500;

            // 위로 솟구치는 거리
            const rise = -(50 + Math.random() * 45) + "vh";

            // 회전 각도
            const rotation = (Math.random() * 1440 - 720) + "deg";

            particle.style.setProperty("--drift", drift + "px");
            particle.style.setProperty("--rise", rise);
            particle.style.setProperty("--rotation", rotation);

            // 파티클마다 시작 시간 차이
            particle.style.animationDelay = Math.random() * 0.4 + "s";

            // 파티클 크기 차이
            const size = 6 + Math.random() * 8;
            particle.style.width = size + "px";
            particle.style.height = size * 1.5 + "px";

            container.appendChild(particle);
        }

        // 애니메이션 종료 후 파티클 제거
        setTimeout(() => {
            container.remove();
        }, 3000);
    }
    </script>
    """, unsafe_allow_javascript=True)

st.divider()

st.caption("오늘도 맛있는 저녁 드세요! 😊")