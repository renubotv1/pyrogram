
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


class InputMediaAreaVenue(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``166``
        - ID: ``B282217F``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

        result_id (``str``):
            N/A

    """

    __slots__: List[str] = ["coordinates", "query_id", "result_id"]

    ID = 0xb282217f
    QUALNAME = "types.InputMediaAreaVenue"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", query_id: int, result_id: str) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.query_id = query_id  # long
        self.result_id = result_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaAreaVenue":
        # No flags
        
        coordinates = TLObject.read(b)
        
        query_id = Long.read(b)
        
        result_id = String.read(b)
        
        return InputMediaAreaVenue(coordinates=coordinates, query_id=query_id, result_id=result_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(Long(self.query_id))
        
        b.write(String(self.result_id))
        
        return b.getvalue()
