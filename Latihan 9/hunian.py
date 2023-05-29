class Hunian():
    # Create constructor
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, image = ""):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.image = image

    # Get data
    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar
    
    def get_image(self):
        return self.image

    def get_dokumen(self):
        pass

    def get_pajak(self):
        # return "works"
        if self.jenis.__eq__("Apartemen"):
            return 100000
        elif self.jenis.__eq__("Indekos"):
            return 200000
        elif self.jenis.__eq__("Rumah"):
            return 300000
        

    def get_summary(self):
        return "Pajak: Rp " + str(self.get_pajak()) + "\n\nHunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."
    