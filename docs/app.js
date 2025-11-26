// ---------------------------
// Input sanitize
// ---------------------------
document.querySelectorAll("input").forEach((inp) => {
    inp.addEventListener("input", () => {
        inp.value = inp.value.replace(/[^0-9.]/g, "");
    });
});

// Shake effect
function shake(el) {
    el.classList.add("shake");
    setTimeout(() => el.classList.remove("shake"), 300);
}

// ---------------------------
// IEC Calculation
// ---------------------------
function calculateTripTime(pickup, fault, tms, curve) {
    if (fault <= pickup) return Infinity;

    const ratio = fault / pickup;

    const curves = {
        normal:  { k: 0.14,  alpha: 0.02 },
        very:    { k: 13.5, alpha: 1 },
        extreme: { k: 80,   alpha: 2 },
        long:    { k: 120,  alpha: 1 }
    };

    const cfg = curves[curve];
    const denom = Math.pow(ratio, cfg.alpha) - 1;

    if (denom <= 0) return Infinity;

    return tms * (cfg.k / denom);
}

function format(t) {
    if (!isFinite(t)) return "No trip (I/Is ≤ 1)";
    if (t < 0.001) return t.toExponential(4) + " s";
    if (t < 1) return t.toFixed(3) + " s";
    if (t < 10) return t.toFixed(2) + " s";
    if (t < 100) return t.toFixed(1) + " s";
    return t.toFixed(0) + " s";
}

// ---------------------------
// Calculate button
// ---------------------------
document.getElementById("calcBtn").onclick = () => {
    const p = parseFloat(pickup.value);
    const f = parseFloat(fault.value);
    const t = parseFloat(tms.value);
    const type = curve.value;

    if (!p || p <= 0) { shake(pickup); result.textContent="Pickup must be > 0"; return; }
    if (!f || f <= 0) { shake(fault); result.textContent="Fault must be > 0"; return; }
    if (!t || t <= 0) { shake(tms); result.textContent="TMS must be > 0"; return; }

    const trip = calculateTripTime(p, f, t, type);
    result.textContent = "Trip time: " + format(trip);
};

// ---------------------------
// Share result
// ---------------------------
document.getElementById("shareBtn").onclick = () => {
    const text = result.textContent;
    if (navigator.share) navigator.share({ text });
    else navigator.clipboard.writeText(text);
};

// ---------------------------
// Theme toggle
// ---------------------------
const themeToggle = document.getElementById("themeToggle");

function setTheme(mode) {
    document.documentElement.setAttribute("data-theme", mode);
    localStorage.setItem("theme", mode);
    themeToggle.textContent = mode === "dark" ? "☀️" : "🌙";
}

setTheme(localStorage.getItem("theme") || "dark");

themeToggle.onclick = () => {
    const newTheme = localStorage.getItem("theme") === "dark" ? "light" : "dark";
    setTheme(newTheme);
};
