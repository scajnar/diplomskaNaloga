from avditorij.base_elements.base_page_element import BasePageElement
from avditorij.base_elements.page import Page
from avditorij.elements.dropdown import Dropdown


class CoursePage(Page):
    def __init__(self, element):
        super().__init__(element)
        self.predmet_button_text = "Predmet"
        self.nastavitve_button_text = "Nastavitve"
        self.sodelujoci_button_text = "Sodelujoči"
        self.ocene_button_text = "Ocene"
        self.porocila_button_text = "Poročila"
        self.more_dropdown_text = "More"

        self.title_xpath = './/h1'
        self.predmet_button_xpath = f'.//a[@role="menuitem" and contains(text(), "{self.predmet_button_text}")]'
        self.nastavitve_button_xpath = f'.//a[@role="menuitem" and contains(text(), "{self.nastavitve_button_text}")]'
        self.sodelujoci_button_xpath = f'.//a[@role="menuitem" and contains(text(), "{self.sodelujoci_button_text}")]'
        self.ocene_button_xpath = f'.//a[@role="menuitem" and contains(text(), "{self.ocene_button_text}")]'
        self.porocila_button_xpath = f'.//a[@role="menuitem" and contains(text(), "{self.porocila_button_text}")]'
        self.more_dropdown_xpath =  f'.//a[@role="menuitem" and contains(text(), "{self.more_dropdown_text}")]'


    class Nastavitve(BasePageElement):
        def __init__(self, element):
            super().__init__(element)
            self.subtitle_xpath = './/h2'
            self.splosno_dropdown_xpath = './/fieldset[@id="id_general"]'
            self.opis_dropdown_xpath = './/fieldset[@id="id_descriptionhdr"]'
            self.oblika_predmeta_dropdown_xpath = './/fieldset[@id="id_courseformathdr"]'
            self.izgled_dropdown_xpath = './/fieldset[@id="id_appearancehdr"]'
            self.datoteke_in_prenosi_dropdown_xpath = './/fieldset[@id="id_filehdr"]'
            self.sledenje_zakljucevanju_dropdown_xpath = './/fieldset[@id="id_completionhdr"]'
            self.skupine_dropdown_xpath = './/fieldset[@id="id_groups"]'
            self.preimenovanje_vlog_dropdown_xpath = './/fieldset[@id="id_rolerenaming"]'
            self.oznake_dropdown_xpath = './/fieldset[@id="id_tagshdr"]'
            self.shrani_in_prikazi_button_xpath = './/input[@id="id_saveanddisplay"]'
            self.preklici_button_xpath = './/input[@id="id_cancel"]'
            self.zahtevana_polja_text_xpath = './/div[@class="fdescription required"]'
            self.zahtevana_polja_info_icon_xpath = './/div[@class="fdescription required"]/i'


        class NastavitveDropdown(BasePageElement):
            def __init__(self, element):
                super().__init__(element)
                self.label_xpath = './/label'
                self.question_mark_icon_xpath = './/i[contains(@class,  "exclamation-circle")]'
                self.exclamation_mark_icon_xpath = './/i[contains(@class,  "question-circle")]'

        class DropdownRow(BasePageElement):
            def __init__(self, element):
                super().__init__(element)

        class InputRow(BasePageElement):
            def __init__(self, element):
                super().__init__(element)


        class SplosnoDropdown(Dropdown):
            def __init__(self, element):
                super().__init__(element)
                # //div[contains(@class, "form-group row  fitem")]


