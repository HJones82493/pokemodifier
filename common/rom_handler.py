"""Module to handle all ROM file interactions

All classes in this module are designed to handle the initial reading and final writing
to and from the ROM files.

Typical usage examples:
    RomReader
        rom_reader = RomReader("<path to ROM>")
        rom_data = rom_reader.data

    RomWriter
        rom_writer = RomWriter(b"<modify rom data as a byte string>", "<path to where to write>")
        rom_writer.write()
"""
import os

from common.exceptions import OverwriteException

class RomReader:
    """Class used to read from a ROM file and import the bytes data"""
    def __init__(self, file_path: str = None, close_on_finish: bool = False):
        """Initialize the ROM reader

        Args:
            file_path - Full path of the ROM file to read
            close_on_finish - Whether to close the file pointer after data has been read
        """
        self._file_path = file_path
        self._file_pointer = None
        self._data = None

        if file_path:
            self._open_file()
        if close_on_finish:
            self._close_file()

    @property
    def file_data(self):
        return self._data

    def _open_file(
            self,
            close_existing: bool = True,
            overwrite_data: bool = True
    ):
        """Method to open the ROM file

        Args:
            close_existing - Whether to close an existing file pointer, default True
            overwrite_data - Whether to overwrite existing data, default True

        Raises:
            FileNotFoundError - If the specified file does not exist
            IOError - If the file is already open and close_existing is False
        """
        if not os.path.exists(self._file_path):
            raise FileNotFoundError(f"Unable to locate ROM file at: {self._file_path}")

        if self._file_pointer:
            if not self._file_pointer.closed:
                if close_existing:
                    self._close_file()
                else:
                    raise IOError("File is already open")
        self._file_pointer = open(self._file_path, "rb")
        self._read_file(overwrite_data)

    def _read_file(self, overwrite_existing: bool = True):
        """Method to read all data from the file

        Args:
            overwrite_existing - Whether to overwrite existing data

        Raises:
            IOError - The file hasn't been opened properly
                    - The file has been opened but is currently closed
        """
        if not self._file_pointer:
            raise IOError("The file hasn't been opened for reading")
        if self._file_pointer.closed:
            raise IOError("The file has been closed")

        if self._data:
            if not overwrite_existing:
                raise OverwriteException("Cannot read file, data already exists")
        self._file_pointer.seek(0)
        self._data = self._file_pointer.read()

    def open_file(
            self,
            file_path: str,
            close_existing: bool = True,
            overwrite_data: bool = True
    ):
        """Opens a file specified by the file_path variable

        NOTE: This will overwrite the file path specified on object creation

        Args:
            file_path - The path to attempt to open
            close_existing - Whether to close an existing file pointer
            overwrite_data - Whether to overwrite existing data, default True
        """
        self._file_path = file_path
        self._open_file(close_existing)
        self._read_file(overwrite_data)

    def _close_file(self):
        """Method to close the file pointer"""
        if not self._file_pointer:
            raise IOError("File not opened to be closed")
        if not self._file_pointer.closed:
            self._file_pointer.close()


class RomWriter:
    """Class used to write data from the app to a ROM file"""
    def __init__(
            self,
            rom_data: bytes,
            file_path: str,
            overwrite: bool = False
    ):
        """Initialize the ROM writer

        Can specify an existing file. If overwrite is false and an already existing path is
        provided, will raise an exception.

        Args:
            rom_data - The data to write for the rom as a byte string
            file_path - Full path to write the ROM file to
            overwrite - Variable to determine whether to overwrite existing file
        """
        self._data = rom_data
        self._save_path = file_path
        self._overwrite = overwrite

    def write(self):
        """Method to save the rom data to the specified file

        Raises:
            IOError - If the file already exists and overwrite is false
        """
        if os.path.exists(self._save_path):
            if not self._overwrite:
                raise IOError("File already exists, cannot write")
        with open(self._save_path, "wb") as fw:
            fw.write(self._data)

    def select_new_file(self, file_path: str):
        """Method to change the save location of the writer

        Args:
            file_path - The location to save the ROM data at

        Raises:
            IOError - If the new path already exists and overwrite is set to false
        """
        if os.path.exists(file_path):
            if not self._overwrite:
                raise IOError("File already exists")
        self._save_path = file_path

    def set_overwrite(self, overwrite: bool):
        """Method to set or unset overwrite

        Args:
            overwrite - Whether to overwrite existing files
        """
        self._overwrite = overwrite