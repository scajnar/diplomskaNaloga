from selenium.webdriver.common.by import By

from elements.button import Button
from elements.dropdown import HeaderDropdown


class OFakultetiDropdown(HeaderDropdown):
    # xpath = './/ul[contains(@class, "menu-level2") and contains(@style, "display: block")]'

    def __init__(self, element):
        super().__init__(element)
        self.o_fakulteti_text = 'O fakulteti'
        self.fakulteta_text = 'Fakulteta'
        self.predstavitev_text = 'Predstavitev'
        self.poslanstvo_in_vizija_text = 'Poslanstvo in vizija'
        self.zgodovina_text = 'Zgodovina'
        self.katedre_in_laboratoriji_text = 'Katedre in laboratoriji'
        self.organiziranost_fakultete_text = 'Organiziranost fakultete'
        self.vodstvo_text = 'Vodstvo'
        self.senat_text = 'Senat'
        self.akademski_zbor_text = 'Akademski zbor'
        self.upravni_odbor_text = 'Upravni odbor'
        self.predstojniki_kateder_text = 'Predstojniki kateder'
        self.skupne_sluzbe_text = 'Skupne službe'
        self.katalog_ijz_text = 'Katalog IJZ'
        self.kje_smo_text = 'Kje smo'
        self.medijsko_sredisce_text = 'Medijsko središče'
        self.vizitka_text = 'Vizitka'
        self.predstavitvene_brosure_text = 'Predstavitvene brošure'
        self.celostna_graficna_podoba_text = 'Celostna grafična podoba'
        self.prostori_fakultete_text = 'Prostori fakultete'
        self.cenik_najema_prostorov_text = 'Cenik najema prostorov'
        self.nacrt_prostorov_text = 'Načrt prostorov'
        self.dokumenti_text = 'Dokumenti'
        self.porocila_text = 'Poročila'
        self.pravilniki_text = 'Pravilniki'
        self.habilitacije_text = 'Habilitacije'
        self.varstvo_osebnih_podatkov_text = 'Varstvo osebnih podatkov'
        self.zaupna_oseba_text = 'Zaupna oseba'
        self.zalozba_in_trgovina_text = 'Založba in trgovina'
        self.cenik_knjig_text = 'Cenik knjig '  # Space after string is correct in this case
        self.seznam_literature_text = 'Seznam literature'
        self.cenik_promocijskih_artiklov_text = 'Cenik promocijskih artiklov'
        self.delovni_cas_in_kontakt_text = 'Delovni čas in kontakt'
        self.restavracija_text = 'Restavracija'
        self.tedenski_meni_text = 'Tedenski meni'
        self.cenik_bife_text = 'Cenik bife'
        self.cenik_jedi_in_menijev_text = 'Cenik jedi in menijev'
        self.delovni_cas_in_kontakt_text = 'Delovni čas in kontakt'
        self.knjiznica_text = 'Knjižnica'
        self.o_knjiznici_text = 'O knjižnici'
        self.izposoja_text = 'Izposoja'
        self.e_knjiznica_text = 'E-knjižnica'
        self.bibliografije_raziskovalcev_text = 'Bibliografije raziskovalcev'
        self.digitalne_storitve_text = 'Digitalne storitve'
        self.uporabniski_koticek_text = 'Uporabniški kotiček'
        self.navajanje_virov_text = 'Navajanje virov'
        self.cenik_knjiznicnih_storitev_text = 'Cenik knjižničnih storitev'
        self.imenik_zaposlenih_text = 'Imenik zaposlenih'
        self.po_abecedi_text = 'Po abecedi'
        self.redni_profesorji_text = 'Redni profesorji'
        self.izredni_profesorji_text = 'Izredni profesorji'
        self.docenti_text = 'Docenti'
        self.predavatelji_in_visji_predavatelji_text = 'Predavatelji in višji predavatelji'
        self.asistenti_text = 'Asistenti'
        self.tehniski_sodelavci_text = 'Tehniški sodelavci'
        self.raziskovalci_text = 'Raziskovalci'
        self.ostale_sluzbe_text = 'Ostale službe'
        self.zunanji_sodelavci_text = 'Zunanji sodelavci'
        self.upokojeni_profesorji_text = 'Upokojeni profesorji'
        self.telefonija_uporabniska_pomoc_text = 'Telefonija – uporabniška pomoč'
        self.nagrade_in_priznanja_text = 'Nagrade in priznanja'
        self.vidmarjeve_nagrade_text = 'Vidmarjeve nagrade'
        self.vodovnikove_nagrade_text = 'Vodovnikove nagrade'
        self.presernove_nagrade_text = 'Prešernove nagrade'
        self.priznanje_poslovnim_partnerjem_text = 'Priznanje poslovnim partnerjem'
        self.nagrada_sodelavcem_fakultete_text = 'Nagrada sodelavcem fakultete'
        self.dekanove_pohvale_studentom_text = 'Dekanove pohvale študentom'
        self.univerzitetna_priznanja_text = 'Univerzitetna priznanja'
        self.drzavne_nagrade_in_priznanja_text = 'Državne nagrade in priznanja'
        self._100fe_text = '100FE'
        self.zgodovina_text = 'Zgodovina'
        self.slovesna_akademija_text = 'Slovesna akademija'
        self.zbornik_text = 'Zbornik'
        self.intervjuji_text = 'Intervjuji'
        self.casovna_kapsula_text = 'Časovna kapsula'

        self.o_fakulteti_xpath = self.menu_level1_xpath.format(text=self.o_fakulteti_text)
        self.fakulteta_xpath = self.menu_level2_xpath.format(text=self.fakulteta_text)
        self.predstavitev_xpath = self.menu_level3_xpath.format(text=self.predstavitev_text)
        self.poslanstvo_in_vizija_xpath = self.menu_level3_xpath.format(text=self.poslanstvo_in_vizija_text)
        self.zgodovina_xpath = self.menu_level3_xpath.format(text=self.zgodovina_text)
        self.katedre_in_laboratoriji_xpath = self.menu_level3_xpath.format(text=self.katedre_in_laboratoriji_text)
        self.organiziranost_fakultete_xpath = self.menu_level3_xpath.format(text=self.organiziranost_fakultete_text)
        self.vodstvo_xpath = self.menu_level4_xpath.format(text=self.vodstvo_text)
        self.senat_xpath = self.menu_level4_xpath.format(text=self.senat_text)
        self.akademski_zbor_xpath = self.menu_level4_xpath.format(text=self.akademski_zbor_text)
        self.upravni_odbor_xpath = self.menu_level4_xpath.format(text=self.upravni_odbor_text)
        self.predstojniki_kateder_xpath = self.menu_level4_xpath.format(text=self.predstojniki_kateder_text)
        self.skupne_sluzbe_xpath = self.menu_level4_xpath.format(text=self.skupne_sluzbe_text)
        self.katalog_ijz_xpath = self.menu_level3_xpath.format(text=self.katalog_ijz_text)
        self.kje_smo_xpath = self.menu_level3_xpath.format(text=self.kje_smo_text)
        self.medijsko_sredisce_xpath = self.menu_level3_xpath.format(text=self.medijsko_sredisce_text)
        self.vizitka_xpath = self.menu_level4_xpath.format(text=self.vizitka_text)
        self.predstavitvene_brosure_xpath = self.menu_level4_xpath.format(text=self.predstavitvene_brosure_text)
        self.celostna_graficna_podoba_xpath = self.menu_level4_xpath.format(text=self.celostna_graficna_podoba_text)
        self.prostori_fakultete_xpath = self.menu_level4_xpath.format(text=self.prostori_fakultete_text)
        self.cenik_najema_prostorov_xpath = self.menu_level3_xpath.format(text=self.cenik_najema_prostorov_text)
        self.nacrt_prostorov_xpath = self.menu_level3_xpath.format(text=self.nacrt_prostorov_text)
        self.dokumenti_xpath = self.menu_level3_xpath.format(text=self.dokumenti_text)
        self.porocila_xpath = self.menu_level4_xpath.format(text=self.porocila_text)
        self.pravilniki_xpath = self.menu_level4_xpath.format(text=self.pravilniki_text)
        self.habilitacije_xpath = self.menu_level4_xpath.format(text=self.habilitacije_text)
        self.varstvo_osebnih_podatkov_xpath = self.menu_level3_xpath.format(text=self.varstvo_osebnih_podatkov_text)
        self.zaupna_oseba_xpath = self.menu_level3_xpath.format(text=self.zaupna_oseba_text)
        self.zalozba_in_trgovina_xpath = self.menu_level2_xpath.format(text=self.zalozba_in_trgovina_text)
        self.cenik_knjig_xpath = self.menu_level3_xpath.format(text=self.cenik_knjig_text)
        self.seznam_literature_xpath = self.menu_level3_xpath.format(text=self.seznam_literature_text)
        self.cenik_promocijskih_artiklov_xpath = self.menu_level3_xpath.format(
            text=self.cenik_promocijskih_artiklov_text)
        self.delovni_cas_in_kontakt_xpath = self.menu_level3_xpath.format(text=self.delovni_cas_in_kontakt_text)
        self.restavracija_xpath = self.menu_level2_xpath.format(text=self.restavracija_text)
        self.tedenski_meni_xpath = self.menu_level3_xpath.format(text=self.tedenski_meni_text)
        self.cenik_bife_xpath = self.menu_level3_xpath.format(text=self.cenik_bife_text)
        self.cenik_jedi_in_menijev_xpath = self.menu_level3_xpath.format(text=self.cenik_jedi_in_menijev_text)
        self.delovni_cas_in_kontakt_xpath = self.menu_level3_xpath.format(text=self.delovni_cas_in_kontakt_text)
        self.knjiznica_xpath = self.menu_level2_xpath.format(text=self.knjiznica_text)
        self.o_knjiznici_xpath = self.menu_level3_xpath.format(text=self.o_knjiznici_text)
        self.izposoja_xpath = self.menu_level3_xpath.format(text=self.izposoja_text)
        self.e_knjiznica_xpath = self.menu_level3_xpath.format(text=self.e_knjiznica_text)
        self.bibliografije_raziskovalcev_xpath = self.menu_level3_xpath.format(
            text=self.bibliografije_raziskovalcev_text)
        self.digitalne_storitve_xpath = self.menu_level3_xpath.format(text=self.digitalne_storitve_text)
        self.uporabniski_koticek_xpath = self.menu_level3_xpath.format(text=self.uporabniski_koticek_text)
        self.navajanje_virov_xpath = self.menu_level3_xpath.format(text=self.navajanje_virov_text)
        self.cenik_knjiznicnih_storitev_xpath = self.menu_level3_xpath.format(text=self.cenik_knjiznicnih_storitev_text)
        self.imenik_zaposlenih_xpath = self.menu_level2_xpath.format(text=self.imenik_zaposlenih_text)
        self.po_abecedi_xpath = self.menu_level3_xpath.format(text=self.po_abecedi_text)
        self.redni_profesorji_xpath = self.menu_level3_xpath.format(text=self.redni_profesorji_text)
        self.izredni_profesorji_xpath = self.menu_level3_xpath.format(text=self.izredni_profesorji_text)
        self.docenti_xpath = self.menu_level3_xpath.format(text=self.docenti_text)
        self.predavatelji_in_visji_predavatelji_xpath = self.menu_level3_xpath.format(
            text=self.predavatelji_in_visji_predavatelji_text)
        self.asistenti_xpath = self.menu_level3_xpath.format(text=self.asistenti_text)
        self.tehniski_sodelavci_xpath = self.menu_level3_xpath.format(text=self.tehniski_sodelavci_text)
        self.raziskovalci_xpath = self.menu_level3_xpath.format(text=self.raziskovalci_text)
        self.ostale_sluzbe_xpath = self.menu_level3_xpath.format(text=self.ostale_sluzbe_text)
        self.zunanji_sodelavci_xpath = self.menu_level3_xpath.format(text=self.zunanji_sodelavci_text)
        self.upokojeni_profesorji_xpath = self.menu_level3_xpath.format(text=self.upokojeni_profesorji_text)
        self.telefonija_uporabniska_pomoc_xpath = self.menu_level3_xpath.format(
            text=self.telefonija_uporabniska_pomoc_text)
        self.nagrade_in_priznanja_xpath = self.menu_level2_xpath.format(text=self.nagrade_in_priznanja_text)
        self.vidmarjeve_nagrade_xpath = self.menu_level3_xpath.format(text=self.vidmarjeve_nagrade_text)
        self.vodovnikove_nagrade_xpath = self.menu_level3_xpath.format(text=self.vodovnikove_nagrade_text)
        self.presernove_nagrade_xpath = self.menu_level3_xpath.format(text=self.presernove_nagrade_text)
        self.priznanje_poslovnim_partnerjem_xpath = self.menu_level3_xpath.format(
            text=self.priznanje_poslovnim_partnerjem_text)
        self.nagrada_sodelavcem_fakultete_xpath = self.menu_level3_xpath.format(
            text=self.nagrada_sodelavcem_fakultete_text)
        self.dekanove_pohvale_studentom_xpath = self.menu_level3_xpath.format(text=self.dekanove_pohvale_studentom_text)
        self.univerzitetna_priznanja_xpath = self.menu_level3_xpath.format(text=self.univerzitetna_priznanja_text)
        self.drzavne_nagrade_in_priznanja_xpath = self.menu_level3_xpath.format(
            text=self.drzavne_nagrade_in_priznanja_text)
        self._100fe_xpath = self.menu_level2_xpath.format(text=self._100fe_text)
        self.zgodovina_xpath = self.menu_level3_xpath.format(text=self.zgodovina_text)
        self.slovesna_akademija_xpath = self.menu_level3_xpath.format(text=self.slovesna_akademija_text)
        self.zbornik_xpath = self.menu_level3_xpath.format(text=self.zbornik_text)
        self.intervjuji_xpath = self.menu_level3_xpath.format(text=self.intervjuji_text)
        self.casovna_kapsula_xpath = self.menu_level3_xpath.format(text=self.casovna_kapsula_text)

        self.o_fakulteti_button = ...
        self.fakulteta_button = ...
        self.predstavitev_button = ...
        self.poslanstvo_in_vizija_button = ...
        self.zgodovina_button = ...
        self.katedre_in_laboratoriji_button = ...
        self.organiziranost_fakultete_button = ...
        self.vodstvo_button = ...
        self.senat_button = ...
        self.akademski_zbor_button = ...
        self.upravni_odbor_button = ...
        self.predstojniki_kateder_button = ...
        self.skupne_sluzbe_button = ...
        self.katalog_ijz_button = ...
        self.kje_smo_button = ...
        self.medijsko_sredisce_button = ...
        self.vizitka_button = ...
        self.predstavitvene_brosure_button = ...
        self.celostna_graficna_podoba_button = ...
        self.prostori_fakultete_button = ...
        self.cenik_najema_prostorov_button = ...
        self.nacrt_prostorov_button = ...
        self.dokumenti_button = ...
        self.porocila_button = ...
        self.pravilniki_button = ...
        self.habilitacije_button = ...
        self.varstvo_osebnih_podatkov_button = ...
        self.zaupna_oseba_button = ...
        self.zalozba_in_trgovina_button = ...
        self.cenik_knjig_button = ...
        self.seznam_literature_button = ...
        self.cenik_promocijskih_artiklov_button = ...
        self.delovni_cas_in_kontakt_button = ...
        self.restavracija_button = ...
        self.tedenski_meni_button = ...
        self.cenik_bife_button = ...
        self.cenik_jedi_in_menijev_button = ...
        self.delovni_cas_in_kontakt_button = ...
        self.knjiznica_button = ...
        self.o_knjiznici_button = ...
        self.izposoja_button = ...
        self.e_knjiznica_button = ...
        self.bibliografije_raziskovalcev_button = ...
        self.digitalne_storitve_button = ...
        self.uporabniski_koticek_button = ...
        self.navajanje_virov_button = ...
        self.cenik_knjiznicnih_storitev_button = ...
        self.imenik_zaposlenih_button = ...
        self.po_abecedi_button = ...
        self.redni_profesorji_button = ...
        self.izredni_profesorji_button = ...
        self.docenti_button = ...
        self.predavatelji_in_visji_predavatelji_button = ...
        self.asistenti_button = ...
        self.tehniski_sodelavci_button = ...
        self.raziskovalci_button = ...
        self.ostale_sluzbe_button = ...
        self.zunanji_sodelavci_button = ...
        self.upokojeni_profesorji_button = ...
        self.telefonija_uporabniska_pomoc_button = ...
        self.nagrade_in_priznanja_button = ...
        self.vidmarjeve_nagrade_button = ...
        self.vodovnikove_nagrade_button = ...
        self.presernove_nagrade_button = ...
        self.priznanje_poslovnim_partnerjem_button = ...
        self.nagrada_sodelavcem_fakultete_button = ...
        self.dekanove_pohvale_studentom_button = ...
        self.univerzitetna_priznanja_button = ...
        self.drzavne_nagrade_in_priznanja_button = ...
        self._100fe_button = ...
        self.zgodovina_button = ...
        self.slovesna_akademija_button = ...
        self.zbornik_button = ...
        self.intervjuji_button = ...
        self.casovna_kapsula_button = ...






        ####
        self.fakulteta_text = 'Fakulteta'
        self.predstavitev_text = 'Predstavitev'
        self.poslanstvo_in_vizija_text = 'Poslanstvo in vizija'
        self.zgodovina_text = 'Zgodovovina'

        self.fakulteta_xpath = self.menu_level2_xpath.format(text=self.fakulteta_text)
        self.predstavitev_xpath = self.menu_level3_xpath.format(text=self.predstavitev_text)
        self.fakulteta_button: 'Button' = ...
        self.predstavitev_button: 'Button' = ...

    def init_expanded(self):
        self.o_fakulteti_button = Button(self.find_element(By.XPATH, self.o_fakulteti_xpath))
        self.fakulteta_button = Button(self.find_element(By.XPATH, self.fakulteta_xpath))
        self.predstavitev_button = Button(self.find_element(By.XPATH, self.predstavitev_xpath))
        self.poslanstvo_in_vizija_button = Button(self.find_element(By.XPATH, self.poslanstvo_in_vizija_xpath))
        self.zgodovina_button = Button(self.find_element(By.XPATH, self.zgodovina_xpath))
        self.katedre_in_laboratoriji_button = Button(self.find_element(By.XPATH, self.katedre_in_laboratoriji_xpath))
        self.organiziranost_fakultete_button = Button(self.find_element(By.XPATH, self.organiziranost_fakultete_xpath))
        self.vodstvo_button = Button(self.find_element(By.XPATH, self.vodstvo_xpath))
        self.senat_button = Button(self.find_element(By.XPATH, self.senat_xpath))
        self.akademski_zbor_button = Button(self.find_element(By.XPATH, self.akademski_zbor_xpath))
        self.upravni_odbor_button = Button(self.find_element(By.XPATH, self.upravni_odbor_xpath))
        self.predstojniki_kateder_button = Button(self.find_element(By.XPATH, self.predstojniki_kateder_xpath))
        self.skupne_sluzbe_button = Button(self.find_element(By.XPATH, self.skupne_sluzbe_xpath))
        self.katalog_ijz_button = Button(self.find_element(By.XPATH, self.katalog_ijz_xpath))
        self.kje_smo_button = Button(self.find_element(By.XPATH, self.kje_smo_xpath))
        self.medijsko_sredisce_button = Button(self.find_element(By.XPATH, self.medijsko_sredisce_xpath))
        self.vizitka_button = Button(self.find_element(By.XPATH, self.vizitka_xpath))
        self.predstavitvene_brosure_button = Button(self.find_element(By.XPATH, self.predstavitvene_brosure_xpath))
        self.celostna_graficna_podoba_button = Button(self.find_element(By.XPATH, self.celostna_graficna_podoba_xpath))
        self.prostori_fakultete_button = Button(self.find_element(By.XPATH, self.prostori_fakultete_xpath))
        self.cenik_najema_prostorov_button = Button(self.find_element(By.XPATH, self.cenik_najema_prostorov_xpath))
        self.nacrt_prostorov_button = Button(self.find_element(By.XPATH, self.nacrt_prostorov_xpath))
        self.dokumenti_button = Button(self.find_element(By.XPATH, self.dokumenti_xpath))
        self.porocila_button = Button(self.find_element(By.XPATH, self.porocila_xpath))
        self.pravilniki_button = Button(self.find_element(By.XPATH, self.pravilniki_xpath))
        self.habilitacije_button = Button(self.find_element(By.XPATH, self.habilitacije_xpath))
        self.varstvo_osebnih_podatkov_button = Button(self.find_element(By.XPATH, self.varstvo_osebnih_podatkov_xpath))
        self.zaupna_oseba_button = Button(self.find_element(By.XPATH, self.zaupna_oseba_xpath))
        self.zalozba_in_trgovina_button = Button(self.find_element(By.XPATH, self.zalozba_in_trgovina_xpath))
        self.cenik_knjig_button = Button(self.find_element(By.XPATH, self.cenik_knjig_xpath))
        self.seznam_literature_button = Button(self.find_element(By.XPATH, self.seznam_literature_xpath))
        self.cenik_promocijskih_artiklov_button = Button(
            self.find_element(By.XPATH, self.cenik_promocijskih_artiklov_xpath))
        self.delovni_cas_in_kontakt_button = Button(self.find_element(By.XPATH, self.delovni_cas_in_kontakt_xpath))
        self.restavracija_button = Button(self.find_element(By.XPATH, self.restavracija_xpath))
        self.tedenski_meni_button = Button(self.find_element(By.XPATH, self.tedenski_meni_xpath))
        self.cenik_bife_button = Button(self.find_element(By.XPATH, self.cenik_bife_xpath))
        self.cenik_jedi_in_menijev_button = Button(self.find_element(By.XPATH, self.cenik_jedi_in_menijev_xpath))
        self.delovni_cas_in_kontakt_button = Button(self.find_element(By.XPATH, self.delovni_cas_in_kontakt_xpath))
        self.knjiznica_button = Button(self.find_element(By.XPATH, self.knjiznica_xpath))
        self.o_knjiznici_button = Button(self.find_element(By.XPATH, self.o_knjiznici_xpath))
        self.izposoja_button = Button(self.find_element(By.XPATH, self.izposoja_xpath))
        self.e_knjiznica_button = Button(self.find_element(By.XPATH, self.e_knjiznica_xpath))
        self.bibliografije_raziskovalcev_button = Button(
            self.find_element(By.XPATH, self.bibliografije_raziskovalcev_xpath))
        self.digitalne_storitve_button = Button(self.find_element(By.XPATH, self.digitalne_storitve_xpath))
        self.uporabniski_koticek_button = Button(self.find_element(By.XPATH, self.uporabniski_koticek_xpath))
        self.navajanje_virov_button = Button(self.find_element(By.XPATH, self.navajanje_virov_xpath))
        self.cenik_knjiznicnih_storitev_button = Button(
            self.find_element(By.XPATH, self.cenik_knjiznicnih_storitev_xpath))
        self.imenik_zaposlenih_button = Button(self.find_element(By.XPATH, self.imenik_zaposlenih_xpath))
        self.po_abecedi_button = Button(self.find_element(By.XPATH, self.po_abecedi_xpath))
        self.redni_profesorji_button = Button(self.find_element(By.XPATH, self.redni_profesorji_xpath))
        self.izredni_profesorji_button = Button(self.find_element(By.XPATH, self.izredni_profesorji_xpath))
        self.docenti_button = Button(self.find_element(By.XPATH, self.docenti_xpath))
        self.predavatelji_in_visji_predavatelji_button = Button(
            self.find_element(By.XPATH, self.predavatelji_in_visji_predavatelji_xpath))
        self.asistenti_button = Button(self.find_element(By.XPATH, self.asistenti_xpath))
        self.tehniski_sodelavci_button = Button(self.find_element(By.XPATH, self.tehniski_sodelavci_xpath))
        self.raziskovalci_button = Button(self.find_element(By.XPATH, self.raziskovalci_xpath))
        self.ostale_sluzbe_button = Button(self.find_element(By.XPATH, self.ostale_sluzbe_xpath))
        self.zunanji_sodelavci_button = Button(self.find_element(By.XPATH, self.zunanji_sodelavci_xpath))
        self.upokojeni_profesorji_button = Button(self.find_element(By.XPATH, self.upokojeni_profesorji_xpath))
        self.telefonija_uporabniska_pomoc_button = Button(
            self.find_element(By.XPATH, self.telefonija_uporabniska_pomoc_xpath))
        self.nagrade_in_priznanja_button = Button(self.find_element(By.XPATH, self.nagrade_in_priznanja_xpath))
        self.vidmarjeve_nagrade_button = Button(self.find_element(By.XPATH, self.vidmarjeve_nagrade_xpath))
        self.vodovnikove_nagrade_button = Button(self.find_element(By.XPATH, self.vodovnikove_nagrade_xpath))
        self.presernove_nagrade_button = Button(self.find_element(By.XPATH, self.presernove_nagrade_xpath))
        self.priznanje_poslovnim_partnerjem_button = Button(
            self.find_element(By.XPATH, self.priznanje_poslovnim_partnerjem_xpath))
        self.nagrada_sodelavcem_fakultete_button = Button(
            self.find_element(By.XPATH, self.nagrada_sodelavcem_fakultete_xpath))
        self.dekanove_pohvale_studentom_button = Button(
            self.find_element(By.XPATH, self.dekanove_pohvale_studentom_xpath))
        self.univerzitetna_priznanja_button = Button(self.find_element(By.XPATH, self.univerzitetna_priznanja_xpath))
        self.drzavne_nagrade_in_priznanja_button = Button(
            self.find_element(By.XPATH, self.drzavne_nagrade_in_priznanja_xpath))
        self._100fe_button = Button(self.find_element(By.XPATH, self._100fe_xpath))
        self.zgodovina_button = Button(self.find_element(By.XPATH, self.zgodovina_xpath))
        self.slovesna_akademija_button = Button(self.find_element(By.XPATH, self.slovesna_akademija_xpath))
        self.zbornik_button = Button(self.find_element(By.XPATH, self.zbornik_xpath))
        self.intervjuji_button = Button(self.find_element(By.XPATH, self.intervjuji_xpath))
        self.casovna_kapsula_button = Button(self.find_element(By.XPATH, self.casovna_kapsula_xpath))

        self.fakulteta_button = Button(self.find_element(By.XPATH, self.fakulteta_xpath))
        self.predstavitev_button = Button(self.find_element(By.XPATH, self.predstavitev_xpath))

    def init_collapsed(self):
        self.o_fakulteti_button = None
        self.fakulteta_button = None
        self.predstavitev_button = None
        self.poslanstvo_in_vizija_button = None
        self.zgodovina_button = None
        self.katedre_in_laboratoriji_button = None
        self.organiziranost_fakultete_button = None
        self.vodstvo_button = None
        self.senat_button = None
        self.akademski_zbor_button = None
        self.upravni_odbor_button = None
        self.predstojniki_kateder_button = None
        self.skupne_sluzbe_button = None
        self.katalog_ijz_button = None
        self.kje_smo_button = None
        self.medijsko_sredisce_button = None
        self.vizitka_button = None
        self.predstavitvene_brosure_button = None
        self.celostna_graficna_podoba_button = None
        self.prostori_fakultete_button = None
        self.cenik_najema_prostorov_button = None
        self.nacrt_prostorov_button = None
        self.dokumenti_button = None
        self.porocila_button = None
        self.pravilniki_button = None
        self.habilitacije_button = None
        self.varstvo_osebnih_podatkov_button = None
        self.zaupna_oseba_button = None
        self.zalozba_in_trgovina_button = None
        self.cenik_knjig_button = None
        self.seznam_literature_button = None
        self.cenik_promocijskih_artiklov_button = None
        self.delovni_cas_in_kontakt_button = None
        self.restavracija_button = None
        self.tedenski_meni_button = None
        self.cenik_bife_button = None
        self.cenik_jedi_in_menijev_button = None
        self.delovni_cas_in_kontakt_button = None
        self.knjiznica_button = None
        self.o_knjiznici_button = None
        self.izposoja_button = None
        self.e_knjiznica_button = None
        self.bibliografije_raziskovalcev_button = None
        self.digitalne_storitve_button = None
        self.uporabniski_koticek_button = None
        self.navajanje_virov_button = None
        self.cenik_knjiznicnih_storitev_button = None
        self.imenik_zaposlenih_button = None
        self.po_abecedi_button = None
        self.redni_profesorji_button = None
        self.izredni_profesorji_button = None
        self.docenti_button = None
        self.predavatelji_in_visji_predavatelji_button = None
        self.asistenti_button = None
        self.tehniski_sodelavci_button = None
        self.raziskovalci_button = None
        self.ostale_sluzbe_button = None
        self.zunanji_sodelavci_button = None
        self.upokojeni_profesorji_button = None
        self.telefonija_uporabniska_pomoc_button = None
        self.nagrade_in_priznanja_button = None
        self.vidmarjeve_nagrade_button = None
        self.vodovnikove_nagrade_button = None
        self.presernove_nagrade_button = None
        self.priznanje_poslovnim_partnerjem_button = None
        self.nagrada_sodelavcem_fakultete_button = None
        self.dekanove_pohvale_studentom_button = None
        self.univerzitetna_priznanja_button = None
        self.drzavne_nagrade_in_priznanja_button = None
        self._100fe_button = None
        self.zgodovina_button = None
        self.slovesna_akademija_button = None
        self.zbornik_button = None
        self.intervjuji_button = None
        self.casovna_kapsula_button = None


        self.fakulteta_button = None
        self.predstavitev_button = None
