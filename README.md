<h1 align="center">⭐ Relay IDMT Calculator</h1>
<h3 align="center">Fast. Accurate. Cross-Platform IEC Trip Time Calculation.</h3>

<p align="center">
  <img src="icon.png" width="180" alt="Relay IDMT Calculator Icon">
</p>

<p align="center">
A modern desktop tool for electrical & protection engineers to instantly compute IEC relay inverse-time trip curves.<br>
Clean UI. Accurate math. Windows & Linux native builds.
</p>

<p align="center">
  <!-- Download Desktop App -->
  <a href="https://github.com/godwintgn/Relay-IDMT-Calculator/releases/latest">
    <img src="https://img.shields.io/badge/⬇️%20Download%20Desktop%20App-2ea043?style=for-the-badge">
  </a>

  <!-- Online Web Version -->
  <a href="https://godwintgn.github.io/Relay-IDMT-Calculator/">
    <img src="https://img.shields.io/badge/🌐%20Open%20Web%20Version-0078D4?style=for-the-badge">
  </a>
</p>

<p align="center">
  <a href="https://github.com/godwintgn/Relay-IDMT-Calculator/releases">
    <img src="https://img.shields.io/github/v/release/godwintgn/Relay-IDMT-Calculator?color=2ea043&label=Latest%20Release&style=for-the-badge">
  </a>

  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-0366d6?style=for-the-badge">

  <a href="https://github.com/godwintgn/Relay-IDMT-Calculator/tree/main?tab=License-1-ov-file">
    <img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-orange?style=for-the-badge">
  </a>
</p>
<style>
@media (max-width: 768px) {
  .qr-desktop-only {
    display: none;
  }
}
</style>

<p align="center" class="qr-desktop-only">
  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAuQAAALkAQAAAABv3x3IAAAEEklEQVR4nO3dS5LkSBDG4fOvNHVpW7GiWYE7hA9rGeKWJFWQyoJ7CQ0vPXYVltkR0Pcnzk2smfTdm3qdgDgFbcqccuQYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4Uw7V4bTca2Qy2h2btPpmFNttw7Hm5fd91xXMt3LZz6f4/tNMM7M8h7MYZ3Csc7ob5f8n26PjdhzHnY0uLu+4fPySYax9izt2uC+9m4HOql8tzHNsqXxz1a47Se1OLudFxOp8ONt1Glsdtnvun5JL6r8Dmx1E3Z0tLvb4ZcdZvc0ce0boon267s61cY0dv8j2DyPfe5x6v7bo+N2HMedjS4u77h8/JJhrH2LO3a4L72bgc6qXy3Mc2ypfHPVrjtJ7U4u50XE6nw423UZWx22e+6fkkvqvwObHUQ7ulYlxbv7r+IP5bBw8nruLOHuTtkW8c+Xdww2dYO0grli7Vnmt+00mNGiu3DDo6Ojo6+vl4vHsgae0+RaR7QdV5FYuVWwYdHR0dHR0dHQ0MhvLPe3kwX0v0wAAAAASUVORK5CYII=" 
       width="260" alt="QR Code to Web Version">
</p>


---

## ⚡ Overview

Relay IDMT Calculator computes IEC inverse-time relay trip durations using official IEC mathematical models.

Designed for:

- Relay & protection engineers  
- Utilities  
- Industrial facilities  
- Relay testing teams  
- Educational institutions  

The tool is completely **free & open-source** for noncommercial use.

---

## 🔢 Supported IEC Curves

- IEC Normal Inverse  
- IEC Very Inverse  
- IEC Extremely Inverse  
- IEC Long Time Inverse  

Uses input parameters:

- Pickup current  
- Fault current  
- Time Multiplier Setting (TMS)

---

## 🎨 Application Features

### Modern Desktop UI  
- Clean, compact, engineer-friendly layout  
- Light & dark theme  
- Error feedback  
- Smart numeric parsing  

### Multi-Platform Native Binaries  
- Windows EXE  
- Linux AppImage  
- Debian DEB package  
- Fedora RPM package  

### Verified Release Pipeline  
Every build is tested before publishing:
- GUI launch tests  
- Install/Uninstall checks  
- AppImage execution tests  

---

## 📥 Download

Get the latest version:

**Releases →** https://github.com/godwintgn/Relay-IDMT-Calculator/releases

Available packages:

### Windows
- `IDMT-Trip-Calculator.exe`

### Linux
- `IDMT-Trip-Calculator.AppImage`
- `idmt-trip-calculator_x.xx_amd64.deb`
- `idmt-trip-calculator-x.xx-1.x86_64.rpm`

---

## 🛠 Installation

### Windows  
Download `.exe` and run.

### Linux AppImage  
```bash
chmod +x IDMT-Trip-Calculator.AppImage
./IDMT-Trip-Calculator.AppImage
```

### Linux DEB  
```bash
sudo dpkg -i idmt-trip-calculator*.deb
```

### Linux RPM  
```bash
sudo dnf install idmt-trip-calculator*.rpm
```

---

## 👨‍💻 Developer Setup

```bash
git clone https://github.com/godwintgn/Relay-IDMT-Calculator.git
cd Relay-IDMT-Calculator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python -m idmt_tool.gui.main
```

---

## 🤖 Automated Build System

A full CI/CD workflow generates:

- Windows EXE  
- Linux AppImage  
- Linux DEB  
- Linux RPM  

Each artifact is auto-tested and uploaded to GitHub Releases.

See: `.github/workflows/release.yml`


## 👤 Author

Developed by **Godwin TGN**.  
Issues and contributions are welcome.
