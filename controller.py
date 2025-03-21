import time
from time import sleep

import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleSpellCheck(self,e):
        self._view._txtOut.clean()
        if self._view._txtIn.value =="":
            self._view._txtOut.controls.append(ft.Text("Add a sentence!", color="red"))
            self._view.page.update()
            sleep(1)
            self._view._txtOut.clean()
            self._view.page.update()
            return
        if self._view._dd_scegliLingua.value is None:
            self._view._txtOut.controls.append(ft.Text("Select a language!", color="red"))
            self._view.page.update()
            sleep(1)
            self._view._txtOut.clean()
            self._view.page.update()
            return
        if self._view._ddScegliMetodo.value is None:
            self._view._txtOut.controls.append(ft.Text("Choose a modality!", color="red"))
            self._view.page.update()
            sleep(1)
            self._view._txtOut.clean()
            self._view.page.update()
            return
        testo=self._view._txtIn.value
        lingua = self._view._dd_scegliLingua.value
        modalita = self._view._ddScegliMetodo.value

        paroleSbagliate, tempo = self.handleSentence(testo, lingua, modalita)

        self._view._txtOut.clean()

        if not paroleSbagliate == " - ":
            self._view._txtOut.controls.append(ft.Text(value=f"Frase inserita: {testo}\nParole errate: {paroleSbagliate}\nTempo richiesto dalla ricerca: {tempo}"))
            self._view.page.update()
        else:
            self._view._txtOut.controls.append(ft.Text(value=f"Everything is correct!\nFrase inserita: {testo}\nTempo richiesto dalla ricerca: {tempo}"))
            self._view.page.update()

        self._view._txtIn.value = ""
        self._view.page.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text