##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 3-1-24                                                                                               #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and method implementation of a class used to manipulate bytes and     #
# their binary representations                                                                               #                     
##############################################################################################################

def _isBytes(_bytes):
    """
    Returns true if and only if _bytes is a bytes object instance.
    """
    return isinstance(_bytes,bytes)

def _isBin(_bin):
    """
    Returns true if and only if _bin is a valid binary string.
    """
    return isinstance(_bin,str) and set(_bin) <= {"0","1"} and len(_bin)%8 == 0

def _toBytes(_bin):
    """
    Function that given a binary-string returns a bytes object with the binary 
    representation of _bin.
    """
    return bytes(int(_bin[i:i+8], 2) for i in range(0, len(_bin), 8))


def _toBin(_bytes):
    """
    Function that given a bytes object instance, returns a string containing its 
    binary representation.
    """
    return ''.join(format(byte, '08b') for byte in _bytes)

class BitArray:
    """
    Class that converts strings of "0s" and "1s" to instances of bytes objects
    and vice versa. It tries to mimic the BitArray class from bitarray.
    """    
    
    def tofile(self,f):
        f.write(self.bytes)
    
    def __init__(self,bin=None,bytes=None):
        
        if bin is None and bytes is None:
            raise Exception("Invoke with 'bin' or 'bytes'")
        
        if bin is not None and bytes is not None:
            raise Exception("Invoke with just one: 'bin' or 'bytes'")
        
        if bin is not None:    
            if _isBin(bin):
                self.bin = bin
                self.bytes = _toBytes(bin)
            else:
                raise Exception("Not a good bin type.")
        else:
            if _isBytes(bytes):
                self.bytes = bytes
                self.bin = _toBin(bytes)
            else:
                raise Exception("Not a good bytes type.")    
