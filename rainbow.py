# pylint: disable=line-too-long, too-many-lines

"""
Provides 24-bit color definitions for use by ANSI Escape Sequence functions.
"""

import random


class ConsoleColor:
    """
    Base definition of a 24-bit color.
    """
    def __init__(self, **kwargs):
        self.red   = kwargs['red'] if 'red' in kwargs else 0
        self.green = kwargs['green'] if 'green' in kwargs else 0
        self.blue  = kwargs['blue'] if 'blue' in kwargs else 0

    def to_ansi_str(self):
        """
        Returns the red, green, and blue channels as an ANSI 24-bit formatted suffix.
        This function isn't intended to be used on its own.
        """
        return f"{self.red};{self.green};{self.blue}m"

    def to_fg_str(self):
        """
        Returns the color channels as an ANSI 24-bit color foreground string.
        """
        return f"\x1b[38;2;{self.to_ansi_str()}"

    def to_bg_str(self):
        """
        Returns the color channels as an ANSI 24-bit color background string.
        """
        return f"\x1b[48;2;{self.to_ansi_str()}"


class ForegroundColor(ConsoleColor):
    """
    Foundation class for colors used in the foreground.
    """


class ForegroundColorNone(ConsoleColor):
    """
    Specialization meant to be used for no foreground color.
    """
    def to_ansi_str(self):
        return ''


class BackgroundColor(ConsoleColor):
    """
    Foundation class for colors used in the background.
    """


class BackgroundColorNone(ConsoleColor):
    """
    Specialization meant to be used for no background color.
    """
    def to_ansi_str(self):
        return ''


class CCBlack(ConsoleColor):
    """
    The color black.
    """


class CCWhite(ConsoleColor):
    """
    The color white.
    """
    def __init__(self):
        super().__init__(red=255, green=255, blue=255)


class CCRed(ConsoleColor):
    """
    The color red.
    """
    def __init__(self):
        super().__init__(red=255)


class CCGreen(ConsoleColor):
    """
    The color green.
    """
    def __init__(self):
        super().__init__(green=255)


class CCBlue(ConsoleColor):
    """
    The color blue.
    """
    def __init__(self):
        super().__init__(blue=255)


class CCYellow(ConsoleColor):
    """
    The color yellow.
    """
    def __init__(self):
        super().__init__(red=255, green=255)


class CCDarkYellow(ConsoleColor):
    """
    The color dark yellow.
    """
    def __init__(self):
        super().__init__(red=255, green=204)


class CCDarkCyan(ConsoleColor):
    """
    The color dark cyan.
    """
    def __init__(self):
        super().__init__(green=139, blue=139)


class CCDarkGrey(ConsoleColor):
    """
    The color dark grey.
    """
    def __init__(self):
        super().__init__(red=45, green=45, blue=45)


class CCRandom(ConsoleColor):
    """
    Generate a random color.
    """
    def __init__(self):
        super().__init__(red=random.randint(0, 255), green=random.randint(0, 255), blue=random.randint(0, 255))


class CCAppleNRedLight(ConsoleColor):
    """
    Neutral Red Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=59, blue=48)


class CCAppleNRedDark(ConsoleColor):
    """
    Neutral Red Dark from Apple's Color Pallette.
    """
    def __init__(self):
        super().__init__(red=255, green=69, blue=58)


class CCAppleNRedALight(ConsoleColor):
    """
    Neutral Accessible Red Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=215, blue=21)


class CCAppleNRedADark(ConsoleColor):
    """
    Neutral Accessible Red Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=105, blue=97)


class CCAppleNOrangeLight(ConsoleColor):
    """
    Neutral Orange Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=149)


class CCAppleNOrangeDark(ConsoleColor):
    """
    Neutral Orange Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=159, blue=10)


class CCAppleNOrangeALight(ConsoleColor):
    """
    Neutral Accessible Orange Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=201, green=52)


class CCAppleNOrangeADark(ConsoleColor):
    """
    Neutral Accessible Orange Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=179, blue=64)


class CCAppleNYellowLight(ConsoleColor):
    """
    Neutral Yellow Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=204)


class CCAppleNYellowDark(ConsoleColor):
    """
    Neutral Yellow Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=214, blue=10)


class CCAppleNYellowALight(ConsoleColor):
    """
    Neutral Accessible Yellow Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=178, green=80)


class CCAppleNYellowADark(ConsoleColor):
    """
    Neutral Accessible Yellow Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=212, blue=38)


class CCAppleNGreenLight(ConsoleColor):
    """
    Neutral Green Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=52, green=199, blue=89)


