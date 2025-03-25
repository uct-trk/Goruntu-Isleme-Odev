# Piksel tabanlı ve komşuluk tabanlı işlemler arasındaki farkları açıklayınız.

# 1. Piksel Tabanlı İşlemler (Point Processing):
# ----------------------------------------------

# Tanım:
# - Her piksel, yalnızca kendi değerine göre işlenir
# - Komşu piksellerden etkilenmez
# - Piksel değeri doğrudan dönüştürülür

# Matematiksel İfade:
# Iout(x,y) = f(Iin(x,y))
# f: dönüşüm fonksiyonu (örn. parlaklık artırma, eşikleme)

# Örnekler:
# - Parlaklık ayarı
# - Kontrast germe
# - Eşikleme (thresholding)
# - Negatif alma
# - Histogram eşitleme

# Avantajlar:
# - Hızlı işlem
# - Basit hesaplama
# - Gerçek zamanlı uygulamalarda kullanılabilir
# - Paralel işleme uygun

# Dezavantajlar:
# - Kenar koruma yetersiz
# - Gürültü azaltmada etkisiz
# - Komşuluk ilişkilerini kullanmaz

# 2. Komşuluk Tabanlı İşlemler (Neighborhood Processing):
# ----------------------------------------------------

# Tanım:
# - Her piksel, kendisi ve komşularının değerlerine göre işlenir
# - Belirli bir pencere (kernel) içindeki pikseller kullanılır
# - Piksel değeri komşuluk ilişkilerine göre hesaplanır

# Matematiksel İfade:
# Iout(x,y) = f(Iin(x±i, y±j)), i,j ∈ pencere boyutu

# Örnekler:
# - Yumuşatma (smoothing)
# - Keskinleştirme (sharpening)
# - Kenar tespiti (edge detection)
# - Gürültü azaltma (noise reduction)
# - Medyan filtresi

# Avantajlar:
# - Gürültü azaltmada etkili
# - Kenar koruma özelliği
# - Daha detaylı görüntü analizi
# - Yerel özellikleri kullanır

# Dezavantajlar:
# - Daha yavaş işlem
# - Hesaplama yükü fazla
# - Sınır piksellerde özel işlem gerektirir
# - Daha karmaşık algoritmalar

# 3. Temel Farklar:
# ----------------

# İşlem Yöntemi:
# - Piksel Tabanlı: Tek piksel üzerinde işlem
# - Komşuluk Tabanlı: Piksel grubu üzerinde işlem

# Hesaplama Karmaşıklığı:
# - Piksel Tabanlı: O(n), n: piksel sayısı
# - Komşuluk Tabanlı: O(n*m), m: pencere boyutu

# Kullanım Alanları:
# - Piksel Tabanlı: Basit görüntü iyileştirme
# - Komşuluk Tabanlı: Detaylı görüntü analizi

# Sonuç Kalitesi:
# - Piksel Tabanlı: Temel iyileştirmeler
# - Komşuluk Tabanlı: Daha sofistike sonuçlar

# 4. Uygulama Örnekleri:
# ---------------------

# Piksel Tabanlı:
# - Parlaklık artırma: I_out = I_in + c
# - Kontrast artırma: I_out = a * I_in + b
# - Eşikleme: I_out = 255 if I_in > T else 0

# Komşuluk Tabanlı:
# - Gaussian blur: 3x3 veya 5x5 kernel ile yumuşatma
# - Sobel operatörü: 3x3 kernel ile kenar tespiti
# - Medyan filtre: NxN pencerede medyan değer hesaplama

# 5. Seçim Kriterleri:
# -------------------

# Piksel Tabanlı Tercih:
# - Hız önemli ise
# - Basit görüntü iyileştirme
# - Gerçek zamanlı uygulamalar
# - Sınırlı hesaplama gücü

# Komşuluk Tabanlı Tercih:
# - Kalite önemli ise
# - Gürültü azaltma gerekli
# - Kenar tespiti/koruma önemli
# - Detaylı analiz gerekli

# Piksel tabanlı ve komşuluk tabanlı işlemler arasındaki farkları tablo olarak gösterelim:

from tabulate import tabulate

# Tablo verilerini hazırlıyoruz
headers = ["Özellik", "Piksel Tabanlı İşlemler", "Komşuluk Tabanlı İşlemler"]
table = [
    ["Etki Alanı", "Tek piksel", "Piksel ve komşuları"],
    ["Kullanılan Veri", "Yalnızca mevcut piksel", "Bir filtre (kernel) ile işlem"],
    ["Hız", "Hızlı", "Nispeten yavaş"],
    ["Karmaşıklık", "Düşük", "Yüksek (filtre boyutuna bağlı)"],
    ["Uygulama Örnekleri", "Parlaklık ayarı, eşikleme", "Bulanıklaştırma, kenar tespiti"],
    ["İşlem Yöntemi", "Doğrudan piksel değeri üzerinde", "Komşu piksellerin analizi ile"],
    ["Hesaplama Yükü", "O(n)", "O(n*m), m: filtre boyutu"],
    ["Bellek Kullanımı", "Düşük", "Yüksek (filtre boyutuna bağlı)"],
    ["Gürültü Azaltma", "Etkisiz", "Etkili"],
    ["Kenar Koruma", "Yetersiz", "İyi"]
]

# Tabloyu oluştur ve yazdır
print("\nPiksel Tabanlı ve Komşuluk Tabanlı İşlemler Karşılaştırması:\n")
print(tabulate(table, headers=headers, tablefmt="grid"))

# Not: Bu kodu çalıştırmak için 'tabulate' kütüphanesinin yüklü olması gerekir
# Yüklemek için: pip install tabulate

# Çıktı örneği:
"""
+------------------+---------------------------+--------------------------------+
| Özellik         | Piksel Tabanlı İşlemler   | Komşuluk Tabanlı İşlemler     |
+==================+===========================+================================+
| Etki Alanı      | Tek piksel               | Piksel ve komşuları            |
+------------------+---------------------------+--------------------------------+
| Kullanılan Veri | Yalnızca mevcut piksel   | Bir filtre (kernel) ile işlem  |
+------------------+---------------------------+--------------------------------+
| Hız             | Hızlı                     | Nispeten yavaş                 |
+------------------+---------------------------+--------------------------------+
| Karmaşıklık     | Düşük                    | Yüksek (filtre boyutuna bağlı) |
+------------------+---------------------------+--------------------------------+
| Uygulama Örn.   | Parlaklık ayarı,eşikleme | Bulanıklaştırma,kenar tespiti |
+------------------+---------------------------+--------------------------------+
"""

# Alternatif olarak, tabulate kütüphanesi olmadan basit bir tablo gösterimi:
def print_simple_table(headers, data):
    # En uzun string uzunluklarını bul
    col_widths = []
    for i in range(len(headers)):
        col_width = max(len(str(row[i])) for row in data)
        col_width = max(col_width, len(headers[i]))
        col_widths.append(col_width)
    
    # Başlıkları yazdır
    for i, header in enumerate(headers):
        print(f"{header:<{col_widths[i]}}", end=" | ")
    print("\n" + "-" * (sum(col_widths) + len(col_widths) * 3))
    
    # Verileri yazdır
    for row in data:
        for i, item in enumerate(row):
            print(f"{str(item):<{col_widths[i]}}", end=" | ")
        print()

# Basit tabloyu yazdır
print("\nBasit Tablo Gösterimi:\n")
print_simple_table(headers, table)