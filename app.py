st.success(f"오늘의 추천 메뉴는 **{recommended_menu}** 입니다!")

components.html("""
<div id="celebration"></div>

<style>
#celebration {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    pointer-events: none;
    z-index: 999999;
}

.confetti {
    position: absolute;
    bottom: -20px;
    width: 9px;
    height: 14px;
    opacity: 0;
    animation: launch 1.8s ease-out forwards;
}

@keyframes launch {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(0.5);
        opacity: 1;
    }
    70% {
        opacity: 1;
    }
    100% {
        transform: translate(var(--drift), -85vh)
                   rotate(var(--rotation)) scale(1);
        opacity: 0;
    }
}
</style>

<script>
const container = document.getElementById("celebration");
const colors = [
    "#ff4b4b", "#ffd43b", "#51cf66",
    "#339af0", "#cc5de8", "#ff922b", "#f06595"
];

for (let i = 0; i < 100; i++) {
    const particle = document.createElement("div");
    particle.className = "confetti";

    particle.style.left = (Math.random() * 100) + "%";
    particle.style.backgroundColor =
        colors[Math.floor(Math.random() * colors.length)];

    particle.style.setProperty(
        "--drift", (Math.random() * 300 - 150) + "px"
    );

    particle.style.setProperty(
        "--rotation", (Math.random() * 1440 - 720) + "deg"
    );

    particle.style.animationDelay = (Math.random() * 0.5) + "s";

    container.appendChild(particle);
}

setTimeout(() => container.remove(), 2500);
</script>
""", height=0)