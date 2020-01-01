# -*- coding: utf-8 -*-
"""Art parameters."""
from .text_dic1 import *
from .text_dic2 import *
from .text_dic3 import *
from .art_dic import *

ART_VERSION = "4.4"  # pragma: no cover
FONT_SMALL_THRESHOLD = 50  # pragma: no cover
FONT_MEDIUM_THRESHOLD = 100  # pragma: no cover
FONT_LARGE_THRESHOLD = 200  # pragma: no cover

TEXT_XLARGE_THRESHOLD = 3  # pragma: no cover
TEXT_LARGE_THRESHOLD = 7  # pragma: no cover
TEXT_MEDIUM_THRESHOLD = 10  # pragma: no cover

ART_TYPE_ERROR = "The 'artname' type must be str."
ART_NAME_ERROR = "Invalid art name."
NUMBER_TYPE_ERROR = "The 'number' type must be int."
TEXT_TYPE_ERROR = "The 'text' type must be str."
FONT_TYPE_ERROR = "The 'font' type must be str."
CHR_IGNORE_TYPE_ERROR = "The 'chr_ignore' type must be bool."
FILE_TYPE_ERROR = "The 'filename' type must be str."
PRINT_STATUS_TYPE_ERROR = "The 'print_status' type must be bool."
OVERWRITE_TYPE_ERROR = "The 'overwrite' type must be bool."
ART_ENVIRONMENT_WARNING = "[Warning] '{0}' is not printable in this environment."
FONT_ENVIRONMENT_WARNING = "[Warning] '{0}' is not printable in this environment."
PACKAGE_LOAD_WARNING = "[Warning] There is a problem loading the package 'coverage'."

SMALL_WIZARD_FONT = [
    "contessa",
    "avatar",
    "mini",
    "bigfig",
    "lcd",
    "bubble",
    "digital",
    "twopoint",
    "3x5",
    "threepoint",
    "ascii_new_roman",
    "bulbhead",
    "lockergnome"]  # pragma: no cover
MEDIUM_WIZARD_FONT = [
    "soft",
    "4max",
    "5x7",
    "stampate",
    "o8",
    "standard",
    "alphabet",
    "computer",
    "shadow",
    "speed",
    "rounded",
    "chartri"]  # pragma: no cover
LARGE_WIZARD_FONT = [
    "xhelvi",
    "utopiai",
    "rev",
    "smpoison",
    "3-d",
    "larry3d",
    "nancyj",
    "nancyj-underlined",
    "os2",
    "block2"]  # pragma: no cover
XLARGE_WIZARD_FONT = [
    "dotmatrix",
    "univers",
    "doh",
    "roman",
    "hollywood",
    "georgia11",
    "block"]  # pragma: no cover

UPPERCASE_FONTS = [
    "1943",
    "4x4_offr",
    "64f1",
    "a_zooloo",
    "advenger",
    "aquaplan",
    "assalt_m",
    "asslt_m",
    "atc",
    "atc_gran",
    "battlesh",
    "baz_bil",
    "beer_pub",
    "c1",
    "c2",
    "c_consen",
    "char1",
    "char4",
    "coil_cop",
    "druid",
    "faces_of",
    "fair_mea",
    "fairligh",
    "fantasy",
    "fbr1",
    "fbr12",
    "fbr_stri",
    "fbr_tilt",
    "finalass",
    "fp1",
    "fp2",
    "funky_dr",
    "future_1",
    "future_2",
    "future_3",
    "future_4",
    "future_5",
    "future_6",
    "future_7",
    "future_8",
    "ghost_bo",
    "grand_pr",
    "green_be",
    "hades",
    "heavy_me",
    "heroboti",
    "house_of",
    "hypa_bal",
    "hyper",
    "kgames_i",
    "kik_star",
    "krak_out",
    "tsn_base",
    "ugalympi",
    "unarmed",
    "usa",
    "usa_pq",
    "vortron",
    "war_of_w",
    "yie-ar",
    "yie_ar_k",
    "z-pilot",
    "zig_zag",
    "zone7"]

