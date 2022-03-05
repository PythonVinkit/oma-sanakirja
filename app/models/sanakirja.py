from typing import List
from app.models.sana import Sana
from app.models.kayttaja import Kayttaja

class Sanakirja():

    def __init__(self, nimi: str, lahtokieli: str, paakayttaja: Kayttaja, kayttajat: List[Kayttaja]):
        self.nimi = nimi
        self.paakayttaja = paakayttaja
        self.kayttajat = kayttajat
        self.lahtokieli = lahtokieli
        self.sanat: List[Sana] = []


    def lisaa_sana(self, sana: str, kuva: str, aani: str, kielet: List[str], kaannokset: List[str]):
        self.sanat.append(Sana(self.lahtokieli, kuva, aani))
        for kieli, kaannos in zip(kielet, kaannokset):
            self.sanat[-1].lisaa_kaannos(kieli, kaannos)

    def lisaa_kaannos_sanaan(self, sana:str, kaannos:str):
        #TODO tähän koodi
        pass
