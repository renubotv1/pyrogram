
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


class InputKeyboardButtonUrlAuth(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``166``
        - ID: ``D02E7FD4``

    Parameters:
        text (``str``):
            N/A

        url (``str``):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        request_write_access (``bool``, *optional*):
            N/A

        fwd_text (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "url", "bot", "request_write_access", "fwd_text"]

    ID = 0xd02e7fd4
    QUALNAME = "types.InputKeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, bot: "raw.base.InputUser", request_write_access: Optional[bool] = None, fwd_text: Optional[str] = None) -> None:
        self.text = text  # string
        self.url = url  # string
        self.bot = bot  # InputUser
        self.request_write_access = request_write_access  # flags.0?true
        self.fwd_text = fwd_text  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUrlAuth":
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        text = String.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 1) else None
        url = String.read(b)
        
        bot = TLObject.read(b)
        
        return InputKeyboardButtonUrlAuth(text=text, url=url, bot=bot, request_write_access=request_write_access, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 1) if self.fwd_text is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(self.bot.write())
        
        return b.getvalue()
