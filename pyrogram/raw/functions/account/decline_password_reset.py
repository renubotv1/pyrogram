
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


class DeclinePasswordReset(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``4C9409F6``

    Parameters:
        No parameters required.

    Returns:
        ``bool``
    """

    __slots__: List[str] = []

    ID = 0x4c9409f6
    QUALNAME = "functions.account.DeclinePasswordReset"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeclinePasswordReset":
        # No flags
        
        return DeclinePasswordReset()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
