# game/script.rpy:38
translate test start_bc1dddea:

    # p "Hello! This is Pronoun Tool, a simple tool for adding pronouns and displaying them in your Ren'Py game, made by npckc."
    p "The TEST language is being displayed! All text will be shown in English except for the pronouns. This is just to show that the pronouns are being translated properly."
    p "Hello! This is Pronoun Tool, a simple tool for adding pronouns and displaying them in your Ren'Py game, made by npckc."

# game/script.rpy:40
translate test start_4826879f:

    # p "I am Pronoun Parrot, your guide to Pronoun Tool! Once you have it set up, it's very easy to use."
    p "I am Pronoun Parrot, your guide to Pronoun Tool! Once you have it set up, it's very easy to use."

# game/script.rpy:42
translate test start_7a8680ca:

    # p "First, copy the file named pronountool.rpy from this game to the game folder of your own game."
    p "First, copy the file named pronountool.rpy from this game to the game folder of your own game."

# game/script.rpy:44
translate test start_77b26b71:

    # p "Once you've done that, all you have to do is follow the instructions in pronountool.rpy to make it work with your game!"
    p "Once you've done that, all you have to do is follow the instructions in pronountool.rpy to make it work with your game!"

# game/script.rpy:46
translate test start_fc85c65d:

    # p "You can change the default pronouns and add more if necessary."
    p "You can change the default pronouns and add more if necessary."

# game/script.rpy:48
translate test start_b0b63ec7:

    # p "It also lets you show the pronouns of the character currently speaking right on the dialogue screen!"
    p "It also lets you show the pronouns of the character currently speaking right on the dialogue screen!"

# game/script.rpy:50
translate test start_08a6f1a1:

    # p "Look at the pronountool.rpy file for more detailed instructions."
    p "Look at the pronountool.rpy file for more detailed instructions."

# game/script.rpy:54
translate test pronoun_5874b6b6:

    # p "Now, let's see an example of how this works. I'm going to call up the pronoun menu."
    p "Now, let's see an example of how this works. I'm going to call up the pronoun menu."

# game/script.rpy:58
translate test pronoun_f4b6a63a:

    # p "Good, you selected pronouns! You chose [selectedpronouns!t], right? I displayed the pronouns you selected using the following code:\n\n{color=#7f7fff}[[selectedpronouns!t]{/color}"
    p "Good, you selected pronouns! You chose [selectedpronouns!t], right? I displayed the pronouns you selected using the following code:\n\n{color=#7f7fff}[[selectedpronouns!t]{/color}"

# game/script.rpy:57
translate test pronoun_42026a45:

    # p "(You can change pronouns if you want by selecting Prefs > Pronouns > Select Pronouns.)"
    p "(You can change pronouns if you want by selecting Prefs > Pronouns > Select Pronouns.)"

# game/script.rpy:59
translate test pronoun_0d5ce8c4:

    # p "To show a set of specific pronouns, you can use the following code after replacing the # with the correct number:\n\n{color=#7f7fff}[[pronounlist[[#]!t]{/color}"
    p "To show a set of specific pronouns, you can use the following code after replacing the # with the correct number:\n\n{color=#7f7fff}[[pronounlist[[#]!t]{/color}"

# game/script.rpy:64
translate test pronoun_ae50946d:

    # p "For example, if you wanted to display [pronounlist[0]!t], since that is #0 in the list in pronountool.rpy, you would use the following code:\n\n{color=#7f7fff}[[pronounlist[[0]!t]{/color}"
    p "For example, if you wanted to display [pronounlist[0]!t], since that is #0 in the list in pronountool.rpy, you would use the following code:\n\n{color=#7f7fff}[[pronounlist[[0]!t]{/color}"

# game/script.rpy:65
translate test texttag_f1552a43:

    # p "Next, let's talk about pronoun text tags!"
    p "Next, let's talk about pronoun text tags!"

# game/script.rpy:70
translate test texttag_d4e2d585:

    # p "In our example, the pronouns used are [pronounlist[0]!t], [pronounlist[1]!t], and [pronounlist[2]!t], corresponding to the following text tags:\n\n{color=#7f7fff}{{_0}[pronounlist[0]!t]{{/_0} {{_1}[pronounlist[1]!t]{{/_1} {{_2}[pronounlist[2]!t]{{/_2}{/color}"
    p "In our example, the pronouns used are [pronounlist[0]!t], [pronounlist[1]!t], and [pronounlist[2]!t], corresponding to the following text tags:\n\n{color=#7f7fff}{{_0}[pronounlist[0]!t]{{/_0} {{_1}[pronounlist[1]!t]{{/_1} {{_2}[pronounlist[2]!t]{{/_2}{/color}"

