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

define who = True
define dreams = True

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

    hide elder onlayer Foreground
    show child onlayer Foreground at child_right

    "The Child laughs."

    hide child onlayer Foreground
    show parent onlayer Foreground at parent_right

    p "Now, is that any way to greet this new face?"

    hide parent onlayer Foreground
    show elder onlayer Foreground at elder_right

    "The Elder sighs."

    e "I wish for you to find your place, both here and in your own space."

    hide elder onlayer Foreground
    show student onlayer Foreground at student_right

    s "Which also brings us to a very interesting point. You're not from here. From the looks of it, you're of the world from our dreams."

    hide student onlayer Foreground
    menu confusion:
        "Who are you?" if who:
            jump ss_who
        "What is this place":
            jump ss_what
        "Your dreams?" if dreams:
            jump ss_dreams
            label ss_who:

                show child onlayer Foreground at child_right

                c "We are The Four!"

                hide child onlayer Foreground
                show student onlayer Foreground at student_right

                s "The Four Directions, to be precise. Living entities, both simple and complex."

                hide student onlayer Foreground
                show parent onlayer Foreground at parent_right

                p "We are some of the only things to exist in this space."

                hide parent onlayer Foreground
                show child onlayer Foreground at child_right

                c "At least for now."
                $ who = False
                hide child onlayer Foreground
                jump confusion

            label ss_what:

                show student onlayer Foreground at student_right

                s "It is a void of sorts. There is light, darkness, and space."

                hide student onlayer Foreground
                show child onlayer Foreground at child_right

                c "There are stars!"

                "The Child gestures to the specks of light that dot the darkness."

                hide child onlayer Foreground
                show student onlayer Foreground at student_right

                s "Those are actually specks of Knowledge. They group together and form bright clumps and clusters. Very helpful to have lying around." 
            
                s "And besides them, there is us. That is all that resides in this space. But that is what we're all trying to change."

                hide student onlayer Foreground

            label ss_dreams:

                show parent onlayer Foreground at parent_right
                p "Yes, we dreamt of a far away world. A world of many things, of people and voices and buildings."

                hide parent onlayer Foreground
                show child onlayer Foreground at child_right

                c "That's where you come from! I just know it! We're always thinking about that world!"

                hide child onlayer Foreground
                show student onlayer Foreground at student_right

                s "And we know about it. We like the things from it."

                hide student onlayer Foreground
                show elder onlayer Foreground at elder_right

                e "Some of the things."

                hide elder onlayer Foreground
                show student onlayer Foreground at student_right

                s "The dreams gave us the ideas to work on something of our own."
                $ dreams = False
                hide student onlayer Foreground
                jump confusion

    menu:
        "What are you working on?":

            show child onlayer Foreground at child_right

            c "We liked your world so much, we want to make one too!"

            hide child onlayer Foreground
            show student onlayer Foreground at student_right

            s "Yes, that's the idea. This void…it would just be a waste if we were the only objects that ever populated it. And a world seems like a pretty good choice."

            hide student onlayer Foreground
            show parent onlayer Foreground at parent_right

            p "We're just doing a bit of brainstorming right now. It's important to think about the way our world could be."
            p "Say, you seem like someone who would be interested in that. Care to join?"

            hide parent onlayer Foreground
            show child onlayer Foreground at child_right

            c "Ooh, yes yes, pleeeeasee. You can make your very own list!"

            "The Child looks at The Parent."

            c "Tell them that they should join. It would be so fun!"

            hide child onlayer Foreground
            show parent onlayer Foreground at parent_right

            p "Well dear, we want everyone to be able to-"

            hide parent onlayer Foreground
            show elder onlayer Foreground at elder_right

            e "Then it's settled. You wouldn't want to say no to The Child, right new face? Time for you to pitch in."

            hide elder onlayer Foreground
            show student onlayer Foreground at student_right

            s "Splendid. Then let's continue."
            s "We've been working in our minds, but you should probably get a paper and pencil, or something else to write with."

            hide student onlayer Foreground
            show child onlayer Foreground at child_right

            c "Yes! Then you have to make a list. Write down as many things as you can."

            hide child onlayer Foreground
            show student onlayer Foreground at student_right

            s "No no, the goal isn't quantity, it's quality. You should think and write down only your best ideas."

            hide student onlayer Foreground
            show child onlayer Foreground at child_right

            c "Well that's stupid. You're gonna end up with nothing written down, and then-"

            p "Why don't we let them decide if an idea is worth writing down or not."
            p "Listen dear, just make a list of things that you think would be a good foundation for a world. Things like tone, genre, time period, and level of technology, science, and magic. I know the people of your world like magic."
            p "Then, once you've got some ideas down on your list, come and talk to us again."

            hide parent onlayer Foreground
            show child onlayer Foreground at child_right

            c "This is going to be great!"

            hide child onlayer Foreground

            "The Elder rolls their eyes, and the group disperses to the four directions."

            centered "..."

            menu ss:
                "Talk to The Child." if child:
                    jump ss_child
                "Talk to The Student" if student:
                    jump ss_student
                "Talk to The Parent and The Elder" if parent:
                    jump ss_pe

                    label ss_child:

                        "The Child stands amidst bright clumps of Knowledge, floating around. They grab two twinkling specks and mash them together. They turn from the bright colors to look at you."

                        show child onlayer Foreground at child_right
                    

                        c "Hi again! Did you make your list?"

                        menu:
                            "Yes, I've worked on it.":
                                jump ss_yes
                            "What are you doing?":
                                jump ss_what

                                label ss_yes:

                                    c "Great! How many things did you come up with?"
                                    number = renpy.input("How many?", length=32)

                                    c "What? That's not enough."
                                label ss_what:


                                    c "I'm coming up with new ideas!"

                                    "They grab one dull speck and shake it, causing it to glow brighter."

                        c "We're going to need a lot more ideas if we're going to make something interesting."




return