class CCAppleNGreenDark(ConsoleColor):
    """
    Neutral Green Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=48, green=209, blue=88)


class CCAppleNGreenALight(ConsoleColor):
    """
    Neutral Accessible Green Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=36, green=138, blue=61)


class CCAppleNGreenADark(ConsoleColor):
    """
    Neutral Accessible Green Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=48, green=219, blue=91)


class CCAppleNMintLight(ConsoleColor):
    """
    Neutral Mint Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=199, blue=190)


class CCAppleNMintDark(ConsoleColor):
    """
    Neutral Mint Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=99, green=230, blue=226)


class CCAppleNMintALight(ConsoleColor):
    """
    Neutral Accessible Mint Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=12, green=129, blue=123)


class CCAppleNMintADark(ConsoleColor):
    """
    Neutral Accessible Mint Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=102, green=212, blue=207)


class CCAppleNTealLight(ConsoleColor):
    """
    Neutral Teal Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=48, green=176, blue=199)


class CCAppleNTealDark(ConsoleColor):
    """
    Neutral Teal Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=64, green=200, blue=224)


class CCAppleNTealALight(ConsoleColor):
    """
    Neutral Accessible Teal Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=130, blue=153)


class CCAppleNTealADark(ConsoleColor):
    """
    Neutral Accessible Teal Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=93, green=230, blue=255)


class CCAppleNCyanLight(ConsoleColor):
    """
    Neutral Cyan Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=50, green=173, blue=230)


class CCAppleNCyanDark(ConsoleColor):
    """
    Neutral Cyan Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=100, green=210, blue=255)


class CCAppleNCyanALight(ConsoleColor):
    """
    Neutral Accessible Cyan Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=113, blue=164)


class CCAppleNCyanADark(ConsoleColor):
    """
    Neutral Accessible Cyan Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=112, green=215, blue=255)


class CCAppleNBlueLight(ConsoleColor):
    """
    Neutral Blue Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=122, blue=255)


class CCAppleNBlueDark(ConsoleColor):
    """
    Neutral Blue Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=10, green=132, blue=255)


class CCAppleNBlueALight(ConsoleColor):
    """
    Neutral Accessible Blue Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=64, blue=221)


class CCAppleNBlueADark(ConsoleColor):
    """
    Neutral Accessible Blue Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=64, green=156, blue=255)


class CCAppleNIndigoLight(ConsoleColor):
    """
    Neutral Indigo Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=88, blue=86, green=214)


class CCAppleNIndigoDark(ConsoleColor):
    """
    Neutral Indigo Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=94, green=92, blue=230)


class CCAppleNIndigoALight(ConsoleColor):
    """
    Neutral Accessible Indigo Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=54, green=52, blue=163)


class CCAppleNIndigoADark(ConsoleColor):
    """
    Neutral Accessible Indigo Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=125, green=122, blue=255)


class CCAppleNPurpleLight(ConsoleColor):
    """
    Neutral Purple Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=175, green=82, blue=222)


class CCAppleNPurpleDark(ConsoleColor):
    """
    Neutral Purple Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=191, green=90, blue=242)


class CCAppleNPurpleALight(ConsoleColor):
    """
    Neutral Accessible Purple Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=137, green=68, blue=171)


class CCAppleNPurpleADark(ConsoleColor):
    """
    Neutral Accessible Purple Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=218, green=143, blue=255)


class CCAppleNPinkLight(ConsoleColor):
    """
    Neutral Pink Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=45, blue=85)


class CCAppleNPinkDark(ConsoleColor):
    """
    Neutral Pink Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=55, blue=95)


class CCAppleNPinkALight(ConsoleColor):
    """
    Neutral Accessible Pink Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=211, green=15, blue=69)


class CCAppleNPinkADark(ConsoleColor):
    """
    Neutral Accessible Pink Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=100, blue=130)


class CCAppleNBrownLight(ConsoleColor):
    """
    Neutral Brown Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=162, green=132, blue=94)


class CCAppleNBrownDark(ConsoleColor):
    """
    Neutral Brown Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=172, green=142, blue=104)


class CCAppleNBrownALight(ConsoleColor):
    """
    Neutral Accessible Brown Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=127, green=101, blue=69)


class CCAppleNBrownADark(ConsoleColor):
    """
    Neutral Accessible Brown Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=181, green=148, blue=105)


class CCAppleNGreyLight(ConsoleColor):
    """
    Neutral Grey Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=142, green=142, blue=147)


