###############################################################################################################
### SETUP #####################################################################################################
###############################################################################################################

## Step 1: Setting up Background Images ###########################################################
##
##  1. Go to where you've defined your background images. (The ones you use when you say "scene hallway", etc.)
##
##  2. Now, for every background image for which you want to define a location, change the image name to have "bg" in it, like so:
##
##          image bg storage = "images/backgrounds/storage.png"
##          image bg lounge = "images/backgrounds/books.png"
##          image bg tv = "images/backgrounds/tv.png"
##
##  3. Since your image names have changed, you will also have to adjust your script accordingly.
##     Using your text editor's find-and-replace tool (usually found under Edit), rename all instances of
##     "scene park" and "show park" to "scene bg park" and "show bg park", and so on.
##
##     (Note: Make sure to only change the scene and show statements for images you actually renamed!
##            Most likely, "scene black" should stay unchanged.)
##
##
## Step 2: Setting up Locations ###################################################################
##
##  1. Next, you should define all the locations in your game below.
##     (Don't worry, you only have to do this once, and it will be worth it!)
##
##     The format for location definitions is as follows:
##
##          "background_name" : {"name":_("Location Name"), "area":1, "pos":(400,500)},
##          "hidden" : {"name":_("???"), "area":None},
##
##  2. The first string should match the names of your background images - that's what will allow the locations to be automatically updated later!
##
##  3. The location name is optional, but can be useful in case you want to display it anywhere. Access it through:
##
##          locations[current_location]["name"]
##
##  4. The area variable allows you to group locations together depending on what general map layout they use.
##     This is intended for games that have different floors or regions (which use different background images).
##
##     If the area is None, this means that we're "off the grid", and the map will be hidden as long as we're there.
##
##     (Note: In case you have only one area in your game, setting all areas to 1 will be enough.)
##
##  5. Finally, "pos" is for the position of the location marker.
##     It should consist of a tuple (x,y) determining the xoffset and yoffset from the upper left corner of the map background image.
##
##     (Note: You don't have to supply "pos" if the a location's area is None.)

define locations = {

    # Feel free to comment these out:
    "hidden" : {"name":_("???"), "area":None},

    "room" : {"name":_("Eileen's Room"), "area":1, "pos":(350,420)},

    }

## Done! ##########################################################################################
##
##  You did it! All that's left is to finetune everything to your liking!
##
##  To display the map screen in your game, add ShowMenu("status") to your navigation or quick menu!
##  For example:
##
##          textbutton _("Map") action ShowMenu("status")

## Important Variables ##############################################################################
##
## You can adjust these as you wish. A few notes:
##
##          [minimap] is used for you as the developer to decide when the minimap should be hidden or shown.
##          Use [$ minimap = False] in your script if you want to (temporarily) disable the minimap, and [$ minimap = True] to enable it again.
##
##          [map_image_path] specifies where your map images are located. They should all be in the same folder and match the area names.
##          In case you do not use PNG images, change [map_image_type] as needed.
##
##          The default [current_area] is the "starting area" of the game.
##          The default [current_location] is the "starting location" of the game.
##
##          [minimap_position] specifies the alignment of the minimap. The default (1.0, 0.0) is the upper right corner of the screen.
##          [minimap_offset] specifies how far away the minimap should be from the border of the screen.
##
##          If not None, [location_indicator_image] should specify a file name, such as "images/map_indicator.png" - otherwise an "x" is displayed instead.
##
##          [area_limit] is used to determine which areas are accessible to view from the menu.
##          If all of them should be accessible from the start, replace "1" with the number of areas in the game.
##
##          The preference variables should be self-explanatory. You can also add them to the preferences screen for player customization.
##
##          [preferences.minimap_zoom] is a bit special. It makes the minimap show a partial, zoomed in view of the map.
##          A value of 2 shrinks the map by half, a value of 3 is only a third of the full map, and so on.
##          If you want to disable this feature, set the value to 0.

default minimap = True

define map_image_path = "map/"
define map_image_type = ".png"

default current_area = None
default current_location = "hidden"

default area_limit = 1

define minimap_position = (1.0, 0.0)
define minimap_offset = 10