# game/script.rpy:69
translate test texttag_826ecbbd:

    # p "Text within each tag will only show up when its pronouns are the ones selected. For example, text within {color=#7f7fff}{{_0}{{/_0}{/color} tags would only show up when {color=#7f7fff}[pronounlist[0]!t]{/color} is selected."
    p "Text within each tag will only show up when its pronouns are the ones selected. For example, text within {color=#7f7fff}{{_0}{{/_0}{/color} tags would only show up when {color=#7f7fff}[pronounlist[0]!t]{/color} is selected."

# game/script.rpy:71
translate test texttag_0e437479:

    # p "You can use it to show different text when different pronouns are selected. For example:\n\n{color=#7f7fff}This is {{_0}Mr{{/_0}{{_1}Ms{{/_1}{{_2}Mx{{/_2} Parrot.{/color}"
    p "You can use it to show different text when different pronouns are selected. For example:\n\n{color=#7f7fff}This is {{_0}Mr{{/_0}{{_1}Ms{{/_1}{{_2}Mx{{/_2} Parrot.{/color}"

# game/script.rpy:73
translate test texttag_7ae1159c:

    # p "This is how the code would actually look in-game:\n\n{color=#7f7fff}This is {_0}Mr{/_0}{_1}Ms{/_1}{_2}Mx{/_2} Parrot.{/color}"
    p "This is how the code would actually look in-game:\n\n{color=#7f7fff}This is {_0}Mr{/_0}{_1}Ms{/_1}{_2}Mx{/_2} Parrot.{/color}"

# game/script.rpy:78
translate test texttag_1c370b7b:

    # p "Did you notice how not all the text in the text tags was displayed? The displayed text should match with the pronouns you selected."
    p "Did you notice how not all the text in the text tags was displayed? The displayed text should match with the pronouns you selected."

# game/script.rpy:77
translate test texttag_63e98cf1:

    # p "You can use the tags however you like to work with your game. For example, if you are writing in a language like French with gender-specific adjectives, you can use the tags for that too."
    p "You can use the tags however you like to work with your game. For example, if you are writing in a language like French with gender-specific adjectives, you can use the tags for that too."


# game/script.rpy:74
translate test texttag_87cb533c:

    # p "For the French version of \"I am nervous\", you could use the following code to display different text for different pronouns:\n\n{color=#7f7fff}Je suis {{_0}nerveux{{/_0}{{_1}nerveuse{{/_1}{{_2}nerveuxe{{/_2}.{/color}"
    p "For the French version of \"I am nervous\", you could use the following code to display different text for different pronouns:\n\n{color=#7f7fff}Je suis {{_0}nerveux{{/_0}{{_1}nerveuse{{/_1}{{_2}nerveuxe{{/_2}.{/color}"

# game/script.rpy:76
translate test texttag_add4b89f:

    # p "This is how the code would actually look in-game:\n\n{color=#7f7fff}Je suis {_0}nerveux{/_0}{_1}nerveuse{/_1}{_2}nerveuxe{/_2}.{/color}"
    p "This is how the code would actually look in-game:\n\n{color=#7f7fff}Je suis {_0}nerveux{/_0}{_1}nerveuse{/_1}{_2}nerveuxe{/_2}.{/color}"

# game/script.rpy:86
translate test texttag_4ad33430:

    # p "For the provided sentence, \"nerveux\" would show up for [pronounlist[0]!t], \"nerveuse\" would show up for [pronounlist[1]!t], and \"nerveuxe\" would show up for [pronounlist[2]!t]."
    p "For the provided sentence, \"nerveux\" would show up for [pronounlist[0]!t], \"nerveuse\" would show up for [pronounlist[1]!t], and \"nerveuxe\" would show up for [pronounlist[2]!t]."

# game/script.rpy:84
translate test texttag_e0158f3a:

    # p "There is also another option of using variables to show pronouns to make things simpler."
    p "There is also another option of using variables to show pronouns to make things simpler."

# game/script.rpy:82
translate test texttag_721a98dc:

    # p "In the Pronouns as Variables section of pronountool.rpy, English pronouns are defined in lists of variables. That makes it possible to use code like this:\n\n{color=#7f7fff}[[they!t!c] went to the supermarket with [[their!t] friend.{/color}"
    p "In the Pronouns as Variables section of pronountool.rpy, English pronouns are defined in lists of variables. That makes it possible to use code like this:\n\n{color=#7f7fff}[[they!t!c] went to the supermarket with [[their!t] friend.{/color}"

# game/script.rpy:93
translate test texttag_5336cd5f:

    # p "It should be much easier to type (and easier to proofread the script). In-game, it would display like so:\n\n{color=#7f7fff}[they!t!c] went to the supermarket with [their!t] friend.{/color}"
    p "It should be much easier to type (and easier to proofread the script). In-game, it would display like so:\n\n{color=#7f7fff}[they!t!c] va au supermarché.{/color}"