class CCAppleNGreyDark(ConsoleColor):
    """
    Neutral Grey Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=142, green=142, blue=147)


class CCAppleNGreyALight(ConsoleColor):
    """
    Neutral Accessible Grey Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=108, green=108, blue=112)


class CCAppleNGreyADark(ConsoleColor):
    """
    Neutral Accessible Grey Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=174, green=174, blue=178)


class CCAppleNGrey2Light(ConsoleColor):
    """
    Neutral Grey2 Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=174, green=174, blue=178)


class CCAppleNGrey2Dark(ConsoleColor):
    """
    Neutral Grey2 Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=99, green=99, blue=102)


class CCAppleNGrey2ALight(ConsoleColor):
    """
    Neutral Accessible Grey2 Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=142, green=142, blue=147)


class CCAppleNGrey2ADark(ConsoleColor):
    """
    Neutral Accessible Grey2 Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=124, green=124, blue=128)


class CCAppleNGrey3Light(ConsoleColor):
    """
    Neutral Grey3 Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=199, green=199, blue=204)


class CCAppleNGrey3Dark(ConsoleColor):
    """
    Neutral Grey3 Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=72, green=72, blue=74)


class CCAppleNGrey4ALight(ConsoleColor):
    """
    Neutral Accessible Grey4 Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=188, green=188, blue=192)


class CCAppleNGrey4ADark(ConsoleColor):
    """
    Neutral Accessible Grey4 Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=68, green=68, blue=70)


class CCAppleNGrey5Light(ConsoleColor):
    """
    Neutral Grey5 Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=229, green=229, blue=234)


class CCAppleNGrey5Dark(ConsoleColor):
    """
    Neutral Grey5 Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=44, green=44, blue=46)


class CCAppleNGrey5ALight(ConsoleColor):
    """
    Neutral Accessible Grey5 Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=216, green=216, blue=220)


class CCAppleNGrey5ADark(ConsoleColor):
    """
    Neutral Accessible Grey5 Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=54, green=54, blue=56)


class CCAppleNGrey6Light(ConsoleColor):
    """
    Neutral Grey6 Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=242, green=242, blue=247)


class CCAppleNGrey6Dark(ConsoleColor):
    """
    Neutral Grey6 Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=28, green=28, blue=30)


class CCAppleNGrey6ALight(ConsoleColor):
    """
    Neutral Accessible Grey6 Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=235, green=235, blue=240)


class CCAppleNGrey6ADark(ConsoleColor):
    """
    Neutral Accessible Grey6 Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=36, green=36, blue=38)


class CCAppleVRedLight(ConsoleColor):
    """
    Vibrant Red Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=49, blue=38)


class CCAppleVRedDark(ConsoleColor):
    """
    Vibrant Red Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=79, blue=68)


class CCAppleVRedALight(ConsoleColor):
    """
    Vibrant Accessible Red Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=194, green=6, blue=24)


class CCAppleVRedADark(ConsoleColor):
    """
    Vibrant Accessible Red Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=65, blue=54)


class CCAppleVOrangeLight(ConsoleColor):
    """
    Vibrant Orange Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=245, green=139)


class CCAppleVOrangeDark(ConsoleColor):
    """
    Vibrant Orange Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=169, blue=20)


class CCAppleVOrangeALight(ConsoleColor):
    """
    Vibrant Accessible Orange Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=173, green=58)


class CCAppleVOrangeADark(ConsoleColor):
    """
    Vibrant Accessible Orange Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=179, blue=64)


class CCAppleVYellowLight(ConsoleColor):
    """
    Vibrant Yellow Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=245, green=194)


class CCAppleVYellowDark(ConsoleColor):
    """
    Vibrant Yellow Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=224, blue=20)


class CCAppleVYellowALight(ConsoleColor):
    """
    Vibrant Accessible Yellow Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=146, green=81)


class CCAppleVYellowADark(ConsoleColor):
    """
    Vibrant Accessible Yellow Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=212, blue=38)


class CCAppleVGreenLight(ConsoleColor):
    """
    Vibrant Green Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=30, green=195, blue=55)


class CCAppleVGreenDark(ConsoleColor):
    """
    Vibrant Green Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=60, green=225, blue=85)


class CCAppleVGreenALight(ConsoleColor):
    """
    Vibrant Accessible Green Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=112, blue=24)


class CCAppleVGreenADark(ConsoleColor):
    """
    Vibrant Accessible Green Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=49, green=222, blue=75)


class CCAppleVMintLight(ConsoleColor):
    """
    Vibrant Mint Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=189, blue=180)


