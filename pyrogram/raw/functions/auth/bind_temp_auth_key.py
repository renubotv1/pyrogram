
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


class BindTempAuthKey(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``CDD42A05``

    Parameters:
        perm_auth_key_id (``int`` ``64-bit``):
            N/A

        nonce (``int`` ``64-bit``):
            N/A

        expires_at (``int`` ``32-bit``):
            N/A

        encrypted_message (``bytes``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["perm_auth_key_id", "nonce", "expires_at", "encrypted_message"]

    ID = 0xcdd42a05
    QUALNAME = "functions.auth.BindTempAuthKey"

    def __init__(self, *, perm_auth_key_id: int, nonce: int, expires_at: int, encrypted_message: bytes) -> None:
        self.perm_auth_key_id = perm_auth_key_id  # long
        self.nonce = nonce  # long
        self.expires_at = expires_at  # int
        self.encrypted_message = encrypted_message  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BindTempAuthKey":
        # No flags
        
        perm_auth_key_id = Long.read(b)
        
        nonce = Long.read(b)
        
        expires_at = Int.read(b)
        
        encrypted_message = Bytes.read(b)
        
        return BindTempAuthKey(perm_auth_key_id=perm_auth_key_id, nonce=nonce, expires_at=expires_at, encrypted_message=encrypted_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.perm_auth_key_id))
        
        b.write(Long(self.nonce))
        
        b.write(Int(self.expires_at))
        
        b.write(Bytes(self.encrypted_message))
        
        return b.getvalue()
