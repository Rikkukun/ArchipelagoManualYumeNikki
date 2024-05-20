# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class EffectsForEnding(Range):
    """How many Effects do you need to obtain to see the Ending
    - 24: same as in the original game
    - 0: you can reach the Ending as soon as you start the seed"""
    display_name = "Effects Required For Ending"
    range_start = 0
    range_end = 24
    default = 24

class LogicDifficulty(Choice):
    """Yume Nikki has a huge map and some entrances which, by a gameplay standpoint, are questionable at best
    The logic selection is here to grant players a choice to prevent some unfun map traversal which would be in logic in almost every seed otherwise, and also buff the Nexus Keys items
    In Easy logic:
    - You are only expected to reach Stairway of Hands after having access to all five beds in the dream world (Madotsuki Room, Snow World, Block World, Candle World and Number World)
    - You are not expected to traverse Hell/Red Maze to reach Forest, Eyeball, Neon and Candle World. You are still expected to reach Docks and Witch Island through Hell though since it's the only way
    - Lamp effect is required in all the dark rooms
    In Mean logic all the above preventions are ignored
    No Logic ignores all logic and therefore seeds could easily result in unbeatable seeds. Don't know why you would play this in Archipelago but it's available"""
    display_name = "Logic Difficulty"
    option_easy = 0
    option_mean = 1
    option_no_logic = 2
    default = 0
    
class LockNexusDoors(DefaultOnToggle):
    """The doors in the Nexus have been locked!
    Find the respective Keys to access the worlds. You always start with a random Nexus Key"""
    display_name = "Lock Nexus Doors"
    
class FunEffects(Toggle):
    """Gives custom logic requirements to certain Effects that otherwise don't have any utility:
    - Towel is required to access the Stairway of Hands by interacting with the beds in the dream world (Towel resembles a bed sheet)
    - Frog is required to access Pink Sea (Based on the Frog's property of giving 2x speed in water)
    - Flute is required to get an item from Masada by playing next to him
    - Demon is required to use the shortcut from FC World to FC House by talking to RNG Demon (100% chance to spawn with Demon equipped)
    - Nopperabou is required to access FC World by interacting with the Pirori in the Ghost Town (Pirori have no face like Nopperabou)
    - Triangle Kerchief is required to get the item from Ghost Madotsuki
    - Poop Hair is required to access Restrooms"""
    display_name = "Fun Effects Mode"

class Eventsanity(DefaultOnToggle):
    """You get items from seeing certain events in Yume Nikki
    Events which require RNG are excluded
    You have to turn this on to make the option Lock Nexus Doors work (otherwise there won't be enough available locations to place Nexus Keys)"""
    display_name = "Eventsanity"
    
class EventsanityRng(Toggle):
    """You get items from seeing certain events which require lucky RNG (Uboa, FACE, Falling Man, Takofuusen, FC Glitch, Melting Madotsuki)
    Activate this at your own risk"""
    display_name = "Eventsanity RNG"
    
class ShuffleVendingMachines(Toggle):
    """You get an item for making a purchase at the three Vending Machines
    Knife is expected in logic in order to obtain money"""
    display_name = "Vending Machines Sanity"

class ShuffleRestrooms(Toggle):
    """You get an item from the two Restrooms in Graffiti World and Block World
    In Fun Effects Mode you need Poop Hair to get these two items"""
    display_name = "Vending Machines Sanity"
    
class SeparateFrogs(DefaultOnToggle):
    """There are two locations where you can obtain the Frog effect: Forest World and Dense Woods
    No: you obtain a single item from any of the two locations
    Yes: you obtain an item from each of the two locations"""
    display_name = "Separate Frogs"
    
class Knifesanity(Toggle):
    """NOT YET IMPLEMENTED"""
    display_name = "Knifesanity"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["effects_for_ending"] = EffectsForEnding
    options["logic_difficulty"] = LogicDifficulty
    options["lock_nexus_doors"] = LockNexusDoors
    options["fun_effects_mode"] = FunEffects
    options["eventsanity"] = Eventsanity
    options["event_rngchance_sanity"] = EventsanityRng
    options["shuffle_vending_machines"] = ShuffleVendingMachines
    options["shuffle_restrooms"] = ShuffleRestrooms
    options["separate_frogs"] = SeparateFrogs
    options["knifesanity"] = Knifesanity
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options