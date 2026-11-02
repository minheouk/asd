st.html("""
<style>
.confetti {
    position: fixed;
    bottom: -20px;
    width: 10px;
    height: 16px;
    z-index: 999999;
    pointer-events: none;
    animation: burst 2s ease-out forwards;
}

@keyframes burst {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(0.5);
        opacity: 1;
    }
    100% {
        transform: translate(var(--drift), -85vh)
                   rotate(720deg) scale(1);
        opacity: 0;
    }
}
</style>

<div id="confetti-container"></div>

<script>
const container = document.getElementById("confetti-container");
const colors = [
    "#ff4b4b", "#ffd43b", "#51cf66",
    "#339af0", "#cc5de8", "#ff922b", "#f06595"
];

for (let i = 0; i < 100; i++) {
    const p = document.createElement("div");
    p.className = "confetti";
    p.style.left = Math.random() * 100 + "vw";
    p.style.backgroundColor =
        colors[Math.floor(Math.random() * colors.length)];
    p.style.setProperty(
        "--drift", (Math.random() * 300 - 150) + "px"
    );
    p.style.animationDelay = Math.random() * 0.5 + "s";
    container.appendChild(p);
}

setTimeout(() => container.remove(), 2500);
</script>
""", unsafe_allow_javascript=True)