import PyPDF2
import pyttsx3


with open('book/Republic By Plato.pdf', 'rb') as book:

    full_text = ""

    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 170)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content
        # # to listening from python
        # audio_reader.say(content)
        # audio_reader.runAndWait()

    # print(full_text)
    audio_reader.save_to_file(full_text, "myaudiobook3.mp3")
    audio_reader.runAndWait()

