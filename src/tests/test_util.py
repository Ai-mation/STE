import pathlib

from AIAutomation.utils import util

PDF_DIRECTORY = util.get_project_root() / "pdfs"


def test_extract_scpi_commands():
    # build pdf path
    pdf_path = PDF_DIRECTORY / "sample.pdf"
    # read in pdf file and convert to text
    pdf_text = util.extract_text_from_pdf(pdf_path=pdf_path)

    scpis = util.extract_scpi_commands(pdf_text)

    [print(scpi) for scpi in scpis]

    # test if scpis returns a lists
    assert isinstance(scpis, list)

    # test if all elements are strings of SCPIs
    assert all(isinstance(command, str) for command in scpis)

    # test if any SCPI is return
    assert len(scpis) > 0

    # test if all SCPI are between 3 and 25 characters
    assert all((3 <= len(command) <= 25) for command in scpis)
