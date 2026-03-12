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
    xalign -0.7
    yalign 1.0
transform student_right:
    zoom 0.7
    xalign -0.35
    yalign 1.0
transform parent_right:
    zoom 0.9
    xalign -0.9
    yalign 2.0
transform elder_right:
    zoom 0.9
    xalign -2.5
    yalign 1.5

define config.layers = ["master", "Foreground", "transient", "Headshot", "headshot", "screens", "overlay" ]



label start:
    "At first, there was nothing but swirling Darkness and Light and Clear."
    "Then there was a spark, and there were The Four Directions, stretching out away from each other." 
    "All around them were specks of Knowledge. These specks collected on The Four Directions, and fed them."
    "As The Four Directions grew, they started to take shape. Four sleeping entities."
    "As they slept, they started to dream. They dreamt of a space beyond their own, each one seeing unique glimpses of all other things."
    "The Four awoke from their dreams, in the Darkness above the Light. Each one wandered the Darkness, and found another. The two pairs learned to speak, and so they shared what they had seen in their dreams."
    "When the pairs came together, they finally learned their names. They were The Four, together, yet alone within the Darkness." 
    "They had dreamt of something called a world, and wished for a world of their own. So The Four set to work creating their world."

return