RANDOM_FILTERED_ARTS = [
    "message2",
    "love you",
    "text decoration",
    "message1",
    "musical"]


NON_ASCII_FONTS = [
    "contouring1",
    "contouring2",
    "contouring3",
    "contouring4",
    "mirror",
    "mirror_flip",
    "flip",
    "white_bubble",
    "smallcaps2",
    "superscript",
    "subscript",
    "full_width",
    "antrophobia",
    "currency",
    "special",
    "dirty",
    "knight",
    "thin2",
    "tiny",
    "love1",
    "love2",
    "fancy1",
    "fancy2",
    "fancy3",
    "fancy4",
    "fancy5",
    "fancy6",
    "fancy7",
    "fancy8",
    "fancy9",
    "fancy10",
    "fancy11",
    "fancy12",
    "fancy13",
    "fancy14",
    "fancy15",
    "fancy16",
    "fancy17",
    "fancy18",
    "fancy19",
    "fancy20",
    "fancy21",
    "fancy22",
    "fancy23",
    "fancy24",
    "fancy25",
    "fancy26",
    "fancy27",
    "fancy28",
    "fancy29",
    "fancy30",
    "symbols",
    "fancy31",
    "fancy32",
    "fancy33",
    "fancy34",
    "fancy35",
    "fancy36",
    "fancy37",
    "fancy38",
    "fancy39",
    "fancy40",
    "fancy41",
    "fancy42",
    "fancy43",
    "fancy44",
    "fancy45",
    "fancy46",
    "fancy47",
    "fancy48",
    "fancy49",
    "fancy50",
    "fancy51",
    "fancy52",
    "fancy53",
    "fancy54",
    "fancy55",
    "fancy56",
    "fancy57",
    "fancy58",
    "fancy59",
    "fancy60",
    "fancy61",
    "fancy62",
    "fancy63",
    "fancy64",
    "fancy65",
    "fancy66",
    "fancy67",
    "fancy68",
    "fancy69",
    "fancy70",
    "fancy71",
    "fancy72",
    "fancy73",
    "fancy74",
    "fancy75",
    "fancy76",
    "fancy77",
    "fancy78",
    "fancy79",
    "fancy80",
    "fancy81",
    "fancy82",
    "fancy83",
    "fancy84",
    "fancy85",
    "fancy86",
    "fancy87",
    "fancy88",
    "fancy89",
    "fancy90",
    "fancy91",
    "fancy92",
    "fancy93",
    "fancy94",
    "fancy95",
    "fancy96",
    "fancy97",
    "fancy98",
    "fancy99",
    "fancy100",
    "white_square",
    "black_square",
    "paranormal",
    "black_bubble",
    "smallcaps3",
    "fraktur2",
    "bold_fraktur",
    "bold_script",
    "handwriting1",
    "handwriting2",
    "rusify",
    "monospace",
    "dirty2",
    "knight2",
    "h4k3r",
    "thin3",
    "tiny2",
    "upside_down",
    "chinese_mafia",
    "sunday_cuddle",
    "native_lands",
    "foreign_friends",
    "atlantic",
    "funky_fresh",
    "greek_legends",
    "minion",
    "hippie",
    "sarah",
    "dwarf",
    "lilia",
    "smooth",
    "smooth2",
    "carrier1",
    "carrier2"]

RANDOM_FILTERED_FONTS = [
    '5x8',
    'binary',
    'decimal',
    'high_noo',
    'hills',
    'katakana',
    'morse',
    'nfi1',
    'octal',
    'rot13',
    'smtengwar',
    'tengwar',
    'tsalagi',
    'gauntlet',
    'flyn_sh',
    'moscow',
    'dwhistled'] + NON_ASCII_FONTS

DESCRIPTION = '''ASCII art is also known as "computer text art".
It involves the smart placement of typed special characters or
letters to make a visual shape that is spread over multiple lines of text.
ART is a Python lib for text converting to ASCII art fancy.'''  # pragma: no cover


