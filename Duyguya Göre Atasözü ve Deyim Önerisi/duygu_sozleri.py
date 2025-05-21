import csv
import random
import tkinter as tk
from tkinter import messagebox, ttk

class DuyguSozleriUygulamasi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Duyguya Göre Atasözü ve Deyim Öneri Sistemi")
        self.pencere.geometry("600x400")
        self.pencere.configure(bg="#f0f0f0")
        
        # Stil ayarları
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#4CAF50")
        self.style.configure("TLabel", padding=6, background="#f0f0f0")
        
        self.veritabani_yukle()
        self.arayuz_olustur()
        
    def veritabani_yukle(self):
        self.sozler = []
        try:
            with open('veritabani.csv', 'r', encoding='utf-8') as dosya:
                okuyucu = csv.DictReader(dosya)
                for satir in okuyucu:
                    self.sozler.append(satir)
        except FileNotFoundError:
            messagebox.showerror("Hata", "Veritabanı dosyası bulunamadı!")
            self.pencere.destroy()
            
    def arayuz_olustur(self):
        # Başlık
        baslik = ttk.Label(self.pencere, text="Duyguya Göre Atasözü ve Deyim Öneri Sistemi",
                          font=("Helvetica", 16, "bold"))
        baslik.pack(pady=20)
        
        # Duygu girişi
        duygu_frame = ttk.Frame(self.pencere)
        duygu_frame.pack(pady=10)
        
        ttk.Label(duygu_frame, text="Duygunuzu girin:").pack(side=tk.LEFT, padx=5)
        self.duygu_giris = ttk.Entry(duygu_frame, width=20)
        self.duygu_giris.pack(side=tk.LEFT, padx=5)
        self.duygu_giris.bind("<Return>", lambda event: self.soz_oner())
        
        # Öneri butonu
        ttk.Button(duygu_frame, text="Öneri Al", command=self.soz_oner).pack(side=tk.LEFT, padx=5)
        
        # Sonuç alanı
        self.sonuc_frame = ttk.Frame(self.pencere)
        self.sonuc_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        self.soz_label = ttk.Label(self.sonuc_frame, text="", font=("Helvetica", 12))
        self.soz_label.pack(pady=10)
        
        self.anlam_label = ttk.Label(self.sonuc_frame, text="", font=("Helvetica", 10))
        self.anlam_label.pack(pady=10)
        
        # Başka öneri butonu
        self.baska_oneri_buton = ttk.Button(self.pencere, text="Başka Öneri Al",
                                          command=self.soz_oner, state=tk.DISABLED)
        self.baska_oneri_buton.pack(pady=10)
        
    def soz_oner(self):
        duygu = self.duygu_giris.get().lower().strip()
        if not duygu:
            messagebox.showwarning("Uyarı", "Lütfen bir duygu girin!")
            return
            
        uygun_sozler = [soz for soz in self.sozler if soz['duygu'] == duygu]
        
        if not uygun_sozler:
            messagebox.showinfo("Bilgi", f"'{duygu}' duygusuna ait öneri bulunamadı.")
            self.soz_label.config(text="")
            self.anlam_label.config(text="")
            self.baska_oneri_buton.config(state=tk.DISABLED)
            return
            
        secilen_soz = random.choice(uygun_sozler)
        self.soz_label.config(text=f"Atasözü/Deyim: {secilen_soz['atasözü_deyim']}")
        self.anlam_label.config(text=f"Anlamı: {secilen_soz['anlam']}")
        self.baska_oneri_buton.config(state=tk.NORMAL)
        
    def baslat(self):
        self.pencere.mainloop()

if __name__ == "__main__":
    uygulama = DuyguSozleriUygulamasi()
    uygulama.baslat() 