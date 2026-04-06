import pyautogui
import keyboard
import tkinter as tk
from PIL import ImageGrab
import os
import time

KAYIT_KLASORU = "togg_dataset"
os.makedirs(KAYIT_KLASORU, exist_ok=True)

sayac = 1
secili_bolge = None  # (x, y, length , high)


def alan_sec():
    global secili_bolge

    ekran_w = pyautogui.size().width
    ekran_h = pyautogui.size().height

    secim = {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "basili": False, "tamam": False}

    pencere = tk.Tk()
    pencere.attributes("-fullscreen", True)
    pencere.attributes("-topmost", True)
    pencere.attributes("-alpha", 0.4)
    pencere.configure(bg="black")
    pencere.overrideredirect(True)

    canvas = tk.Canvas(pencere, cursor="crosshair", bg="black",
                       width=ekran_w, height=ekran_h, highlightthickness=0)
    canvas.pack()

    tk.Label(pencere,
             text="  Araba fotosunun etrafini ciz  |  ESC = iptal  ",
             font=("Arial", 13, "bold"), fg="white", bg="#111133",
             padx=12, pady=7).place(x=ekran_w // 2, y=28, anchor="center")

    def mouse_bas(e):
        secim["x1"] = e.x
        secim["y1"] = e.y
        secim["basili"] = True

    def mouse_surukle(e):
        if secim["basili"]:
            canvas.delete("secim")
            canvas.create_rectangle(
                secim["x1"], secim["y1"], e.x, e.y,
                outline="#00ff88", width=2, fill="#00ff8815", tags="secim"
            )

    def mouse_birak(e):
        secim["x2"] = e.x
        secim["y2"] = e.y
        secim["tamam"] = True
        pencere.destroy()

    def iptal(e=None):
        pencere.destroy()

    canvas.bind("<ButtonPress-1>", mouse_bas)
    canvas.bind("<B1-Motion>", mouse_surukle)
    canvas.bind("<ButtonRelease-1>", mouse_birak)
    pencere.bind("<Escape>", iptal)
    pencere.mainloop()

    if secim["tamam"]:
        x1 = min(secim["x1"], secim["x2"])
        y1 = min(secim["y1"], secim["y2"])
        x2 = max(secim["x1"], secim["x2"])
        y2 = max(secim["y1"], secim["y2"])
        w = x2 - x1
        h = y2 - y1
        if w > 10 and h > 10:
            secili_bolge = (x1, y1, w, h)
            print(f"  Alan kaydedildi: x={x1}, y={y1}, {w}x{h} px")
            print(f"  Artik F8 ile foto cekebilirsin!")
            return True
    return False


def fotograf_cek():
    global sayac, secili_bolge

    if secili_bolge is None:
        print("\n  Alan secilmedi! Araba fotografini cercevele ;)..")
        time.sleep(0.3)
        if not alan_sec():
            print("  Iptal.")
            return

    x, y, w, h = secili_bolge
    dosya_adi = f"{KAYIT_KLASORU}/togg_t10x_{sayac:04d}.jpg"

    try:
        ekran = pyautogui.screenshot(region=(x, y, w, h))
        ekran.save(dosya_adi, "JPEG", quality=92)
        print(f"  [{sayac:04d}] Kaydedildi: {dosya_adi}")
        sayac += 1
    except Exception as e:
        print(f"  Hata: {e}")


def alani_sifirla():
    global secili_bolge
    secili_bolge = None
    print("\n  Alan sifirlandi. Bir sonraki F8'de yeniden secersin.")


print("=" * 50)
print("  TOGG T10X  |  Foto Cekici")
print("=" * 50)
print("  F8   -> Foto cek (ilk basista alan secersin)")
print("  F9   -> Alani sifirla / yeni alan sec")
print("  ESC  -> Kapat")
print(f"\n  Kayit klasoru: {os.path.abspath(KAYIT_KLASORU)}")
print("-" * 50)

keyboard.add_hotkey("f8", fotograf_cek)
keyboard.add_hotkey("f9", alani_sifirla)
keyboard.wait("esc")

print(f"\n  Toplam kaydedilen: {sayac - 1} fotograf")
print("  Kapandi.")
