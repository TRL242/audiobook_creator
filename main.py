import PyPDF2
import pyttsx3


with open('book/Bridgewater Associates Ray Dalio - Principles.pdf', 'rb') as book:

    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 170)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        #to listening from python
        # audio_reader.say(content)
        audio_reader.save_to_file(content, "myaudiobook.mp3")
        audio_reader.runAndWait()

