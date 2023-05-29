# Saya Mohammad Ray Mosaid dengan NIM 2004942 mengerjakan LP9 Praktikum DPBO dalam mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

from hunian import Hunian

class Apartemen(Hunian):
    # Create constructor
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, image):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.jenis_hunian = "Apartemen"
        self.nama_pemilik = nama_pemilik
        self.image = image
        self.sisa_kamar = 0
    
    # Get data
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_image(self):
        return self.image
    
    def get_sisa_kamar (self):
        self.sisa_kamar = self.jml_kamar - self.jml_penghuni
        if self.sisa_kamar < 0:
            self.sisa_kamar = 0
    
    def get_detail(self):
        self.get_sisa_kamar()
        return "Jenis Hunian" + self.jenis_hunian + "\n" + "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n" + "Jumlah Kamar Tersedia : " + str(self.sisa_kamar) + "\n"
