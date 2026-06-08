█▀▀ █▀▀ █▀▀ █▀█ █▄░█ ▄▀█ █▀█   BLUE TCC OVERLAY
█▄▄ █▄▄ █▄▄ █▄█ █░▀█ █▀█ █▀▄   SYSTEM PERFORMANCE HUD

───────────────────────────────────────────────
⚡ REAL-TIME SYSTEM OVERLAY (PYTHON)
───────────────────────────────────────────────

BlueTCC Overlay is a lightweight performance monitoring HUD
designed for gamers and power users.

It provides real-time system metrics directly on screen
with a minimal, transparent overlay + system tray control.

───────────────────────────────────────────────
🚀 FEATURES
───────────────────────────────────────────────

📊 LIVE SYSTEM MONITORING
- CPU Usage (%)
- RAM Usage (%)
- GPU Usage (%)
- GPU Temperature (°C)
- FPS Counter (Realtime)
- Network Ping (ms)

🪟 OVERLAY ENGINE
- Frameless transparent HUD
- Always-on-top window
- Low CPU usage design
- Gaming-friendly performance

🧭 SYSTEM TRAY CONTROL
- Show / Hide overlay
- Exit application safely
- Background running support

🎮 GAMING OPTIMIZED
- Lightweight Python architecture
- No heavy dependencies
- Suitable for fullscreen games

───────────────────────────────────────────────
🧱 REQUIREMENTS
───────────────────────────────────────────────

- Python 3.10+
- Windows 10 / 11

Python Packages:
pip install psutil ping3 pynvml GPUtil pystray pillow

───────────────────────────────────────────────
▶️ RUN PROJECT
───────────────────────────────────────────────

python overlay.py

───────────────────────────────────────────────
📦 BUILD EXECUTABLE (PRODUCTION)
───────────────────────────────────────────────

python -m PyInstaller --noconfirm --clean --onefile --windowed ^
--name "Overlay App" ^
--icon "assets/icon.ico" ^
--add-data "assets;assets" ^
overlay.py

───────────────────────────────────────────────
📁 PROJECT STRUCTURE
───────────────────────────────────────────────

BlueTCC_Overlay/
│
├── overlay.py            # Main application
├── assets/
│   └── icon.ico          # App + tray icon
├── installer.iss        # Inno Setup installer
├── run.bat              # Quick launcher
└── README.txt

───────────────────────────────────────────────
⚠️ IMPORTANT NOTES
───────────────────────────────────────────────

• If tray icon does not appear:
  → Restart Windows Explorer

• If icon missing in EXE:
  → Ensure --add-data "assets;assets"

• First run may require Administrator permission

• NVML GPU features require NVIDIA driver

───────────────────────────────────────────────
🧠 PERFORMANCE NOTES
───────────────────────────────────────────────

This overlay is designed to minimize CPU usage:
- Thread-based FPS counter
- Lightweight polling system
- 200–500ms update interval

───────────────────────────────────────────────
🔧 TROUBLESHOOTING
───────────────────────────────────────────────

TRAY NOT WORKING:
- Check pystray installation
- Run as normal user (not restricted shell)
- Restart explorer.exe

GPU NOT DETECTED:
- Install latest NVIDIA driver
- Ensure pynvml is available

ICON NOT FOUND:
- Verify assets/icon.ico exists
- Confirm PyInstaller --add-data flag

───────────────────────────────────────────────
📜 LICENSE
───────────────────────────────────────────────

MIT License © BlueTCC

───────────────────────────────────────────────
💡 FUTURE UPGRADES
───────────────────────────────────────────────

- Real-time graph overlay (CPU/GPU chart)
- Click-through mode (game overlay style)
- Hotkey toggle (F6 / F7)
- Auto-start on Windows boot
- MSI Afterburner-style UI
- In-game DX overlay support

───────────────────────────────────────────────
