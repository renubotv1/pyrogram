
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PQInnerData = Union[raw.types.PQInnerData, raw.types.PQInnerDataDc, raw.types.PQInnerDataTemp, raw.types.PQInnerDataTempDc]


# noinspection PyRedeclaration
class PQInnerData:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PQInnerData
            PQInnerDataDc
            PQInnerDataTemp
            PQInnerDataTempDc
    """

    QUALNAME = "pyrogram.raw.base.PQInnerData"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/pq-inner-data")
