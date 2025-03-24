"""
İsim-Soyisim: Sıla Pekşen
E-mail: slpkn503@gmail.com
Github Kullanıcı Adı: silapeksen

Notlar:
-> Hazır var olan kodlardan ne anladığımı yorum satırları halinde ekleyeceğim.
"""

from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        # Her bir istasyonun özellikleri: id, isim vs.
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    # Sanırım iki istasyon arası bağlantı, süresi için.(Bir graph ın edge si)
    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))
    
    # İstasyonları karşılaştırmak için __lt__ metodu
    def __lt__(self, other: 'Istasyon'):
        return self.idx < other.idx  # İstasyon ID'sine göre sıralama


class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    # Yeni istasyon ekleme
    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    # Yeni istasyona bağlantı ekleme
    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        #1'den 2'ye ve 2'den 1'e ayrı süre, tek bağlantı
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """
        
        # İlk olarak başlangıç ve hedef istasyonlarının varlığı kontrolü gerekiyor
        # Başlangıç VEYA Hedeften herhangi biri yok ise None döndürür.
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        # Gittiğimiz yolu takip etmek için:
        # Dıştaki köşeli parantez Liste oluşturmak için
        # Normal parantez Tuple oluşturmak için
        # Parantezin solunda başlangıç, sağında ise gidilen yolun listesi bulunmakta.
        takip = [(self.istasyonlar[baslangic_id], [self.istasyonlar[hedef_id]])]

        """
        Ziyaret edilenlen istasyonların takibi istenmiş.
        Bu yüzden istasyonları bi listeye alıp kontrol edeceğim.
        """
        visited = []

        # Takip sonlanana kadar, sonlandığında 0.
        while len(takip) > 0:
            # İlk elemanı FIFO(first in first out) mantığına dayanarak x'e atadım.
            x = takip.pop(0)
            simdiki = x[0]
            topYol = x[1]
            # x tuple gibi oldu, 2 eleman

            # Hedefe ulaştığımızda total yol dönmeli.
            if simdiki == self.istasyonlar[hedef_id]:
                return topYol
            
            # Ziyaret edilmiş olanları listeme ekliyorum.
            if simdiki not in visited:
                visited.append(simdiki)
        
            for koms, _ in simdiki.komsular:
                if koms not in visited:
                    # Temp olarak yol
                    tempYol = topYol + [koms]
                    # takibe ekleme
                    takip.append((koms, tempYol))
        return None
        # End of while

    # todo ve pass i sildim     


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """

        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        # süre(top), simdiki, başlangıçtan itibaren gidilen yol
        pq = [(0, self.istasyonlar[baslangic_id], [self.istasyonlar[baslangic_id]])]

        otherVisited = set()

        while pq:
            timing, simdiki, topYol = heapq.heappop(pq)

            if simdiki == self.istasyonlar[hedef_id]:
                return topYol, timing  # En hızlı rota bulundu

            if simdiki not in otherVisited:
                otherVisited.add(simdiki)

            for komsu, eklenen_zaman in simdiki.komsular:
                if komsu not in otherVisited:
                    heapq.heappush(pq, (timing + eklenen_zaman, komsu, topYol + [komsu]))
        return None


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 