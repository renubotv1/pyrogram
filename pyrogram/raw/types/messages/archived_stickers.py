
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


class ArchivedStickers(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ArchivedStickers`.

    Details:
        - Layer: ``166``
        - ID: ``4FCBA9C8``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        sets (List of :obj:`StickerSetCovered <pyrogram.raw.base.StickerSetCovered>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetArchivedStickers
    """

    __slots__: List[str] = ["count", "sets"]

    ID = 0x4fcba9c8
    QUALNAME = "types.messages.ArchivedStickers"

    def __init__(self, *, count: int, sets: List["raw.base.StickerSetCovered"]) -> None:
        self.count = count  # int
        self.sets = sets  # Vector<StickerSetCovered>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ArchivedStickers":
        # No flags
        
        count = Int.read(b)
        
        sets = TLObject.read(b)
        
        return ArchivedStickers(count=count, sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.sets))
        
        return b.getvalue()
