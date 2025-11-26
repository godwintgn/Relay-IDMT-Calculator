// Sanitize numeric input
function sanitizeNumber(value) {
    return value.replace(/[^0-9.]/g, "");
}

document.querySelectorAll("input").forEach(inp => {
    inp.addEventListener("input", () => {
        inp.value = sanitizeNumber(inp.value);
    });
});

// Shake animation
function shake(el) {
    el.classList.add("shake");
    setTimeout(() => el.classList.remove("shake"), 300);
}

// IEC math
function calculateTripTime(pickup, fault, tms, curve) {
    if (fault <= pickup) return Infinity;

    const K = {
        normal: 0.14,
        very: 13.5,
        extreme: 80,
        long: 120
    }[curve];

    const ratio = fault / pickup;
    const t = K * tms / (Math.pow(ratio, 0.02) - 1);

    return (!isFinite(t) || t <= 0) ? Infinity : t;
}

/* ------------------------
   CALCULATE BUTTON
-------------------------*/
document.getElementById("calcBtn").onclick = () => {
    const pickup = document.getElementById("pickup");
    const fault = document.getElementById("fault");
    const tms = document.getElementById("tms");
    const curve = document.getElementById("curve").value;
    const result = document.getElementById("result");

    const p = parseFloat(pickup.value);
    const f = parseFloat(fault.value);
    const t = parseFloat(tms.value);

    if (!p) { shake(pickup); return result.textContent = "Invalid pickup"; }
    if (!f) { shake(fault); return result.textContent = "Invalid fault"; }
    if (!t) { shake(tms); return result.textContent = "Invalid TMS"; }

    const trip = calculateTripTime(p, f, t, curve);

    if (trip === Infinity) {
        result.textContent = "No trip (Fault ≤ Pickup)";
        result.style.color = "#d9534f";
    } else {
        result.textContent = `Trip time: ${trip.toFixed(4)} s`;
        result.style.color = "var(--button-bg)";
    }
};

/* ------------------------
   SHARE BUTTON
-------------------------*/
document.getElementById("shareBtn").onclick = () => {
    const text = document.getElementById("result").textContent;

    if (navigator.share) {
        navigator.share({ text });
    } else {
        navigator.clipboard.writeText(text);
        alert("Result copied to clipboard!");
    }
};

/* ------------------------
   THEME TOGGLE
-------------------------*/
const toggle = document.getElementById("themeToggle");

function applyTheme(mode) {
    document.documentElement.classList.toggle("dark", mode === "dark");
    toggle.textContent = mode === "dark" ? "☀️" : "🌙";
    localStorage.setItem("theme", mode);
}

applyTheme(localStorage.getItem("theme") || "light");

toggle.onclick = () => {
    const current = document.documentElement.classList.contains("dark") ? "dark" : "light";
    applyTheme(current === "dark" ? "light" : "dark");
};
