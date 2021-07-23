Jurassic Park (Megadrive) Password Generator
============================================

The 1993 game Jurassic Park for the Megadrive had a
[Password Save](https://en.wikipedia.org/wiki/Password_save) system to allow
the player to continue a game later, in the days before save files were
common. The password is an eight-digit alphanumerical code, and contains all
the information required to reproduce the (almost) exact state of the game
without the need to save any data on the cartridge.

This is a Python 3 library containing a single class,
```JurassicParkPasswordGenerator```. Once created, it has a ```password```
function which returns a valid password for the game. You can use the
class's other functions to customise the state of the game, such as
which level you start on, or how much ammo you have.

    >>> from JurassicParkMegadrive.JurassicParkPasswordGenerator import JurassicParkPasswordGenerator
    >>> p = JurassicParkPasswordGenerator()
    >>> p.password()
    '0VVVVVUP'

If we wanted to play as the velociraptor, we can do so like this...

    >>> p.player('raptor')
    'raptor'
    >>> p.password()
    'G3KS6L20'

For more advanced use, we can play in the Volcano stage, with no weapons other
than a full supply of rockets...

    >>> p.player('grant')
    'grant'
    >>> p.weapon(1, 0)
    0
    >>> p.weapon(2, 0)
    0
    >>> p.weapon(3, 0)
    0
    >>> p.weapon(4, 0)
    0
    >>> p.weapon(5, 0)
    0
    >>> p.weapon(6, 60)
    60
    >>> p.weapon(7, 0)
    0
    >>> g.level(6)
    6
    >>> g.password()
    'A0000U2A'

