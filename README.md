# Archipelago Manual for Yume Nikki

This is an Archipelago implementation for the freeware game Yume Nikki using the manual Archipelago Client.

You can download the game [here](https://store.steampowered.com/app/650700/Yume_Nikki/) for free on Steam.

It is highly advised to use a save file with all the 24 effects already obtained. If you want to go even further you can use a save file with all the effects dropped on the ground in the Nexus as eggs, and picking them up as you receive them from Archipelago.


# How this works

With the most basic yaml configuration: the 24 effects are shuffled in the item pool.

Your goal is to reach the ending after having obtained all the 24 effects from Archipelago.


# Yaml Options

## Lock Nexus Doors

This setting locks the 12 doors in the Nexus.

Find the respective Keys to access the worlds.

If this option is on you will always start with a random Nexus Key.


## Eventsanity

Since the Lock Nexus Doors setting only adds items to Archipelago but no locations, this complementary optional setting shuffles various Yume Nikki events in the item pool, listed below.

You can even play with Nexus doors unlocked and eventsanity on, but you will get more filler items.

- **Melting Madotsuki**
- **Toriningen Party**
- **Witch's Flight**
- **Rave Aztec Monkey**
- **Monoe**
- **Monoko**
- **Play with Masada** (More on this in the Custom Effects Requirements setting)
- **UFO**
- **Mars-san**
- **Closet Madotsuki**
- **Severed Heads in the Sky**


## Event RNGchance Sanity

This shuffles more events in the item pool which require luck or good RNG, listed below.

Activate this at your own risk.

- **Uboa**
- **FACE**
- **Takofuusen**
- **Falling Man**


## Vending Machines Sanity

You get an item for making a purchase at the three Vending Machines.

Knife is expected in logic in order to obtain money.


## Separate Frogs

There are two locations where you can obtain the Frog effect: Forest World and Dense Woods.

You can choose if you will obtain a single item from any of the two locations or two items in total: one from each of the two locations.


## Custom Effects Requirements

A completely custom setting that increases fun and gives utility to certain effects that otherwise don't have any:

- Frog is required to access Pink Sea (Based on the Frog's property of giving 2x speed in water)
- Towel is required to access the Stairway of Hands by interacting with the beds in the dream world (Based on Towel's resemblance to a bed sheet)
- Demon is required to use the shortcut from FC World to FC House by talking to RNG Demon (Based on Demon's property of making RNG Demon spawn with 100% chance)
- Flute is required to get the item from **Play with Masada**


## Logic Difficulty

Yume Nikki has a huge map and some entrances which, by a gameplay standpoint, are questionable at best. The logic selection is here to grant players a choice to prevent some unfun map traversal which otherwise would be in logic in almost every seed.

- **Easy logic**: you are only expected to reach Stairway of Hands after having access to all five beds in the dream world (Madotsuki Room, Snow World, Block World, Candle World and Number World), granting you a 100% access by interacting with all of them in the same dream;
you are not expected to traverse Hell/Red Maze to reach Forest, Eyeball, Neon and Candle World, even if you could, you are still expected to reach Docks and Witch Island through Hell though since it's the only route;
Lamp effect is required in all the dark rooms;
- **Mean logic**: all the above preventions are ignored;
- **No Logic**: ignores all logic and seeds could easily be unbeatable. Don't know why you would play this in Archipelago but it's available
