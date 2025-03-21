from time import sleep
import flet as ft

class View(object):                             # DA QUI GESTISCO L'INTERFACCIA GRAFICA
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page
        self._txtOut = None

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        self._dd_scegliLingua = ft.Dropdown(label="Select Language",
                                            options=[ft.dropdown.Option("italian"),ft.dropdown.Option("english"),ft.dropdown.Option("spanish")])

        self._ddScegliMetodo = ft.Dropdown(label="Search Modality",
                                      options=[ft.dropdown.Option("Default"),ft.dropdown.Option("Linear"),ft.dropdown.Option("Dichotomic")], expand = 1)
        self._txtIn = ft.TextField(label="Add your sentence here",hint_text="Text", value="", expand = 1)
        self._btn = ft.ElevatedButton("SpellCheck", width = 100, on_click=self.__controller.handleSpellCheck)#da mettere in  controller

        self._txtOut = ft.ListView(expand=1)# sara giusto?      non so

        row1 = ft.Row([self._dd_scegliLingua])
        row2 = ft.Row([self._ddScegliMetodo, self._txtIn, self._btn])
        row3=ft.Row([self._txtOut])


        self.page.add(row1,row2, row3)
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
