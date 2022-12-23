
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 33

style choice_button is default:
    xysize (1185, None)
    idle_background Frame("gui/button/choice_[prefix_]background.png",
        150, 8, 150, 8, tile=False)

style choice_button_text is default:
    xalign 0.5
    idle_color "#ccc"
    hover_color "#fff"
    insensitive_color "#444"
