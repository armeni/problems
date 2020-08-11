import ctypes


def dec2bin(x, signed) -> str:
    """
    Выдать двоичное представление int32/uint32
    """
    if signed:
        return f'{x & 0xffffffff:032b}'
    else:
        return f'{x:032b}'


def bin2dec(x, signed) -> int:
    """
    Выдать целое число по его двоичному представлению
    """
    return int(x, 2) - 2**32 * int(x[0]) * signed


def float2bin(x) -> str:
    """
    Выдать двоичное представление float32
    """
    return f'{ctypes.c_uint32.from_buffer(ctypes.c_float(x)).value:>032b}'


def bin2float(x) -> float:
    """
    Выдать float32 по его двоичному представлению
    """
    return ctypes.c_float.from_buffer(ctypes.c_uint32(int(x, 2))).value
