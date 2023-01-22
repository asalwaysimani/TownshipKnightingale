# Everything below is just a regular script. You can look through it to see how the pronouns and text tags are displayed.

# Example of a DynamicCharacter

define mc = DynamicCharacter("mcname", show_pronouns="[selectedpronouns!t]")
default mcname = _("Main Character") # Set the variable (mcname) used as default for the DynamicCharacter.

image bg green = "#adc199"

image bg black = "#000000"

init -2:
    style say_thought:
        line_spacing 10
    style say_dialogue:
        line_spacing 10
    style confirm_prompt_text:
        line_spacing 10
    style about_text:
        line_spacing 10

label pronouns:

    $ quick_menu = False
    scene bg black
    with fade
    scene bg green with fade
    show pronounparrot base at right with dissolve
    $ quick_menu = True

    p "Hello! This is Pronoun Tool, a simple tool for adding pronouns and displaying them in your Ren'Py game, made by npckc."

    p "I am Pronoun Parrot, your guide to Pronoun Tool! Once you have it set up, it's very easy to use."

    p "First, copy the file named pronountool.rpy from this game to the game folder of your own game."

    p "Once you've done that, all you have to do is follow the instructions in pronountool.rpy to make it work with your game!"

    p "You can change the default pronouns and add more if necessary."

    p "It also lets you show the pronouns of the character currently speaking right on the dialogue screen!"

    p "Look at the pronountool.rpy file for more detailed instructions."

label pronoun:

    p "Now, let's see an example of how this works. I'm going to call up the pronoun menu."

    call pronounselection # This calls a choice menu to select pronouns.

    p "Good, you selected pronouns! You chose [selectedpronouns!t], right? I displayed the pronouns you selected using the following code:\n\n{color=#7f7fff}[[selectedpronouns!t]{/color}"

    p "(You can change pronouns if you want by selecting Prefs > Pronouns > Select Pronouns.)"

    p "To show a set of specific pronouns, you can use the following code after replacing the # with the correct number:\n\n{color=#7f7fff}[[pronounlist[[#]!t]{/color}"

    p "For example, if you wanted to display [pronounlist[0]!t], since that is #0 in the list in pronountool.rpy, you would use the following code:\n\n{color=#7f7fff}[[pronounlist[[0]!t\]{/color}"

label texttag:

    p "Next, let's talk about pronoun text tags!"

    p "In our example, the pronouns used are [pronounlist[0]!t], [pronounlist[1]!t], and [pronounlist[2]!t], corresponding to the following text tags:\n\n{color=#7f7fff}{{0}[pronounlist[0]!t]{{/0} {{1}[pronounlist[1]!t]{{/1} {{2}[pronounlist[2]!t]{{/2}{/color}"

    p "Text within each tag will only show up when its pronouns are the ones selected. For example, text within {color=#7f7fff}{{0}{{/0}{/color} tags would only show up when {color=#7f7fff}[pronounlist[0]!t]{/color} is selected."

    p "You can use it to show different text when different pronouns are selected. For example:\n\n{color=#7f7fff}This is {{0}Mr{{/0}{{1}Ms{{/1}{{2}Mx{{/2} Parrot.{/color}"

    p "This is how the code would actually look in-game:\n\n{color=#7f7fff}This is {0}Mr{/0}{1}Ms{/1}{2}Mx{/2} Parrot.{/color}"

    p "Did you notice how not all the text in the text tags was displayed? The displayed text should match with the pronouns you selected."

    p "You can use the tags however you like to work with your game. For example, if you are writing in a language like French with gender-specific adjectives, you can use the tags for that too."

    p "For the French version of \"I am nervous\", you could use the following code to display different text for different pronouns:\n\n{color=#7f7fff}Je suis {{0}nerveux{{/0}{{1}nerveuse{{/1}{{2}nerveuxe{{/2}.{/color}"

    p "This is how the code would actually look in-game:\n\n{color=#7f7fff}Je suis {0}nerveux{/0}{1}nerveuse{/1}{2}nerveuxe{/2}.{/color}"

    p "For the provided sentence, \"nerveux\" would show up for [pronounlist[0]!t], \"nerveuse\" would show up for [pronounlist[1]!t], and \"nerveuxe\" would show up for [pronounlist[2]!t]."

    p "There is also another option of using variables to show pronouns to make things simpler."

    p "In the Pronouns as Variables section of pronountool.rpy, English pronouns are defined in lists of variables. That makes it possible to use code like this:\n\n{color=#7f7fff}[[they!t!c] went to the supermarket with [[their!t] friend.{/color}"

    p "It should be much easier to type (and easier to proofread the script). In-game, it would display like so:\n\n{color=#7f7fff}[they!t!c] went to the supermarket with [their!t] friend.{/color}"

    p "However, this method might make it harder to do translations, as pronouns are not used the same way in every language, and different languages require different text changes depending on gender."

    p "If you decide to use variables, it would be best to also have the text tags as an option."

label pronoundisplay:

    $ persistent.displaypronouns = True
    p "I think that should explain text tags well enough, so let's move on! Have you noticed how it says [pronounlist[2]!t] next to my name?"

    p "That's because this tool also allows you to show pronouns when characters are speaking!"

    mc "Here's an example using the Main Character showing the pronouns you selected earlier. (If you change the selected pronouns, the displayed pronouns will change too!)"

    gfc "Here's an example with a genderflux character. Currently, the pronouns displayed should be [gfpronouns!t]. However, you can change that in-game with this (replace # with the pronouns you want):\n\n{color=#7f7fff}$ gfpronouns = pronounlist[[#]{/color}"

    $ gfpronouns = pronounlist[2]

    gfc "Here, I just changed the pronouns to [gfpronouns!t] with this code - the pronouns displayed should have changed too: \n\n{color=#7f7fff}$ gfpronouns = pronounlist[[2]{/color}"

    p "To make this work, you have to add pronouns for each character you use. For example, I, Pronoun Parrot, am defined like this:\n\n{color=#7f7fff}define p = Character(\"Pronoun Parrot\", image=\"pronounparrot\", show_pronouns=\"[[pronounlist[[2]!t]\"){/color}"

    p "You put the pronouns for each character in show_pronouns! Simple, right? After that, all you have to do is tweak the say screen a little. Look in pronountool.rpy for the specific instructions."

    p "This option can be turned off if the player does not want to see pronouns. You can test this by selecting Prefs > Pronouns > Display Pronouns."

label end:

    p relaxed "That's pretty much it! I hope that all made sense. Please feel free to play around with the code to make it fit with your game."

    p "If you use this tool in your game, I'd appreciate it if you credit Pronoun Tool or npckc in some way, but it isn't required."
    p "Thank you for your time!"

    $ quick_menu = False
    scene black with fade
    return

    return

