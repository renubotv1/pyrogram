
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


class GetAppConfig(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``61E3F854``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`help.AppConfig <pyrogram.raw.base.help.AppConfig>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x61e3f854
    QUALNAME = "functions.help.GetAppConfig"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAppConfig":
        # No flags
        
        hash = Int.read(b)
        
        return GetAppConfig(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        return b.getvalue()
