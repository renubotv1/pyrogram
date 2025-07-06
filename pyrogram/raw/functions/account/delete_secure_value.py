
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


class DeleteSecureValue(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``B880BC4B``

    Parameters:
        types (List of :obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["types"]

    ID = 0xb880bc4b
    QUALNAME = "functions.account.DeleteSecureValue"

    def __init__(self, *, types: List["raw.base.SecureValueType"]) -> None:
        self.types = types  # Vector<SecureValueType>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteSecureValue":
        # No flags
        
        types = TLObject.read(b)
        
        return DeleteSecureValue(types=types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.types))
        
        return b.getvalue()