# game/script.rpy:95
translate test texttag_64c4cf40:

    # p "However, this method might make it harder to do translations, as pronouns are not used the same way in every language, and different languages require different text changes depending on gender."
    p "However, this method might make it harder to do translations, as pronouns are not used the same way in every language, and different languages require different text changes depending on gender."

# game/script.rpy:93
translate test texttag_a35fd5ca:

    # p "If you decide to use variables, it would be best to also have the text tags as an option."
    p "If you decide to use variables, it would be best to also have the text tags as an option."

# game/script.rpy:91
translate test pronoundisplay_dd4e0698:

    # p "I think that should explain text tags well enough, so let's move on! Have you noticed how it says [pronounlist[2]!t] next to my name?"
    p "I think that should explain text tags well enough, so let's move on! Have you noticed how it says [pronounlist[2]!t] next to my name?"

# game/script.rpy:93
translate test pronoundisplay_e8cd0333:

    # p "That's because this tool also allows you to show pronouns when characters are speaking!"
    p "That's because this tool also allows you to show pronouns when characters are speaking!"

# game/script.rpy:105
translate test pronoundisplay_d2660917:

    # mc "Here's an example using the Main Character showing the pronouns you selected earlier. (If you change the selected pronouns, the displayed pronouns will change too!)"
    mc "Here's an example using the Main Character showing the pronouns you selected earlier. (If you change the selected pronouns, the displayed pronouns will change too!)"

# game/script.rpy:107
translate test pronoundisplay_16651fa9:

    # gfc "Here's an example with a genderflux character. Currently, the pronouns displayed should be [gfpronouns!t]. However, you can change that in-game with this (replace # with the pronouns you want):\n\n{color=#7f7fff}$ gfpronouns = pronounlist[[#]{/color}"
    gfc "Here's an example with a genderflux character. Currently, the pronouns displayed should be [gfpronouns!t]. However, you can change that in-game with this (replace # with the pronouns you want):\n\n{color=#7f7fff}$ gfpronouns = pronounlist[[#]{/color}"

# game/script.rpy:110
translate test pronoundisplay_bdc9ceef:

    # gfc "Here, I just changed the pronouns to [gfpronouns!t] with this code - the pronouns displayed should have changed too: \n\n{color=#7f7fff}$ gfpronouns = pronounlist[[2]{/color}"
    gfc "Here, I just changed the pronouns to [gfpronouns!t] with this code - the pronouns displayed should have changed too: \n\n{color=#7f7fff}$ gfpronouns = pronounlist[[2]{/color}"

# game/script.rpy:105
translate test pronoundisplay_167afaf4:

    # p "To make this work, you have to add pronouns for each character you use. For example, I, Pronoun Parrot, am defined like this:\n\n{color=#7f7fff}define p = Character(\"Pronoun Parrot\", image=\"pronounparrot\", show_pronouns=\"[[pronounlist[[2]!t]\"){/color}"
    p "To make this work, you have to add pronouns for each character you use. For example, I, Pronoun Parrot, am defined like this:\n\n{color=#7f7fff}define p = Character(\"Pronoun Parrot\", image=\"pronounparrot\", show_pronouns=\"[[pronounlist[[2]!t]\"){/color}"

# game/script.rpy:107
translate test pronoundisplay_b9c6db41:

    # p "You put the pronouns for each character in show_pronouns! Simple, right? After that, all you have to do is tweak the say screen a little. Look in pronountool.rpy for the specific instructions."
    p "You put the pronouns for each character in show_pronouns! Simple, right? After that, all you have to do is tweak the say screen a little. Look in pronountool.rpy for the specific instructions."

# game/script.rpy:95
translate test pronoundisplay_deeef1be:

    # p "This option can be turned off if the player does not want to see pronouns. You can test this by selecting Prefs > Pronouns > Display Pronouns."
    p "This option can be turned off if the player does not want to see pronouns. You can test this by selecting Prefs > Pronouns > Display Pronouns."

# game/script.rpy:116
translate test end_71638308:

    # p relaxed "That's pretty much it! I hope that all made sense. Please feel free to play around with the code to make it fit with your game."
    p relaxed "That's pretty much it! I hope that all made sense. Please feel free to play around with the code to make it fit with your game."

# game/script.rpy:101
translate test end_6a3ae738:

    # p "If you use this tool in your game, I'd appreciate it if you credit Pronoun Tool or npckc in some way, but it isn't required."
    p "If you use this tool in your game, I'd appreciate it if you credit Pronoun Tool or npckc in some way, but it isn't required."

# game/script.rpy:102
translate test end_81385241:

    # p "Thank you for your time!"
    p "Thank you for your time!"




