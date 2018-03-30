import sys

PY2 = sys.version_info[0] == 2

if PY2:
    from .zipencrypt2 import ZipFile
    from zipfile import BadZipfile, error, ZIP_STORED, ZIP_DEFLATED, \
        is_zipfile, ZipInfo, PyZipFile, LargeZipFile
    __all__ = ["BadZipfile", "error", "ZIP_STORED", "ZIP_DEFLATED",
               "is_zipfile", "ZipInfo", "ZipFile", "PyZipFile", "LargeZipFile"]
else:
    from .zipencrypt3 import ZipFile
    from zipfile import BadZipFile, BadZipfile, error, ZIP_STORED, \
        ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA, is_zipfile, ZipInfo, PyZipFile, \
        LargeZipFile
    __all__ = ["BadZipFile", "BadZipfile", "error",
               "ZIP_STORED", "ZIP_DEFLATED", "ZIP_BZIP2", "ZIP_LZMA",
               "is_zipfile", "ZipInfo", "ZipFile", "PyZipFile", "LargeZipFile"]
