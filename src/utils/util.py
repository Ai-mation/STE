import pathlib
import re
from datetime import datetime
from pathlib import Path

import pypdf
from pypdf._protocols import PdfReaderProtocol, PdfWriterProtocol
from pypdf.generic import IndirectObject

from AIAutomation.utils.util_models import SCPIPatterns


class pdf:
    error_state = {"01": "File doesn't exis"}

    def __init__(self, pdf_file_path: Path) -> None:
        self.pdf_file_path = pdf_file_path
        self.pdf_reader = self.read_pdf()
        self.pdf_object = None
        self.pdf_pages = []
        self.error_state = None

    def read_pdf(self):
        if not Path.exists():
            raise FileNotFoundError

        self.pdf_object = self.pdf_reader(open(self.pdf_file_path))
        self.pdf_pages.append(
            [PdfPage(filepdf) for filepdf in self.pdf_object.pages]
        )


class PdfPage(pypdf.PageObject):
    def __init__(
        self,
        pdf: PdfReaderProtocol | PdfWriterProtocol | None = None,
        indirect_reference: IndirectObject | None = None,
    ) -> None:
        super().__init__(pdf, indirect_reference)


# ------------- OS/PATH UTILS -----------------#


def get_project_root():
    root = pathlib.Path(__file__).parent.parent
    return root


# ------------- DATETIME UTILS -----------------#
def get_date_time():
    now = datetime.now()
    now_formatted = now.strftime("%Y-%m-%d_%H:%M:%S")
    return now_formatted


# TODO: Need a way to divide this into header/footer and actual page content
# TODO: Create a MODEL of PDF where
# pages = list of page


def extract_text_from_pdf(pdf_path):
    text = ""
    pdf = pypdf.PdfReader(open(pdf_path, "rb"))
    for page in pdf.pages:
        text += page.extract_text()
        return text
    return text


def extract_scpi_commands(text):
    scpi_patterns = SCPIPatterns()
    for pattern in scpi_patterns:
        scpi_match = re.findall(pattern, text)
        if scpi_match:
            return scpi_match


def extract_patterns_from_text(text: str, pattern: re.Pattern):
    matches = re.findall(pattern=pattern, string=text)
    if matches:
        return matches


def extract_pattern_from_text(text: str, pattern: re.Pattern):
    match = re.search(pattern=pattern, string=text)
    if match:
        found = match.group()
        return found
