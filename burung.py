class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.name = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, spesies, cara_bernafas, apa):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.spesies = spesies
        self.cara_bernafas = cara_bernafas
        self.apa = apa

    def terbang(self):
        print(f"{self.name}  seekor burung {self.spesies} sedang terbang  di udara dengan bernafas menggunakan  {self.cara_bernafas}")

    def berkicau(self):
        print(f"{self.name}  seekor burung {self.spesies} sedang terbang  di udara sambil {self.apa}")

irus = burung('irus', 'biji-bijian', 'di darat', 'bertelur', 'pipit', 'pundi-pundi udara', 'berkicauan' )
irus.terbang()
irus.berkicau()