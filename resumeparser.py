import PyPDF2
import docx

class ResumeParser:
    def __init__(self):
        pass

    def parse_resume(self, file_stream):
        file_stream.seek(0) 
        file_signature = file_stream.read(4)

        if file_signature == b'%PDF':
            return self._parse_pdf(file_stream)
        elif file_signature[:2] == b'PK':
            return self._parse_docx(file_stream)
        else:
            raise ValueError("Unsupported file type. Please provide a PDF or DOCX file.")

    @staticmethod
    def _parse_pdf(file_stream):
        text = ""
        try:
            reader = PyPDF2.PdfReader(file_stream)
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise ValueError(f"Error reading PDF file: {e}")

    @staticmethod
    def _parse_docx(file_stream):
        text = ""
        try:
            doc = docx.Document(file_stream)
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        except Exception as e:
            raise ValueError(f"Error reading DOCX file: {e}")

  