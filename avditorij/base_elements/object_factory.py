
o_fakulteti_strings = [
'O fakulteti',
'Fakulteta',
'Predstavitev',
'Poslanstvo in vizija',
'Zgodovina',
'Katedre in laboratoriji',
'Organiziranost fakultete',
'Vodstvo',
'Senat',
'Akademski zbor',
'Upravni odbor',
'Predstojniki kateder',
'Skupne službe',
'Katalog IJZ',
'Kje smo',
'Medijsko središče',
'Vizitka',
'Predstavitvene brošure',
'Celostna grafična podoba',
'Prostori fakultete',
'Cenik najema prostorov',
'Načrt prostorov',
'Dokumenti',
'Poročila',
'Pravilniki',
'Habilitacije',
'Varstvo osebnih podatkov',
'Zaupna oseba',
'Založba in trgovina',
'Cenik knjig',
'Seznam literature',
'Cenik promocijskih artiklov',
'Delovni čas in kontakt',
'Restavracija',
'Tedenski meni',
'Cenik bife',
'Cenik jedi in menijev',
'Delovni čas in kontakt',
'Knjižnica',
'O knjižnici',
'Izposoja',
'E-knjižnica',
'Bibliografije raziskovalcev',
'Digitalne storitve',
'Uporabniški kotiček',
'Navajanje virov',
'Cenik knjižničnih storitev',
'Imenik zaposlenih',
'Po abecedi',
'Redni profesorji',
'Izredni profesorji',
'Docenti',
'Predavatelji in višji predavatelji',
'Asistenti',
'Tehniški sodelavci',
'Raziskovalci',
'Ostale službe',
'Zunanji sodelavci',
'Upokojeni profesorji',
'Telefonija – uporabniška pomoč',
'Nagrade in priznanja',
'Vidmarjeve nagrade',
'Vodovnikove nagrade',
'Prešernove nagrade',
'Priznanje poslovnim partnerjem',
'Nagrada sodelavcem fakultete',
'Dekanove pohvale študentom',
'Univerzitetna priznanja',
'Državne nagrade in priznanja',
'100FE',
'Zgodovina',
'Slovesna akademija',
'Zbornik',
'Intervjuji',
'Časovna kapsula',
]
izobrazevanje_strings = ...

class Factory:
    def __init__(self, list_of_strings: [str], level):
        self.elem_text = []
        self.elem_xpath = []
        self.elem_button = []
        self.elem_button_three_dots = []
        self.elem_button_none = []
        for string in list_of_strings:
            temp = string
            temp = temp.lower()
            temp = temp.replace(' ', "_").replace("š", "s").replace("č", "c").replace("ž", "z")

            self_string = f'self.{temp}'
            self.elem_text.append(f"{self_string}_text = '{string}'")
            xpath = f"{self_string}_xpath = self.menu_level{level}_xpath.format(text=self.{temp}_text)"
            self.elem_xpath.append(xpath)

            self.elem_button_three_dots.append(f"{self_string}_button = ...")
            self.elem_button.append(f"{self_string}_button = Button(self.find_element(By.XPATH, {self_string}_xpath))")
            self.elem_button_none.append(f"{self_string}_button = None")
    def print_text(self):
        for elem in self.elem_text:
            print(elem)

    def print_xpath(self):
        for elem in self.elem_xpath:
            print(elem)

    def print_three_dots(self):
        for elem in self.elem_button_three_dots:
            print(elem)

    def print_button(self):
        for elem in self.elem_button:
            print(elem)

    def print_none(self):
        for elem in self.elem_button_none:
            print(elem)

o_fakulteti = Factory(o_fakulteti_strings, 3)
#o_fakulteti.print_text()
#o_fakulteti.print_xpath()
#o_fakulteti.print_three_dots()
o_fakulteti.print_button()
#o_fakulteti.print_none()