FONT_MAP = {"block": [block_dic, True], "banner": [banner_dic, False],  # pragma: no cover
            "standard": [standard_dic, False], "avatar": [avatar_dic, True],
            "basic": [basic_dic, True], "bulbhead": [bulbhead_dic, True],
            "chunky": [chunky_dic, False], "coinstak": [coinstak_dic, False],
            "contessa": [contessa_dic, False], "contrast": [contrast_dic, True],
            "cyberlarge": [cyberlarge_dic, True], "cybermedium": [cybermedium_dic, True],
            "doom": [doom_dic, False], "dotmatrix": [dotmatrix_dic, False],
            "drpepper": [drpepper_dic, False],
            "epic": [epic_dic, True], "fuzzy": [fuzzy_dic, False],
            "isometric1": [isometric1_dic, True], "isometric2": [isometric2_dic, True],
            "isometric3": [isometric3_dic, True], "isometric4": [isometric4_dic, True],
            "larry3d": [larry3d_dic, False],
            "nancyj": [nancyj_dic, False], "ogre": [ogre_dic, False],
            "rectangles": [rectangles_dic, False], "roman": [roman_dic, False],
            "rounded": [rounded_dic, False], "rowancap": [rowancap_dic, True],
            "script": [script_dic, False],
            "serifcap": [serifcap_dic, True], "shadow": [shadow_dic, False],
            "slant": [slant_dic, False], "speed": [speed_dic, False],
            "starwars": [starwars_dic, False], "stop": [stop_dic, False],
            "thin": [thin_dic, False], "usaflag": [usaflag_dic, False],
            "3-d": [dic_3d, False], "3x5": [dic_3x5, False], "5lineoblique":
                [dic_5lineoblique, False], "alphabet": [alphabet_dic, False],
            "banner3-d": [banner3d_dic, True],
            "banner3": [banner3_dic, True], "banner4": [banner4_dic, True],
            "bell": [bell_dic, False], "catwalk": [catwalk_dic, False], "colossal": [colossal_dic, False],
            "acrobatic": [acrobatic_dic, True], "alligator": [alligator_dic, False],
            "alligator2": [alligator2_dic, False], "block2": [block2_dic, True],
            "caligraphy": [caligraphy_dic, True],
            "computer": [computer_dic, True], "digital": [digital_dic, True],
            "doh": [doh_dic, True],
            "eftirobot": [eftirobot_dic, True], "graffiti": [graffiti_dic, True],
            "stellar": [stellar_dic, False], "swan": [swan_dic, False], "tanja": [tanja_dic, False],
            "thick": [thick_dic, False], "threepoint": [threepoint_dic, False],
            "tombstone": [tombstone_dic, True], "trek": [trek_dic, True],
            "twopoint": [twopoint_dic, False], "univers": [univers_dic, False],
            "weird": [weird_dic, False], "pebbles": [pebbles_dic, False],
            "puffy": [puffy_dic, False], "tinker-toy": [tinker_toy_dic, False],
            "straight": [straight_dic, False], "stampatello": [stampatello_dic,
                                                               False],
            "smslant": [smslant_dic, False], "smshadow": [smshadow_dic, False],
            "smscript": [smscript_dic, False], "smkeyboard": [smkeyboard_dic,
                                                              False],
            "smisome1": [smisome1_dic, True], "slscript": [slscript_dic, False],
            "slide": [slide_dic, False], "sblood": [sblood_dic, True],
            "rozzo": [rozzo_dic, False], "pyramid": [pyramid_dic, False],
            "maxfour": [maxfour_dic, False], "nipples": [nipples_dic, False],
            "o8": [o8_dic, False], "peaks": [peaks_dic, False],
            "pawp": [pawp_dic, False],
            "barbwire": [barbwire_dic, False], "bigchief": [bigchief_dic, False],
            "binary": [binary_dic, False], "bubble": [bubble_dic, False],
            "calgphy2": [calgphy2_dic, False],
            "cygnet": [cygnet_dic, False], "diamond": [diamond_dic, False],
            "eftifont": [eftifont_dic, False], "eftitalic": [eftitalic_dic,
                                                             False],
            "eftiwater": [eftiwater_dic, False], "fourtops": [fourtops_dic, False],
            "goofy": [goofy_dic, True], "hollywood": [hollywood_dic, False],
            "invita": [invita_dic, False], "italic": [italic_dic, False],
            "jazmine": [jazmine_dic, False], "lcd": [lcd_dic, False],
            "lean": [lean_dic, False], "letters": [letters_dic, False],
            "lockergnome": [lockergnome_dic, False], "madrid": [madrid_dic, False],
            "marquee": [marquee_dic, False], "mike": [mike_dic, True],
            "mini": [mini_dic, False],
            "nancyj-fancy": [nancyj_fancy_dic, False],
            "nancyj-underlined": [nancyj_underlined_dic, False],
            "pepper": [pepper_dic, False], "poison": [poison_dic, True],
            "rot13": [rot13_dic, False], "short": [short_dic, False],
            "small": [small_dic, False], "tengwar": [tengwar_dic, True],
            "big": [big_dic, False], "1row": [dic_1row, True],
            "3d_diagonal": [dic_3d_diagonal, False],
            "4max": [dic_4max, True],
            "amc3line": [amc3line_dic, True],
            "cybersmall": [cybersmall_dic, True],
            "gothic": [gothic_dic, False],
            "rev": [rev_dic, False],
            "smtengwar": [smtengwar_dic, False],
            "term": [term_dic, False],
            "amcrazor": [amcrazor_dic, True],
            "amcaaa01": [amcaaa01_dic, True],
            "amcneko": [amcneko_dic, False],
            "amcrazo2": [amcrazo2_dic, True],
            "amcslash": [amcslash_dic, False],
            "amcthin": [amcthin_dic, True],
            "amctubes": [amctubes_dic, True],
            "amcun1": [amcun1_dic, False],
            "arrows": [arrows_dic, False],
            "bear": [bear_dic, True],
            "benjamin": [benjamin_dic, True],
            "bigfig": [bigfig_dic, False],
            "bolger": [bolger_dic, False],
            "braced": [braced_dic, True],
            "bright": [bright_dic, True],
            "broadway": [broadway_dic, True],
            "cards": [cards_dic, True],
            "chiseled": [chiseled_dic, True],
            "cola": [cola_dic, False],
            "crawford": [crawford_dic, True],
            "cricket": [cricket_dic, False],
            "danc4": [danc4_dic, False],
            "dancingfont": [dancingfont_dic, True],
            "decimal": [decimal_dic, False],
            "defleppard": [defleppard_dic, True],
            "dietcola": [dietcola_dic, False],
            "double": [double_dic, True],
            "doubleshorts": [doubleshorts_dic, True],
            "eftipiti": [eftipiti_dic, False],
            "filter": [filter_dic, True],
            "flipped": [flipped_dic, True],
            "fraktur": [fraktur_dic, False],
            "funface": [funface_dic, True],
            "funfaces": [funfaces_dic, True],
            "georgi16": [georgi16_dic, False],
            "georgia11": [georgia11_dic, False],
            "ghost": [ghost_dic, True],
            "ghoulish": [ghoulish_dic, True],
            "glenyn": [glenyn_dic, True],
            "graceful": [graceful_dic, True],
            "greek": [greek_dic, False],
            "heartleft": [heartleft_dic, False],
            "heartright": [heartright_dic, False],
            "henry3d": [henry3d_dic, False],
            "horizontalleft": [horizontalleft_dic, True],
            "horizontalright": [horizontalright_dic, True],
            "icl-1900": [ICL_1900_dic, True],
            "impossible": [impossible_dic, True],
            "jacky": [jacky_dic, True],
            "katakana": [katakana_dic, False],
            "keyboard": [keyboard_dic, False],
            "knob": [knob_dic, True],
            "lildevil": [lildevil_dic, True],
            "lineblocks": [lineblocks_dic, True],
            "merlin1": [merlin1_dic, True],
            "merlin2": [merlin2_dic, True],
            "modular": [modular_dic, True],
            "morse": [morse_dic, True],
            "moscow": [moscow_dic, True],
            "muzzle": [muzzle_dic, True],
            "nscript": [nscript_dic, False],
            "nvscript": [nvscript_dic, False],
            "octal": [octal_dic, False],
            "oldbanner": [oldbanner_dic, False],
            "os2": [os2_dic, False],
            "puzzle": [puzzle_dic, True],
            "rammstein": [rammstein_dic, False],
            "red_phoenix": [red_phoenix_dic, False],
            "runyc": [runyc_dic, False],
            "santaclara": [santaclara_dic, False],
            "shimrod": [shimrod_dic, False],
            "smallcaps": [smallcaps_dic, True],
            "smpoison": [smpoison_dic, True],
            "soft": [soft_dic, False],
            "spliff": [spliff_dic, True],
            "stacey": [stacey_dic, True],
            "stampate": [stampate_dic, False],
            "stforek": [stforek_dic, True],
            "sub-zero": [sub_zero_dic, True],
            "swampland": [swampland_dic, True],
            "sweet": [sweet_dic, True],
            "ticks": [ticks_dic, False],
            "ticksslant": [ticksslant_dic, False],
            "tiles": [tiles_dic, False],
            "tsalagi": [tsalagi_dic, False],
            "tubular": [tubular_dic, False],
            "twisted": [twisted_dic, True],
            "varsity": [varsity_dic, False],
            "wavy": [wavy_dic, False],
            "wetletter": [wetletter_dic, True],
            "whimsy": [whimsy_dic, True],
            "wow": [wow_dic, True],
            "alligator3": [alligator3_dic, True],
            "alpha": [alpha_dic, True],
            "amc3liv1": [amc3liv1_dic, True],
            "ascii_new_roman": [ascii_new_roman_dic, True],
            "b1ff": [B1FF_dic, True],
            "dwhistled": [dwhistled_dic, False],
            "eftiwall": [eftiwall_dic, False],
            "fire_font-s": [fire_font_s_dic, False],
            "gradient": [gradient_dic, True],
            "1943": [dic_1943, False],
            "advenger": [advenger_dic, False],
            "char1": [char1_dic, False],
            "char2": [char2_dic, False],
            "char3": [char3_dic, False],
            "char4": [char4_dic, False],
            "charact1": [charact1_dic, False],
            "charact2": [charact2_dic, False],
            "charact3": [charact3_dic, False],
            "charact4": [charact4_dic, False],
            "charact5": [charact5_dic, False],
            "charact6": [charact6_dic, False],
            "characte": [characte_dic, False],
            "chartr": [chartr_dic, False],
            "chartri": [chartri_dic, False],
            "xbrite": [xbrite_dic, False],
            "xbriteb": [xbriteb_dic, False],
            "xbritebi": [xbritebi_dic, False],
            "xbritei": [xbritei_dic, False],
            "xchartr": [xchartr_dic, False],
            "xchartri": [xchartri_dic, False],
            "xcour": [xcour_dic, False],
            "xcourb": [xcourb_dic, False],
            "xcourbi": [xcourbi_dic, False],
            "xcouri": [xcouri_dic, False],
            "xhelv": [xhelv_dic, False],
            "xhelvb": [xhelvb_dic, False],
            "xhelvbi": [xhelvbi_dic, False],
            "xhelvi": [xhelvi_dic, False],
            "xsans": [xsans_dic, False],
            "xsansb": [xsansb_dic, False],
            "xsansbi": [xsansbi_dic, False],
            "xsansi": [xsansi_dic, False],
            "xtimes": [xtimes_dic, False],
            "xttyb": [xttyb_dic, False],
            "heroboti": [heroboti_dic, False],
            "high_noo": [high_noo_dic, False],
            "hills": [hills_dic, False],
            "home_pak": [home_pak_dic, True],
            "house_of": [house_of_dic, False],
            "hypa_bal": [hypa_bal_dic, False],
            "hyper": [hyper_dic, False],
            "inc_raw": [inc_raw_dic, False],
            "italics": [italics_dic, False],
            "kgames_i": [kgames_i_dic, False],
            "4x4_offr": [dic_4x4_offr, False],
            "5x7": [dic_5x7, False],
            "5x8": [dic_5x8, False],
            "6x9": [dic_6x9, False],
            "6x10": [dic_6x10, False],
            "64f1": [dic_64f1, False],
            "a_zooloo": [a_zooloo_dic, False],
            "asc": [asc_dic, False],
            "assalt_m": [assalt_m_dic, False],
            "asslt_m": [asslt__m_dic, False],
            "atc": [atc_dic, False],
            "atc_gran": [atc_gran_dic, False],
            "battlesh": [battlesh_dic, False],
            "baz_bil": [baz_bil_dic, False],
            "beer_pub": [beer_pub_dic, False],
            "c1": [c1_dic, False],
            "c2": [c2_dic, False],
            "kik_star": [kik_star_dic, False],
            "krak_out": [krak_out_dic, False],
            "tsn_base": [tsn_base_dic, False],
            "twin_cob": [twin_cob_dic, False],
            "type_set": [type_set_dic, False],
            "ucf_fan": [ucf_fan_dic, False],
            "ugalympi": [ugalympi_dic, False],
            "unarmed": [unarmed__dic, False],
            "usa": [usa_dic, False],
            "usa_pq": [usa_pq_dic, False],
            "utopia": [utopia_dic, False],
            "utopiab": [utopiab_dic, False],
            "utopiabi": [utopiabi_dic, False],
            "utopiai": [utopiai_dic, False],
            "vortron": [vortron_dic, False],
            "war_of_w": [war_of_w_dic, False],
            "xtty": [xtty_dic, False],
            "love1": [love1_dic, False],
            "yie_ar_k": [yie_ar_k_dic, False],
            "yie-ar": [yie_ar_dic, False],
            "zig_zag": [zig_zag_dic, False],
            "zone7": [zone7_dic, False],
            "z-pilot": [z_pilot_dic, False],
            "aquaplan": [aquaplan_dic, False],
            "ascii": [ascii_dic, False],
            "c_ascii": [c_ascii_dic, False],
            "c_consen": [c_consen_dic, False],
            "clb6x10": [clb6x10_dic, False],
            "clb8x8": [clb8x8_dic, False],
            "clb8x10": [clb8x10_dic, False],
            "cli8x8": [cli8x8_dic, False],
            "clr4x6": [clr4x6_dic, False],
            "clr5x6": [clr5x6_dic, False],
            "clr5x8": [clr5x8_dic, False],
            "clr5x10": [clr5x10_dic, False],
            "clr6x6": [clr6x6_dic, False],
            "clr6x8": [clr6x8_dic, False],
            "clr6x10": [clr6x10_dic, False],
            "clr7x8": [clr7x8_dic, False],
            "clr8x8": [clr8x8_dic, False],
            "clr8x10": [clr8x10_dic, False],
            "coil_cop": [coil_cop_dic, False],
            "contouring1": [contouring1_dic, False],
            "contouring2": [contouring2_dic, True],
            "com_sen": [com_sen_dic, False],
            "druid": [druid_dic, False],
            "e_fist": [e_fist_dic, True],
            "ebbs_1": [ebbs_1_dic, False],
            "ebbs_2": [ebbs_2_dic, False],
            "eca": [eca_dic, False],
            "faces_of": [faces_of_dic, False],
            "fair_mea": [fair_mea_dic, False],
            "fairligh": [fairligh_dic, False],
            "fantasy": [fantasy_dic, False],
            "fbr_stri": [fbr_stri_dic, False],
            "fbr_tilt": [fbr_tilt_dic, False],
            "fbr1": [fbr1_dic, False],
            "fbr2": [fbr2_dic, False],
            "fbr12": [fbr12_dic, False],
            "finalass": [finalass_dic, False],
            "fireing": [fireing_dic, False],
            "flyn_sh": [flyn_sh_dic, False],
            "fp1": [fp1_dic, False],
            "fp2": [fp2_dic, False],
            "funky_dr": [funky_dr_dic, False],
            "future_1": [future_1_dic, False],
            "future_2": [future_2_dic, False],
            "future_3": [future_3_dic, False],
            "future_4": [future_4_dic, False],
            "future_5": [future_5_dic, False],
            "future_6": [future_6_dic, False],
            "future_7": [future_7_dic, False],
            "future_8": [future_8_dic, False],
            "gauntlet": [gauntlet_dic, False],
            "ghost_bo": [ghost_bo_dic, False],
            "grand_pr": [grand_pr_dic, False],
            "green_be": [green_be_dic, False],
            "hades": [hades_dic, False],
            "heavy_me": [heavy_me_dic, False],
            "nfi1": [nfi1_dic, False],
            "flip": [flip_dic, False],
            "mirror": [mirror_dic, False],
            "mirror_flip": [mirror_flip_dic, False],
            "white_bubble": [white_bubble_dic, False],
            "smallcaps2": [smallcaps2_dic, False],
            "superscript": [superscript_dic, False],
            "subscript": [subscript_dic, False],
            "full_width": [full_width_dic, False],
            "antrophobia": [antrophobia_dic, False],
            "currency": [currency_dic, False],
            "special": [special_dic, False],
            "dirty": [dirty_dic, False],
            "dirty2": [dirty2_dic, False],
            "knight": [knight_dic, False],
            "knight2": [knight2_dic, False],
            "thin2": [thin2_dic, False],
            "tiny": [tiny_dic, False],
            "fancy1": [fancy1_dic, False],
            "fancy2": [fancy2_dic, False],
            "fancy3": [fancy3_dic, False],
            "fancy4": [fancy4_dic, False],
            "fancy5": [fancy5_dic, False],
            "fancy6": [fancy6_dic, False],
            "fancy7": [fancy7_dic, False],
            "fancy8": [fancy8_dic, False],
            "fancy9": [fancy9_dic, False],
            "fancy10": [fancy10_dic, False],
            "fancy11": [fancy11_dic, False],
            "fancy12": [fancy12_dic, False],
            "fancy13": [fancy13_dic, False],
            "fancy14": [fancy14_dic, False],
            "fancy15": [fancy15_dic, False],
            "fancy16": [fancy16_dic, False],
            "fancy17": [fancy17_dic, False],
            "fancy18": [fancy18_dic, False],
            "fancy19": [fancy19_dic, False],
            "fancy20": [fancy20_dic, False],
            "fancy21": [fancy21_dic, False],
            "fancy22": [fancy22_dic, False],
            "fancy23": [fancy23_dic, False],
            "fancy24": [fancy24_dic, False],
            "fancy25": [fancy25_dic, False],
            "fancy26": [fancy26_dic, False],
            "fancy27": [fancy27_dic, False],
            "fancy28": [fancy28_dic, False],
            "fancy29": [fancy29_dic, False],
            "fancy30": [fancy30_dic, False],
            "symbols": [symbols_dic, False],
            "fancy31": [fancy31_dic, False],
            "fancy32": [fancy32_dic, False],
            "fancy33": [fancy33_dic, False],
            "fancy34": [fancy34_dic, False],
            "fancy35": [fancy35_dic, False],
            "fancy36": [fancy36_dic, False],
            "fancy37": [fancy37_dic, False],
            "fancy38": [fancy38_dic, False],
            "fancy39": [fancy39_dic, False],
            "fancy40": [fancy40_dic, False],
            "fancy41": [fancy41_dic, False],
            "fancy42": [fancy42_dic, False],
            "fancy43": [fancy43_dic, False],
            "fancy44": [fancy44_dic, False],
            "fancy45": [fancy45_dic, False],
            "fancy46": [fancy46_dic, False],
            "fancy47": [fancy47_dic, False],
            "fancy48": [fancy48_dic, False],
            "fancy49": [fancy49_dic, False],
            "fancy50": [fancy50_dic, False],
            "fancy51": [fancy51_dic, False],
            "fancy52": [fancy52_dic, False],
            "fancy53": [fancy53_dic, False],
            "fancy54": [fancy54_dic, False],
            "fancy55": [fancy55_dic, False],
            "fancy56": [fancy56_dic, False],
            "fancy57": [fancy57_dic, False],
            "fancy58": [fancy58_dic, False],
            "fancy59": [fancy59_dic, False],
            "fancy60": [fancy60_dic, False],
            "fancy61": [fancy61_dic, False],
            "fancy62": [fancy62_dic, False],
            "fancy63": [fancy63_dic, False],
            "fancy64": [fancy64_dic, False],
            "fancy65": [fancy65_dic, False],
            "fancy66": [fancy66_dic, False],
            "fancy67": [fancy67_dic, False],
            "fancy68": [fancy68_dic, False],
            "fancy69": [fancy69_dic, False],
            "fancy70": [fancy70_dic, False],
            "fancy71": [fancy71_dic, False],
            "fancy72": [fancy72_dic, False],
            "fancy73": [fancy73_dic, False],
            "fancy74": [fancy74_dic, False],
            "fancy75": [fancy75_dic, False],
            "fancy76": [fancy76_dic, False],
            "fancy77": [fancy77_dic, False],
            "fancy78": [fancy78_dic, False],
            "fancy79": [fancy79_dic, False],
            "fancy80": [fancy80_dic, False],
            "fancy81": [fancy81_dic, False],
            "fancy82": [fancy82_dic, False],
            "fancy83": [fancy83_dic, False],
            "fancy84": [fancy84_dic, False],
            "contouring3": [contouring3_dic, False],
            "contouring4": [contouring4_dic, False],
            "love2": [love2_dic, False],
            "fancy85": [fancy85_dic, False],
            "fancy86": [fancy86_dic, False],
            "white_square": [white_square_dic, False],
            "black_square": [black_square_dic, False],
            "paranormal": [paranormal_dic, False],
            "black_bubble": [black_bubble_dic, False],
            "smallcaps3": [smallcaps3_dic, False],
            "fraktur2": [fraktur2_dic, False],
            "bold_fraktur": [bold_fraktur_dic, False],
            "bold_script": [bold_script_dic, False],
            "handwriting1": [handwriting1_dic, False],
            "handwriting2": [handwriting2_dic, False],
            "rusify": [rusify_dic, False],
            "monospace": [monospace_dic, False],
            "h4k3r": [h4k3r_dic, False],
            "thin3": [thin3_dic, False],
            "tiny2": [tiny2_dic, False],
            "upside_down": [upside_down_dic, False],
            "chinese_mafia": [chinese_mafia_dic, False],
            "sunday_cuddle": [sunday_cuddle_dic, False],
            "native_lands": [native_lands_dic, False],
            "foreign_friends": [foreign_friends_dic, False],
            "atlantic": [atlantic_dic, False],
            "funky_fresh": [funky_fresh_dic, False],
            "greek_legends": [greek_legends_dic, False],
            "minion": [minion_dic, False],
            "hippie": [hippie_dic, False],
            "sarah": [sarah_dic, False],
            "fancy87": [fancy87_dic, False],
            "fancy88": [fancy88_dic, False],
            "fancy89": [fancy89_dic, False],
            "fancy90": [fancy90_dic, False],
            "fancy91": [fancy91_dic, False],
            "fancy92": [fancy92_dic, False],
            "dwarf": [dwarf_dic, False],
            "lilia": [lilia_dic, False],
            "fancy93": [fancy93_dic, False],
            "fancy94": [fancy94_dic, False],
            "fancy95": [fancy95_dic, False],
            "smooth": [smooth_dic, False],
            "fancy96": [fancy96_dic, False],
            "fancy97": [fancy97_dic, False],
            "fancy98": [fancy98_dic, False],
            "fancy99": [fancy99_dic, False],
            "smooth2": [smooth2_dic, False],
            "carrier1": [carrier_dic, False],
            "fancy100": [fancy100_dic, False],
            "carrier2": [carrier2_dic, False]
            }

FONT_NAMES = sorted(list(FONT_MAP.keys()))  # pragma: no cover
ART_NAMES = sorted(list(art_dic.keys()))  # pragma: no cover
FONT_COUNTER = len(FONT_NAMES)  # pragma: no cover
ART_COUNTER = len(ART_NAMES)  # pragma: no cover
DEFAULT_FONT = "standard"  # pragma: no cover
