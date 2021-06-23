from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP')

pp1 = PersegiPanjang(10,3)
print(pp1.info())
print(pp1.hitung_luas())

print('\n')

sg1 = Segitiga(10,5)
print(sg1.info())
print(sg1.hitung_luas())
