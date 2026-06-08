import tkinter as tk
import psutil
import threading
import time
from ping3 import ping
import pynvml
import GPUtil
import sys
import pystray
from PIL import Image
import os

# =========================
# GLOBAL
# =========================
overlay = tk.Tk()
tray_icon = None

overlay.title("Overlay App")
overlay.geometry("340x220+20+20")
overlay.configure(bg="black")
overlay.overrideredirect(True)
overlay.attributes("-topmost", True)
overlay.wm_attributes("-transparentcolor", "black")

label = tk.Label(
    overlay,
    text="Loading...",
    fg="#ffb347",
    bg="black",
    font=("Consolas", 18, "bold")
)
label.pack(anchor="nw", padx=10, pady=10)

# =========================
# PATH FIX (PyInstaller)
# =========================
def resource_path(path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, path)
    return path

# =========================
# TRAY ICON
# =========================
def create_image():
    return Image.open(resource_path("assets/icon.ico"))

def hide_window(icon=None, item=None):
    overlay.after(0, overlay.withdraw)

def show_window(icon=None, item=None):
    overlay.after(0, overlay.deiconify)

def exit_app(icon=None, item=None):
    global tray_icon
    if tray_icon:
        tray_icon.stop()
    overlay.after(0, overlay.destroy)
    sys.exit()

def setup_tray():
    global tray_icon

    menu = pystray.Menu(
        pystray.MenuItem("Show", show_window),
        pystray.MenuItem("Hide", hide_window),
        pystray.MenuItem("Exit", exit_app)
    )

    tray_icon = pystray.Icon(
        "Overlay App",
        create_image(),
        "Overlay App",
        menu
    )

    tray_icon.run_detached()

# =========================
# GPU INIT
# =========================
pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0)

def get_gpu_temp():
    try:
        return pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
    except:
        return 0

def get_gpu_usage():
    try:
        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        return util.gpu
    except:
        g = GPUtil.getGPUs()
        return g[0].load * 100 if g else 0


# =========================
# FPS COUNTER (REAL TIMER)
# =========================
fps = 0
frame = 0
last = time.time()

def fps_counter():
    global fps, frame, last
    while True:
        frame += 1
        now = time.time()
        if now - last >= 1:
            fps = frame
            frame = 0
            last = now
        time.sleep(0.001)

threading.Thread(target=fps_counter, daemon=True).start()


# =========================
# PING
# =========================
def get_ping():
    try:
        p1 = ping("1.1.1.1", timeout=1)
        p2 = ping("1.0.0.1", timeout=1)

        valid = [p for p in [p1, p2] if p]
        if not valid:
            return -1

        return int(min(valid) * 1000)

    except:
        return -1


# =========================
# MAIN LOOP
# =========================
def update():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    gpu = get_gpu_usage()
    temp = get_gpu_temp()
    ping_v = get_ping()

    label.config(text=
        f"CPU : {cpu:.1f}%\n"
        f"RAM : {ram:.1f}%\n"
        f"GPU : {gpu:.1f}%\n"
        f"TEMP: {temp}°C\n"
        f"FPS : {fps}\n"
        f"PING: {ping_v if ping_v > 0 else 'N/A'} ms"
    )

    overlay.after(200, update)
# =========================
# HOTKEY EXIT
# =========================
overlay.bind("<Escape>", lambda e: exit_app())

# =========================
# START EVERYTHING (IMPORTANT ORDER)
# =========================
setup_tray()
update()
overlay.mainloop()