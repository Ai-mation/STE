import re
from typing import NamedTuple


class SCPIPatterns(NamedTuple):
    FOUR_CHAR_SCPI: re.Pattern = r"\b[A-Z:]{4,}\b"
    THREE_CHAR_SCPI: re.Pattern = r"\b[A-Z:]{3,}\b"
    COLON_CHAR_SCPI: re.Pattern = r"\b[A-Z:]{3|4:,}\b"
