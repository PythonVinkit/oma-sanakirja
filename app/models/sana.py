class Sana():

    def __init__(self, lahtokieli: str, kuva: str, aani: str):
        self.lahtokieli = lahtokieli
        self.kuva = kuva
        self.aani = aani
        self.kaannokset = {}


    def lisaa_kaannos(self, kieli: str, kaannos: str):
        self.kaannokset[kieli] = kaannos

    def poista_kaannos(self, kieli: str):
        self.kaannokset.pop(kieli)