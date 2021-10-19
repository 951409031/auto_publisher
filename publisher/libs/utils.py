import zlib


def crc32(file):
    h = zlib.crc32(file, 0)
    return "%08X" % (h & 0xFFFFFFFF)

