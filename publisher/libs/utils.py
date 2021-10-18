import zlib


def crc32(file):
    with open(file, 'rb') as fh:
        h = 0
        while True:
            s = fh.read(65536)
            if not s:
                break
            h = zlib.crc32(s, h)
        return "%08X" % (h & 0xFFFFFFFF)

