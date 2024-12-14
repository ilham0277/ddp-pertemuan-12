class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.name = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class Ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, spesies, cara_bergerak, apa):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.spesies = spesies
        self.cara_bergerak = cara_bergerak
        self.apa = apa


    def berjalan(self):
        print(f"{self.name} berjalan dengan cara {self.cara_bergerak} di atas tanah")

    def mematuk(self):
        print(f"seseorang telah dipatuk oleh seekor ular ({self.name}) yang berbisa")

iris = Ular('iris', 'daging', 'di darat', 'bertelur', 'kadut', 'melata', 'berkicauan' )
iris.berjalan()
iris.mematuk()