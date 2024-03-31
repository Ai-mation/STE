import logging
import os
import pathlib
from typing import List, Optional, Union

from errors import MultipleHandlersFoundError

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def init_logger(
    filename: Optional[Union[pathlib.Path, str]] = None,
    file_level: Optional[int] = logging.DEBUG,
) -> None:

    logging.basicConfig(level=logging.DEBUG)
    if filename:
        setup_file_handler(filename, file_level)


def find_handler(handler: logging.Handler) -> Union[logging.Handler, None]:
    handlers: List[logging.Handler] = []
    for h in logging.root.handlers:
        # we want an exact match, do not use isinstance
        if h is handler:
            handlers.append(h)
    n = len(handlers)
    if n == 0:
        return None
    elif n == 1:
        return handlers[0]
    else:
        raise MultipleHandlersFoundError(handler)


def find_file_handler() -> Union[logging.FileHandler, None]:
    """Return `logging.FileHandler` from `logging.root.logger`."""
    return find_handler(logging.FileHandler)


def find_stream_handler() -> Union[logging.StreamHandler, None]:
    """Return `logging.StreamHandler` from `logging.root.logger`."""
    return find_handler(logging.StreamHandler)


def _create_file_handler(
    filename: pathlib.Path, level: Optional[int] = logging.DEBUG
) -> logging.FileHandler:
    """Setup, format, and return a custom `logging.FileHandler`.

    Args:
        `filename`
        `level`: Defaults to `logging.DEBUG`

    Returns:
        A `logging.FileHandler`.
    """
    filename.parent.mkdir(parents=True, exist_ok=True)
    file_formatter = logging.Formatter(
        fmt=(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s\t\t\t\t"
            "[ %(pathname)s:%(lineno)s ]"
        )
    )
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(file_formatter)
    return file_handler


def setup_file_handler(
    filename: Union[pathlib.Path, str], level: Optional[int] = logging.DEBUG
) -> None:
    """Create a `logging.FileHandler` or change the filename of an existing one.

    Args:
        `filename`: Must have a `.log` file extension.
        `level`: Defaults to `logging.DEBUG`
    """
    if not isinstance(filename, pathlib.Path):
        filename = pathlib.Path(filename)
    if filename.suffix != ".log":
        raise ValueError(f"File must have .log extension: {filename}")
    if filename.exists():
        raise FileExistsError(filename)
    file_handler_old = find_file_handler()
    if file_handler_old:
        filename_old = pathlib.Path(file_handler_old.baseFilename)
        file_handler_old.close()
        filename_old.replace(filename)
        logging.root.removeHandler(file_handler_old)
    file_handler = _create_file_handler(filename, level)
    logging.root.addHandler(file_handler)


def clear_handlers():
    logging.root.handlers.clear()
