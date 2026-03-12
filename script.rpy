# ok start

define c = Character("The Child")
define s = Character("The Student")
define p = Character("The Parent")
define e = Character("The Elder")

image child = "images/The Child.png"
image student = "images/The Student.png"
image parent = "images/The Parent.png"
image elder = "images/The Elder.png"
image background1 = "images/background1.jpg"

define config.layeredimage_offer_screen = True

transform background:
    zoom 0.5

transform child_right:
    zoom 0.8
    xalign 0.0
    yalign 0.2


define config.layers = ["master", "Foreground", "transient", "Headshot", "headshot", "screens", "overlay" ]



label start:

    "Here is The Child"
    show background1 onlayer master at background
    show child onlayer Foreground at child_right


    "Can you see it?"

    hide child onlayer Foreground

    show student onlayer Foreground
    "Now for The Student."
    hide student onlayer Foreground

    show parent onlayer Foreground
    "Now The Parent."

    hide parent onlayer Foreground

    show elder onlayer Foreground
    "And lastly, The Elder."
return