# ok start

define c = Character("The Child")
define s = Character("The Student")
define p = Character("The Parent")
define e = Character("The Elder")
define q = Character("???")

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

    centered "Chapter 1: Swirl & Snarl"
    centered "In which introductions are made"

    show background1 onlayer master at background

    "You find yourself in motion, spinning around over and over in a strange space."
    "It is neither cool nor hot. It is both light and dark. There is a thin layer between you and the space around you." 
    "As you spin, you are spoken to."

    q "Something new? Something new! Something new with a new face!"

    q "Stand back. Let us give this new face a proper welcome."

    q "A new face means new thoughts. Perhaps this is what we need."

    q "Seems doubtful. Although this one has a familiar twinkle in their eye."

    "Four presences wait eagerly and expectantly around you. They come into focus as the spinning starts to slow."

    q "Everyone, let us meet this new face with our best. Let us introduce ourselves, and each express a wish for this individual."

    "The presences approach you, one at a time."

    show child onlayer Foreground at child_right

    "A small energetic figure beams at you."

    c "Hello! I wish for you to have fun making with us! Oh, also I am The Child."

    hide child onlayer Foreground
    show student onlayer Foreground at student_right

    "The Child is replaced by a figure who tips its head to you."

    s "I am The Student. My wish is for you to be open to us, so that we can be open to you. May we learn from each other."

    hide student onlayer Foreground
    show parent onlayer Foreground at parent_right

    "A third figure radiates warmth and words."

    p "I am The Parent, dear. It is lovely to meet you. I wish for you to stay with us as long as you find meaningful."

    hide parent onlayer Foreground
    show elder onlayer Foreground at elder_right

    "The last figure seems content to remain where it is."

    e "The Elder. I wish you'd have gotten here sooner."

    "The Child laughs."

    p "Now, is that any way to greet this new face?"

    "The Elder sighs."

    e "I wish for you to find your place, both here and in your own space."

    s "Which also brings us to a very interesting point. You're not from here. From the looks of it, you're of the world from our dreams."

    menu confusion:
        "Who are you?":
            jump ss_who
        "What is this place":
            jump ss_what
        "Your dreams?":
            jump ss_dreams
        label ss_who:

            c "We are The Four!"

            s "The Four Directions, to be precise. Living entities, both simple and complex."

            p "We are some of the only things to exist in this space."

            c "At least for now."
            jump confusion


return