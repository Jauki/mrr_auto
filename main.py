from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import os

urlSen = "https://sentence.yourdictionary.com/"
urlExp = "https://thesaurus.yourdictionary.com/"


class MRRTask:
    def __init__(self, src):
        self.src = src

    def translate(self):
        print("translate")
        translator = Translator(service_urls=['translate.googleapis.com'])
        print(translator.translate(self.src, dest="de").text)
        return translator.translate(self.src, dest="de").text
        pass

    def sentence(self):
        try:
            print("Sentence")
            page = requests.get(urlSen + self.src)
            soup = BeautifulSoup(page.content, 'html.parser')
            lists = soup.find_all('li', class_="sentences-list-item")
            sentences = []
            for item in lists:
                box = item.find('div', class_="single-sentence-box").text
                box = box.split('.')
                sentences.append(box[0])
            return sentences[0]
        except IndexError:
            print(f'Some Words cant be converted! Look up yourself - Sentence Manager')
            return '!!! X !!!'
        pass

    def synonym(self):
        try:
            print("Synonym")
            page = requests.get(urlExp + self.src)
            soup = BeautifulSoup(page.content, 'html.parser')
            lists = soup.find_all('div', class_="single-synonym-box")
            synonyms = []
            for item in lists:
                box = item.find('div', class_="synonym").text
                synonyms.append(box)
            return synonyms[0]
        except IndexError:
            print(f'Some Words cant be converted! Look up yourself - Synonym Manager')
            return '!!! X !!!'
        pass

    def out(self):
        print("out")
        return f'| {self.src} | {self.sentence()} | {self.synonym()} |  {self.translate()} |\n'


def print_file(object_list):
    try:
        if os.path.isfile("out.md"):
            os.remove("out.md")
        f = open("out.md", "w")
        f.write("| word | sentence | explanation | german |\n"
                "|------|----------|-------------|--------|\n")
        for obj in object_list:
            f.write(obj.out())
        f.close()
        print("Done! Everything is stored in the 'out.md' File in your directory!")
    except OSError:
        print(f'Error!')


def in_file():
    file_name = "in.txt"
    f = open(file_name)
    input_text = f.read()
    f.close()
    return input_text.splitlines()


# Main
words = in_file()
objects = []

for word in words:
    objects.append(MRRTask(word))

print_file(objects)
