
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedAuthorization = Union[raw.types.auth.ExportedAuthorization]


# noinspection PyRedeclaration
class ExportedAuthorization:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.ExportedAuthorization

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.ExportAuthorization
    """

    QUALNAME = "pyrogram.raw.base.auth.ExportedAuthorization"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/exported-authorization")
