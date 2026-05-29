import os
from PyPDF2 import PdfReader
from docx import Document

class ResumeParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        if self.file_path.endswith(".pdf"):
            return self._parse_pdf()
        elif self.file_path.endswith(".docx"):
            return self._parse_docx()
        else:
            raise ValueError("Unsupported file format")

    def _parse_pdf(self):
        text = ""
        try:
            reader = PdfReader(self.file_path)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
        return text.strip()

    def _parse_docx(self):
        text = ""
        try:
            doc = Document(self.file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            return f"Error reading DOCX: {str(e)}"
        return text.strip()


# ✅ TEST BLOCK
if __name__ == "__main__":
    file_path = r"C:\Users\Dell\Desktop\DeepakResume1.pdf"  # change this path

    parser = ResumeParser(file_path)
    content = parser.parse()

    print("\n📄 Extracted Resume Text:\n")
    print(content[:1000])  # print first 1000 chars