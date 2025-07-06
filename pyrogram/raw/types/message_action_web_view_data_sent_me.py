
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


class MessageActionWebViewDataSentMe(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``47DD8079``

    Parameters:
        text (``str``):
            N/A

        data (``str``):
            N/A

    """

    __slots__: List[str] = ["text", "data"]

    ID = 0x47dd8079
    QUALNAME = "types.MessageActionWebViewDataSentMe"

    def __init__(self, *, text: str, data: str) -> None:
        self.text = text  # string
        self.data = data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionWebViewDataSentMe":
        # No flags
        
        text = String.read(b)
        
        data = String.read(b)
        
        return MessageActionWebViewDataSentMe(text=text, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(String(self.data))
        
        return b.getvalue()
