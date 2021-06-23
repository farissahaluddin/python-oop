class PersegiPanjang():
    # fungsi yg dipanggil pertama kali
    def __init__(self, pjg, lbr):
        self.pjg = pjg
        self.lbr = lbr

    def info(self):
        return f'Modul rumus Persegi Panjang, dengan panjang {self.pjg} dan luas {self.lbr} '

    def hitung_luas(self):
        return self.pjg * self.lbr
