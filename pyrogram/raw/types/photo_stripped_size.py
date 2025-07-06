
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class PhotoStrippedSize(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``166``
        - ID: ``E0B0BC2E``

    Parameters:
        type (``str``):
            N/A

        bytes (``bytes``):
            N/A

    """

    __slots__: List[str] = ["type", "bytes"]

    ID = 0xe0b0bc2e
    QUALNAME = "types.PhotoStrippedSize"

    def __init__(self, *, type: str, bytes: bytes) -> None:
        self.type = type  # string
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoStrippedSize":
        # No flags
        
        type = String.read(b)
        
        bytes = Bytes.read(b)
        
        return PhotoStrippedSize(type=type, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.type))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()
