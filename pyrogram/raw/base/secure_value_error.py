
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SecureValueError = Union[raw.types.SecureValueError, raw.types.SecureValueErrorData, raw.types.SecureValueErrorFile, raw.types.SecureValueErrorFiles, raw.types.SecureValueErrorFrontSide, raw.types.SecureValueErrorReverseSide, raw.types.SecureValueErrorSelfie, raw.types.SecureValueErrorTranslationFile, raw.types.SecureValueErrorTranslationFiles]


# noinspection PyRedeclaration
class SecureValueError:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 9 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecureValueError
            SecureValueErrorData
            SecureValueErrorFile
            SecureValueErrorFiles
            SecureValueErrorFrontSide
            SecureValueErrorReverseSide
            SecureValueErrorSelfie
            SecureValueErrorTranslationFile
            SecureValueErrorTranslationFiles
    """

    QUALNAME = "pyrogram.raw.base.SecureValueError"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/secure-value-error")
