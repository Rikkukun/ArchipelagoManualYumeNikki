# Archipelago Manual for Yume Nikki

This is an Archipelago implementation for the freeware game Yume Nikki using the manual Archipelago Client.

You can download the game for free [here](https://store.steampowered.com/app/650700/Yume_Nikki/) on Steam.

It is highly advised to use a save file with all the 24 effects already obtained. If you want to go even further you can use a save file with all the effects dropped on the ground in the Nexus as eggs, and picking them up as you receive them from the multiworld.


# How this works

With the most basic yaml settings: the 24 effects and Instructions are shuffled in the item pool.

The goal is reaching the ending after having obtained the 24 effects from the multiworld.


# Yaml Options

## Effects Required for Ending

You can choose the number of effects needed to reach the ending. Number from 0 to 24.


## Lock Nexus Doors

This setting locks the 12 doors in the Nexus.

Find the respective Keys to access the worlds.

If this setting is active you will always start with a random Nexus Key.

This setting only adds items to the multiworld but zero locations, so in order to not break generation you need to shuffle at least events when playing with this option.


## Shuffle Events

This setting shuffles various Yume Nikki events in the item pool, listed below.

- **Toriningen Party**
- **Witch's Flight**
- **Monoe**
- **Monoko**
- **Mars-san**
- **Play with Masada** (More on this in the Fun Effects Mode setting)
- **UFOs on Mars**
- **Rave Aztec Monkey**
- **Closet Madotsuki**
- **Ghost Madotsuki** (More on this in the Fun Effects Mode setting)
- **Severed Heads in the Sky**
- **Thing with the Quivering Jaw**
- **FC Goblins**


## Shuffle RNG Events

This shuffles more events in the item pool which require luck or good RNG, listed below.

Activate at your own risk.

- **Uboa**
- **FACE**
- **Takofuusen**
- **Falling Man**
- **Famicom Glitch**
- **Melting Madotsuki** (This is considered a RNG event because interacting with all five beds in the same dream while in Snowman form is unreasonable, so you always end up hoping for good RNG that the bed in Snow World warps you to Stairway of Hands)


## Shuffle Vending Machines

You get an item for making a purchase at the three Vending Machines.

Knife is expected in logic in order to obtain money.


## Shuffle Restrooms

You get an item for entering each of the two Restrooms in Graffiti World and Block World.

More on this in the Fun Effects Mode setting.


## Separate Frogs

There are two locations where you can obtain the Frog effect: Forest World and Dense Woods.

If off you get only one item from the first frog you interact with.

If on you will get one item from each of the two frogs, effectively adding a location.


## Fun Effects Mode

A completely custom setting that gives utility to certain effects that otherwise don't have any:

- **Frog** is required to access Pink Sea (Based on the Frog's property of giving 2x speed in water)
- **Towel** is required to access the Stairway of Hands by interacting with the beds in the dream world (Based on Towel's resemblance to a bed sheet)
- **Demon** is required to use the shortcut from FC World to FC House by talking to RNG Demon (Based on Demon's property of making RNG Demon spawn with 100% chance)
- **Flute** is required to get the check Play with Masada
- **Nopperabou** is required to interact with the Pirori to get from Docks to Wilderness and from Barracks Settlement to FC World (Pirori have no face like Nopperabou)
- **Triangle Kerchief** is required to get the check Ghost Madotsuki
- **Poop Hair** is required to access Restrooms"""


## Logic Difficulty

Yume Nikki has a huge map and some entrances which, by a gameplay standpoint, are questionable at best. The logic selection is here to grant players a choice to prevent some unfun map traversal which otherwise would be in logic in almost every seed.

- **Easy logic**:
	- You are only expected to reach Stairway of Hands after having access to all five beds in the dream world (Madotsuki Room, Snow World, Block World, Candle World and Number World)
	- You are not expected to traverse Hell/Red Maze to reach Forest, Eyeball, Neon and Candle World. You are still expected to reach Docks and Witch Island through Hell though since it's the only way
	- Lamp effect is required in all the dark rooms
- **Mean logic**: all the above preventions are ignored;
- **No Logic**: ignores all logic and seeds could easily be unbeatable. Don't know why you would play this in Archipelago but it's available


## Choose Effects Translation

- Unofficial translations from UboaChan (Medamaude, Yuki Onna, Buyo Buyo, Knife, Fat, Nopperabou, Triangle Kerchief, Demon, Stoplight)

- Official translations from the Steam release (Eye Palm, Snow Woman, Squish-Squish, Kitchen Knife, Fatten, Faceless Ghost, Spirit Headband, Oni, Traffic Light)"""


# Miscellaneous Info

The canonical Yume Nikki Ending can be viewed as this game's Triforce Hunt since the requirement to reach it is having an X amount of Effects. I am working on an alternate arbitrary goal inspired by vgperson's Essences which can be viewed as a more local/objective-based gameplay.

Instructions is considered a useful "Effect" item but it's not counted in the total amount of effects you need to reach the Ending.

Instructions is an item you start with in the original game. This is replaced by the starting Nexus Key if Lock Nexus Doors is on and with a random item otherwise.

Filler locations are 100 Yen. They are currently not considered in the Vending Machines' logic. I will rethink about this when implementing Knifesanity.

Knifesanity/Killsanity is yaml setting not yet implemented which adds a location for every NPC you can kill in the game. This is a meme idea and I don't spur anyone with a sane mind to play it due to the big amount of locations and filler items it adds.


# Thanks to

- vgperson for creating a working standalone Yume Nikki randomizer from which I took some clever ideas
- SpearOfLies for helping with logic and testing
- Fajacopo for some ideas for Fun Effects Mode
- Kikiyama for making Yume Nikki
- and you :)