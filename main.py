import pdfplumber
from gtts import gTTS


def get_text_string():
    file_path = "text.pdf"
    with pdfplumber.open(file_path) as pdf_file:
        page = pdf_file.pages
        pages_pdf_text = ''.join([page.extract_text() for page in page])
        pdf_text = "".join(pages_pdf_text)
        pdf_text.replace("\n", " ")
        return pdf_text

def get_audio_file():
    language = "ru"
    pdf_text = get_text_string()
    phrase = gTTS(text=pdf_text, lang=language, slow=False)
    phrase.save("computerhistory.mp3")


def main():
    get_text_string()
    get_audio_file()


if __name__ == '__main__':
    main()