class CCAppleVMintDark(ConsoleColor):
    """
    Vibrant Mint Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=108, green=224, blue=219)


class CCAppleVMintALight(ConsoleColor):
    """
    Vibrant Accessible Mint Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=11, green=117, blue=112)


class CCAppleVMintADark(ConsoleColor):
    """
    Vibrant Accessible Mint Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=49, green=222, blue=75)


class CCAppleVTealLight(ConsoleColor):
    """
    Vibrant Teal Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=46, green=167, blue=189)


class CCAppleVTealDark(ConsoleColor):
    """
    Vibrant Teal Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=68, green=212, blue=237)


class CCAppleVTealALight(ConsoleColor):
    """
    Vibrant Accessible Teal Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=119, blue=140)


class CCAppleVTealADark(ConsoleColor):
    """
    Vibrant Accessible Teal Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=93, green=230, blue=255)


class CCAppleVCyanLight(ConsoleColor):
    """
    Vibrant Cyan Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=65, green=175, blue=220)


class CCAppleVCyanDark(ConsoleColor):
    """
    Vibrant Cyan Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=90, green=205, blue=250)


class CCAppleVCyanALight(ConsoleColor):
    """
    Vibrant Accessible Cyan Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=103, blue=150)


class CCAppleVCyanADark(ConsoleColor):
    """
    Vibrant Accessible Cyan Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=112, green=215, blue=255)


class CCAppleVBlueLight(ConsoleColor):
    """
    Vibrant Blue Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=112, blue=245)


class CCAppleVBlueDark(ConsoleColor):
    """
    Vibrant Blue Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=20, green=142, blue=255)


class CCAppleVBlueALight(ConsoleColor):
    """
    Vibrant Accessible Blue Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(green=64, blue=221)


class CCAppleVBlueADark(ConsoleColor):
    """
    Vibrant Accessible Blue Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=64, green=156, blue=255)


class CCAppleVIndigoLight(ConsoleColor):
    """
    Vibrant Indigo Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=84, green=82, blue=204)


class CCAppleVIndigoDark(ConsoleColor):
    """
    Vibrant Indigo Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=99, green=97, blue=242)


class CCAppleVIndigoALight(ConsoleColor):
    """
    Vibrant Accessible Indigo Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=54, green=52, blue=163)


class CCAppleVIndigoADark(ConsoleColor):
    """
    Vibrant Accessible Indigo Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=125, green=122, blue=222)


class CCAppleVPurpleLight(ConsoleColor):
    """
    Vibrant Purple Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=159, green=75, blue=201)


class CCAppleVPurpleDark(ConsoleColor):
    """
    Vibrant Purple Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=204, green=101, blue=255)


class CCAppleVPurpleALight(ConsoleColor):
    """
    Vibrant Accessible Purple Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=173, green=68, blue=171)


class CCAppleVPurpleADark(ConsoleColor):
    """
    Vibrant Accessible Purple Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=218, green=143, blue=255)


class CCAppleVPinkLight(ConsoleColor):
    """
    Vibrant Pink Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=245, green=35, blue=75)


class CCAppleVPinkDark(ConsoleColor):
    """
    Vibrant Pink Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=65, blue=105)


class CCAppleVPinkALight(ConsoleColor):
    """
    Vibrant Accessible Pink Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=193, green=16, blue=50)


class CCAppleVPinkADark(ConsoleColor):
    """
    Vibrant Accessible Pink Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=255, green=58, blue=95)


class CCAppleVBrownLight(ConsoleColor):
    """
    Vibrant Brown Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=152, green=122, blue=84)


class CCAppleVBrownDark(ConsoleColor):
    """
    Vibrant Brown Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=182, green=152, blue=114)


class CCAppleVBrownALight(ConsoleColor):
    """
    Vibrant Accessible Brown Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=119, green=93, blue=59)


class CCAppleVGreyLight(ConsoleColor):
    """
    Virbant Grey Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=132, green=132, blue=137)


class CCAppleVGreyDark(ConsoleColor):
    """
    Vibrant Grey Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=162, green=162, blue=167)


class CCAppleVGreyALight(ConsoleColor):
    """
    Vibrant Accessible Grey Light from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=97, green=97, blue=101)


class CCAppleVGreyADark(ConsoleColor):
    """
    Vibrant Accessible Grey Dark from Apple's Color Palette.
    """
    def __init__(self):
        super().__init__(red=152, green=152, blue=157)


class CCTextDefault(CCAppleNGrey5Light):
    """
    Default color used for all text.
    """


class CCListItemHighlight(CCAppleNPinkLight):
    """
    Default color used for list highlights.
    """
