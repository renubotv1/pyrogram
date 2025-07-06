
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


class ChatAdminWithInvites(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatAdminWithInvites`.

    Details:
        - Layer: ``166``
        - ID: ``F2ECEF23``

    Parameters:
        admin_id (``int`` ``64-bit``):
            N/A

        invites_count (``int`` ``32-bit``):
            N/A

        revoked_invites_count (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["admin_id", "invites_count", "revoked_invites_count"]

    ID = 0xf2ecef23
    QUALNAME = "types.ChatAdminWithInvites"

    def __init__(self, *, admin_id: int, invites_count: int, revoked_invites_count: int) -> None:
        self.admin_id = admin_id  # long
        self.invites_count = invites_count  # int
        self.revoked_invites_count = revoked_invites_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminWithInvites":
        # No flags
        
        admin_id = Long.read(b)
        
        invites_count = Int.read(b)
        
        revoked_invites_count = Int.read(b)
        
        return ChatAdminWithInvites(admin_id=admin_id, invites_count=invites_count, revoked_invites_count=revoked_invites_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.admin_id))
        
        b.write(Int(self.invites_count))
        
        b.write(Int(self.revoked_invites_count))
        
        return b.getvalue()
