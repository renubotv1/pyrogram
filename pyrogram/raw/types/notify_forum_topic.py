
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


class NotifyForumTopic(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.NotifyPeer`.

    Details:
        - Layer: ``166``
        - ID: ``226E6308``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        top_msg_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "top_msg_id"]

    ID = 0x226e6308
    QUALNAME = "types.NotifyForumTopic"

    def __init__(self, *, peer: "raw.base.Peer", top_msg_id: int) -> None:
        self.peer = peer  # Peer
        self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NotifyForumTopic":
        # No flags
        
        peer = TLObject.read(b)
        
        top_msg_id = Int.read(b)
        
        return NotifyForumTopic(peer=peer, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_msg_id))
        
        return b.getvalue()
