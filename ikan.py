class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.name = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, jenis_makanan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.jenis_makanan = jenis_makanan

    def berenang(self):
        print(f"{self.name} seekor ikan  {self.jenis} sedang berenang  {self.hidup} ")

    def makan(self):
        print(f"{self.name} seekor ikan  {self.jenis} sedang memakan {self.jenis_makanan}")


loly = ikan('loly','pelet','di air', 'bertelur', 'koi', 'pelet')
loly.berenang()
loly.makan()