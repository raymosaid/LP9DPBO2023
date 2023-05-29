from hunian import Hunian

class Indekos(Hunian):
    # Create constructor
    def __init__(self, nama_pemilik, nama_penghuni, image):
        super().__init__("Indekos")
        self.jenis_hunian = "Indekos"
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.image = image

    # Get data
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_image(self):
        return self.image

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos."
    
    def get_detail(self):
        return "Jenis Hunian" + self.jenis_hunian + "\n" + "Pemilik : " + self.nama_pemilik + "\nNama Penghuni : " + self.nama_penghuni + "\n"
