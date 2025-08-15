# screen_capture.py
import mss# for screen capture
import mss.tools# for saving images
from datetime import datetime# for timestamping screenshots

def capture_screenshot(save_path="live_screen.png"):
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])#monitor [1] = primary
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=save_path)
        print(f"✅ Screenshot saved to: {save_path}")