define location_indicator_image = None

default preferences.show_minimap = True
default preferences.minimap_opacity = 0.5
default preferences.minimap_size = 0.3

default preferences.minimap_zoom = 2

## Character Callback ######################################################
##
##  This is where the magic happens.
##  Whenever a character speaks, the location will be updated to match the current background image.

init python:

    def location(name=None):
        global current_location
        global current_area
        global area_limit
        loc = None
        if 'bg' in renpy.get_showing_tags():
            loc = renpy.get_attributes('bg')[0]
        if name in locations:
            current_location = name
        elif loc in locations:
            current_location = loc
        if locations[current_location]["area"]:
            current_area = locations[current_location]["area"]
            if locations[current_location]["area"] > area_limit:
                area_limit = locations[current_location]["area"]

    def update_location(event, **kwargs):
        location()

define config.all_character_callbacks = [ update_location ]


## Screens ##########################################################################################
##
##  This is the screen that is accessible through the game menu.
##  It contains the map screen, but you can also add other things to make it even more useful!

screen status():
    tag menu
    on "show" action SetVariable("current_area", locations[current_location]["area"])
    use game_menu(_("Status")):
        text _("Current Location: ") + locations[current_location]["name"]
        use map

## Minimap ##########################################################################################
##
##  The minimap is a tiny map in the corner of the screen.
##  Feel free to comment out this section if you don't need it.

init python:
    config.overlay_screens.append("minimap")

transform minimap_opacity(opac):
    on hover:
        ease 0.3 alpha 1.0 mesh True
    on idle:
        ease 0.3 alpha opac mesh True

screen minimap():

    $ area = locations[current_location]["area"]

    if minimap and preferences.show_minimap and area != None:

        fixed pos minimap_offset,minimap_offset xysize config.screen_width-2*minimap_offset, config.screen_height-2*minimap_offset-gui.textbox_height:

            fixed fit_first True xalign minimap_position[0] yalign minimap_position[1]:
                button:
                    frame:
                        use map(scale=preferences.minimap_size, minimap=True)
                        at minimap_opacity(preferences.minimap_opacity)
                    action ShowMenu('status')
                    keyboard_focus False

## Map Screen ##########################################################################################
##
##  This is where you can edit the map screen itself.
##  Note that any changes here will be reflected both in the minimap and in the game menu.

screen map(scale=1.0, minimap=False):

    if minimap:
        $ area = locations[current_location]["area"]
    else:
        $ area = current_area

    if minimap and preferences.minimap_zoom:
        $ scale = scale * preferences.minimap_zoom

    if area != None:
        fixed fit_first True:
            if not minimap:
                yalign 0.5

            # The map background image. You can change the file path as needed, but all background images should match your use of the area variable.
            add map_image_path + str(area) + map_image_type zoom scale:
                if minimap and preferences.minimap_zoom:
                    crop (int(locations[current_location]["pos"][0]-renpy.image_size(map_image_path + str(area) + map_image_type)[0]/(preferences.minimap_zoom*2)), int(locations[current_location]["pos"][1]-renpy.image_size(map_image_path + str(area) + map_image_type)[1]/(preferences.minimap_zoom*2)), int(renpy.image_size(map_image_path + str(area) + map_image_type)[0]/preferences.minimap_zoom), int(renpy.image_size(map_image_path + str(area) + map_image_type)[1]/preferences.minimap_zoom))

            # The location indicator
            if area == locations[current_location]["area"]:
                fixed:
                    if minimap and preferences.minimap_zoom:
                        xpos 0.5 ypos 0.5
                    else:
                        xpos int(locations[current_location]["pos"][0]*scale) ypos int(locations[current_location]["pos"][1]*scale)

                    if location_indicator_image:
                        add location_indicator_image zoom scale
                    else:
                        text "x" size int(gui.interface_text_size*scale)

            # Area view buttons
            if not minimap and area_limit > 1:
                hbox xalign 0.5:
                    textbutton "<" action SetVariable("current_area", If(current_area > 1, current_area-1, 1))
                    text _("AREA")
                    textbutton ">" action SetVariable("current_area", If(current_area < area_limit, current_area+1, area_limit))
