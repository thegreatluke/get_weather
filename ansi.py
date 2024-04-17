# pylint: disable=line-too-long, too-few-public-methods

"""
ANSI Support in OOP style.
"""

import rainbow


class ControlSequences:
    """
    Predefined common ANSI SGRs that are used extensively.
    """
    MODIFIER_RESET                 = "\x1b[0m"
    DECORATION_PREFIX_BOLD         = "\x1b[1m"
    DECORATION_PREFIX_ITALIC       = "\x1b[3m"
    DECORATION_PREFIX_UNDERLINE    = "\x1b[4m"
    DECORATION_PREFIX_BLINK        = "\x1b[5m"
    DECORATION_PREFIX_VIDINVERT    = "\x1b[7m"
    DECORATION_PREFIX_STRIKE       = "\x1b[9m"
    DECORATION_PREFIX_DBLUNDERLINE = "\x1b[21m"
    CURSOR_HIDE                    = "\x1b[?25l"
    CURSOR_SHOW                    = "\x1b[?25h"


class ATDecoration:
    """
    Codified ANSI decorators.
    """
    def __init__(self, **kwargs):
        self.bold         = kwargs['bold'] if 'bold' in kwargs else False
        self.italic       = kwargs['italic'] if 'italic' in kwargs else False
        self.underline    = kwargs['underline'] if 'underline' in kwargs else False
        self.blink        = kwargs['blink'] if 'blink' in kwargs else False
        self.vidinvert    = kwargs['vidinvert'] if 'video_invert' in kwargs else False
        self.strike       = kwargs['strike'] if 'strike' in kwargs else False
        self.dblunderline = kwargs['dblunderline'] if 'dblunderline' in kwargs else False

    def to_ansi_str(self):
        """
        Returns the data in this class as an ANSI escape string.
        """
        a = ''

        if self.bold:
            a += f"{ControlSequences.DECORATION_PREFIX_BOLD}"
        if self.italic:
            a += f"{ControlSequences.DECORATION_PREFIX_ITALIC}"
        if self.underline:
            a += f"{ControlSequences.DECORATION_PREFIX_UNDERLINE}"
        if self.blink:
            a += f"{ControlSequences.DECORATION_PREFIX_BLINK}"
        if self.vidinvert:
            a += f"{ControlSequences.DECORATION_PREFIX_VIDINVERT}"
        if self.strike:
            a += f"{ControlSequences.DECORATION_PREFIX_STRIKE}"
        if self.dblunderline:
            a += f"{ControlSequences.DECORATION_PREFIX_DBLUNDERLINE}"

        return a


class ATDecorationNone(ATDecoration):
    """
    Symbolic placeholder for no decorations.
    """
    def to_ansi_str(self):
        """
        Return an empty string since we want no decorations.
        """
        return ''


class ATCoordinates:
    """
    Representation of coordinates in the terminal space.
    """
    def __init__(self, **kwargs):
        self.row = kwargs['row'] if 'row' in kwargs else 1
        self.col = kwargs['col'] if 'col' in kwargs else 1

    def to_ansi_str(self):
        """
        Returns the data in this class as an ANSI escape string.
        """
        return f"\x1b[{self.row};{self.col}H"


class ATCoordinatesNone(ATCoordinates):
    """
    Symbolic placeholder for no coordinates.
    """
    def to_ansi_str(self):
        """
        Return an empty string since we want no coordinates.
        """
        return ''


class ATCoordinatesDefault(ATCoordinates):
    """
    Symbolic placeholder for default coordinates.
    """
    def __init__(self):
        super().__init__(row=1, col=18)


class ATStringPrefix:
    """
    Defines the prefix component of an ANSI-terminated string.
    The prefix is a way to collate SGR modifiers for text that can be used in an
    OOP fashion.
    """
    def __init__(self, **kwargs):
        self.fgcol  = kwargs['fgcol'] if 'fgcol' in kwargs else rainbow.ForegroundColorNone()
        self.bgcol  = kwargs['bgcol'] if 'bgcol' in kwargs else rainbow.BackgroundColorNone()
        self.deco   = kwargs['deco'] if 'deco' in kwargs else ATDecorationNone()
        self.coords = kwargs['coords'] if 'coords' in kwargs else ATCoordinatesNone()

    def to_ansi_str(self):
        """
        Returns the data in this class as an ANSI escape string.
        """
        return f"{self.fgcol.to_fg_str()}{self.bgcol.to_bg_str()}{self.deco.to_ansi_str()}{self.coords.to_ansi_str()}"


class ATStringPrefixNone(ATStringPrefix):
    """
    Symbolic placeholder for no ATStringPrefix.
    """
    def to_ansi_str(self):
        """
        Return an empty string since we want no prefix.
        """
        return ''


class ATString:
    """
    Defines an ANSI-terminated string.
    This class collates a ATStringPrefix with user data (string of text) and a SGR
    modifier reset.
    """
    def __init__(self, **kwargs):
        self.prefix   = kwargs['prefix'] if 'prefix' in kwargs else ATStringPrefixNone()
        self.udata    = kwargs['udata'] if 'udata' in kwargs else ''
        self.usereset = kwargs['usereset'] if 'userest' in kwargs else True

    def to_ansi_str(self):
        """
        Returns the data in this class as an ANSI escape string.
        """
        a = ''

        a += f"{self.prefix.to_ansi_str()}{self.udata}"
        if self.usereset:
            a += f"{ControlSequences.MODIFIER_RESET}"

        return a


class ATStringNone(ATString):
    """
    Symbolic placeholder for no ATString.
    """
    def to_ansi_str(self):
        """
        Return an empty string since we want no ATString.
        """
        return ''


class ATStringComposite:
    """
    Defines a collection of ATStrings.
    This object is useful for allowing individual words in a sentence to be manipulated
    without affecting others.
    """
    def __init__(self, **kwargs):
        self.composite = kwargs['comp'] if 'comp' in kwargs else []

    def to_ansi_str(self):
        """
        Returns all of the ATStrings contained here in a single string.
        """
        a = ''

        for b in self.composite:
            a += f"{b.to_ansi_str()}"

        return a


# THIS ISN'T NEEDED FOR THIS PROGRAM
#
# class ATSceneImageString(ATString):
#     """
#     A specialization of the ATString class meant to be used when describing "images".
#     """
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.prefix.fgcol = rainbow.ForegroundColorNone()
#         self.prefix.deco  = ATDecorationNone()
#         self.udata        = ' '
#         self.usereset     = True
