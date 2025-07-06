
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AttachMenuPeerType = Union[raw.types.AttachMenuPeerTypeBotPM, raw.types.AttachMenuPeerTypeBroadcast, raw.types.AttachMenuPeerTypeChat, raw.types.AttachMenuPeerTypePM, raw.types.AttachMenuPeerTypeSameBotPM]


# noinspection PyRedeclaration
class AttachMenuPeerType:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            AttachMenuPeerTypeBotPM
            AttachMenuPeerTypeBroadcast
            AttachMenuPeerTypeChat
            AttachMenuPeerTypePM
            AttachMenuPeerTypeSameBotPM
    """

    QUALNAME = "pyrogram.raw.base.AttachMenuPeerType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/attach-menu-peer-type")
