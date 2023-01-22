define pc = Character("Lois Knightingale", image="")

# layeredimage Knightingale:
#     group expressions:
#         attribute neutral default:
#             "images/ xxx.png"
#     group outfit:
#         attribute Adventurer default:
#             "images/ xxx.png"

init python:

    class char:
        def __init__(self, names, birthday, sign):
            self.names = names
            self.birthday = birthday
            self.sign = sign
            self.likes = likes
            self.dislikes = dislikes


    class adventurer(char):
        def __init__(self, level=1, township=0, monarchy=0, merchants=0, guild=0, *args, **kwargs):
            char.__init__(self, **kwargs)
            self.level = level
            self.township = township
            self.monarchy = monarchy
            self.merchants = merchants
            self.guild = guild

init:
    $ Knightingale = adventurer(
        names="Lois Knightingale",
        birthday="January 21st",
        sign ="Aquarius",
        likes="",
        dislikes="",
        level="1",
        township="1",
        monarchy="0",
        merchants="0",
        guild="0"
    )