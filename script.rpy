# ok start

define c = Character("The Child")
define s = Character("The Student")
define p = Character("The Parent")
define e = Character("The Elder")

image child = "images/The Child.png"
image student = "images/The Student.png"
image parent = "images/The Parent.png"
image elder = "images/The Elder.png"
image background1 = "image/background1.jpg"

define config.layeredimage_offer_screen = True




define config.layers = ["master", "Foreground", "transient", "Headshot", "headshot", "screens", "overlay" ]



label start:

    "Here is The Child"
    show child onlayer Foreground

    "Can you see it?"

return