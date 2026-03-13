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
define Child = True
define Student = True
define Parent = True
define Elder = True
define fixer = Character("[number]")

default tracker = 0

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

    "Attention! Any time you see the three dots in the center of the screen, that means you've been prompted to do a real-life activity. Here is an example:"

    centered "..."

    "All right, enjoy..."

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
                jump ss_next

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

                label ss_next:
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
                        label ss:
                            menu:
                                "Talk to The Child." if Child:
                                    jump ss_child
                                "Talk to The Student" if Student:
                                    jump ss_student
                                "Talk to The Parent and The Elder" if Parent:
                                    jump ss_pe

                                    label ss_child:

                                        "The Child stands amidst bright clumps of Knowledge, floating around. They grab two twinkling specks and mash them together. They turn from the bright colors to look at you."

                                        show child onlayer Foreground at child_right
                                    

                                        c "Hi again! Did you make your list?"

                                        menu:
                                            "Yes, I've worked on it.":
                                                jump ss_yes
                                            "What are you doing?":
                                                jump ss_enough

                                                label ss_yes:

                                                    c "Great! Let me see how many you came up with."

                                                    $ number = renpy.input("How many?", length=32)

                                                    c "What? That's not enough."
                                                label ss_enough:


                                                    c "I'm coming up with new ideas!"

                                                    "They grab one dull speck and shake it, causing it to glow brighter."

                                        c "We're going to need a lot more ideas if we're going to make something interesting."


                                        c "I've already figured out a couple different kinds of animals that would be cool."
                                        c "We could have animals with 5 legs, and animals with big horns on their noses, and, and…have you ever heard of a Hyrax?"

                                        menu:
                                            "Maybe you should slow down.":
                                                jump ss_slow
                                            "...":
                                                jump ss_place1

                                    label ss_place1:

                                        c "And there can be a bunch of different trees! Strong trees, twisty trees, hollow trees. And people will make bread and candy and cookies!"
                                        c "There would need to be a lot of people making cookies for it to be a proper world, obviously."

                                        menu:
                                            "I thought you were supposed to be brainstorming more general details?":
                                                jump ss_slow
                                            "...":
                                                jump ss_place2
                                    label ss_place2:
                                        c "Oh there's so much to do! I don't know what to work on first! Maybe we should figure out which beings will fly and which will swim. Or maybe we can start naming all the cities that we're going to make. Actually, we should probably create some liquids to dunk the cookies in…"

                                        menu:
                                            "This seems like a lot of ideas":
                                                jump ss_slow

                                                label ss_slow:

                                                    c "Well…I guess so."
                                                    c "The rest of The Four said we were supposed to be figuring out the big stuff before the small stuff. I trust them…so I guess I'll do that too." 
                                                    c "But you should write some more stuff down on that list of yours! You can never have too many ideas…I think."
                                                    

                                                    "The Child turns away and goes back to fiddling with the motes of Knowledge."
                                                    $ Child = False
                                                    $ tracker += 1
                                                    hide child onlayer Foreground
                                                    centered "..."

                                                    if tracker >= 3:
                                                        jump ss_ending 
                                                    else:
                                                        jump ss
                                                

                                    label ss_student:
                                        show student onlayer Foreground at student_right
                                        "The Student sits in an especially dark space in the void. They seem focused on something inward."

                                        menu:
                                            "...":
                                                jump ss_wait
                                            "How's it going?":
                                                jump ss_hows

                                                label ss_wait:
                                                    s "Well, don't be shy. Come join me."

                                                    "You sit beside the entity."
                                                    jump ss_hows
                                                

                                                label ss_hows:
                                                    s "I am meditating. I hear that it is good for trying to be one's best self, despite what The Elder may say."
                                        menu:
                                            "What does The Elder have against meditation?":
                                                jump ss_against
                                            "What are you meditating on?":
                                                jump ss_on

                                                label ss_against:
                                                    s "If I am not mistaken, The Elder believes that everyone should strive to be their best self, but is rather particular about how they do it."
                                                    s "They find things that seem to progress slowly to be a waste of time. Rather impatient if you ask me."

                                                    "The Student smiles."

                                                    s "But then again, you must remember that we are all relatively young."

                                                label ss_on:
                                                    s "I am trying to sort through my ideas."

                                        s "I wish to select the best possible idea to move forward with, but that requires an analysis of how things might go later."
                                        menu:
                                            "What do you have so far?":
                                                jump ss_place3
                                    label ss_place3:            

                                        s "Well…nothing yet. But I've been thinking about it! If I pick a bad idea to start with, then this whole project will be a failure. Don't you agree?"
                                        menu:
                                            "Not really...":
                                                jump ss_place4
                                            "I suppose.":
                                                jump ss_place4

                                        label ss_place4:
                                            "The Student scoffs."

                                            "Really? What would you do then? Would you just pluck every idea out of the air as it drifts by you, like The Child?"
                                            menu:
                                                "I would go with the first idea I had":
                                                    jump ss_first
                                                "I would test a few of my ideas.":
                                                    jump ss_ideas
                                                "I would talk to someone else about my ideas.":
                                                    jump ss_ideas

                                                    label ss_first:
                                                        s "Well, you're obviously no academic."

                                                    label ss_ideas:

                                                        s "...I suppose that is definitely an option. I hadn't really considered that."

                                            s "Look, I still believe we can learn something from each other."
                                            s "If you're willing to give my method a try…then perhaps I will try yours as well."
                                            menu:
                                                "Deal.":
                                                    jump ss_place6
                                        label ss_place6:        
                                            s "Thank you. In that case, pick one of your ideas to expand upon. Then we can compare our ideas later."
                                            s "Until then, good luck."

                                            centered "..."

                                            $ Student = False
                                            $ tracker += 1
                                            hide student onlayer Foreground

                                            if tracker >= 3:
                                                jump ss_ending
                                            else:
                                                jump ss
                                        

                                    label ss_pe:

                                        show elder onlayer Foreground

                                        "The Elder stands in the darkness, swaying gently side to side."

                                        e "..."

                                        "After some silence, The Parent rushes over."

                                        hide elder onlayer Foreground
                                        show parent onlayer Foreground at parent_right

                                        p "Ah, hello dear. Apologies if I kept you from finding me. The other two were having a bit of an argument, but that's all cleared up now."

                                        hide parent onlayer Foreground
                                        show elder onlayer Foreground at elder_right

                                        e "Until it starts up again. We're always arguing about something."

                                        hide elder onlayer Foreground
                                        show parent onlayer Foreground at parent_right

                                        p "Not always! I mean, well, I suppose it's true that we've been having our…creative disputes."
                                        p "But now you're here, new face, and we have come up with an idea."
                                        p "What if you were to build your own world alongside us? We've only ever dreamt of one world, one way to be. But if you made a world of your own, we'd have two worlds, two datapoints to base our progress on."
                                        p "You could make it however you wished, with magic or mad science or anything. And it would be such a help to us."

                                        hide parent onlayer Foreground
                                        show elder onlayer Foreground at elder_right

                                        e "Now wait just a minute. We all agreed that we would create a world based off of the one we dreamt about. None of this science fiction or fantasy mumbo jumbo. Why do we need another world to do that?"

                                        hide elder onlayer Foreground
                                        show parent onlayer Foreground at parent_right

                                        p "Well…um…"

                                        "The Parent takes The Elder's hands in theirs."

                                        p "The others have been talking, and they have a desire to make beyond just what we know from the other world. They want to create things that are new and exciting."

                                        "The Elder shakes off The Parent."

                                        hide parent onlayer Foreground
                                        show elder onlayer Foreground at elder_right

                                        e "But that's not what we agreed upon! You can't just go changing things up like that. It has to be the way we said it would be!"

                                        hide elder onlayer Foreground
                                        show parent onlayer Foreground at parent_right

                                        p "I know what we originally had planned, but the others think-"

                                        hide parent onlayer Foreground
                                        show elder onlayer Foreground at elder_right

                                        e "And what do you think? What do you want?"

                                        hide elder onlayer Foreground
                                        show parent onlayer Foreground at parent_right

                                        p "I simply want everyone to be fulfilled."

                                        hide parent onlayer Foreground
                                        show elder onlayer Foreground at elder_right

                                        e "No, you don't. Because if you did, you wouldn't have brought this to me."

                                        hide elder onlayer Foreground
                                        show parent onlayer Foreground at parent_right

                                        p "Dear, can't we make just one change?"

                                        hide parent onlayer Foreground
                                        show elder onlayer Foreground at elder_right

                                        e "No! No, no, no!"

                                        "The Elder starts storming off."

                                        e "Do what you want! It obviously doesn't involve me!"

                                        hide elder onlayer Foreground

                                        "The Elder vanishes from sight."

                                        show parent onlayer Foreground at parent_right

                                        p "Oh dear…"

                                        menu:
                                            "Are they going to be alright?":
                                                jump ss_alright
                                            "Are you alright?":
                                                jump ss_you

                                                label ss_alright:

                                                    "The Parent gives a gentle nod and a weak smile."

                                                    p "Yes. We will speak with them. They can find obstructions…incredibly bothersome."
                                                    p "They see the endpoint better than any of us, but become annoyed when we do not take the most direct path to that endpoint. I will assure them that we will listen to their voice. That should help calm them."


                                                label ss_you:

                                                    "The Parent sighs."

                                                    p "Yes, I am fine. I believe The Elder does not consider our points of view. We will need to speak with them some more, so that all may be known to one another."

                                                    "The Parent smiles."

                                                    p "But I do not mind. Conflict is a small price to pay for the love we share. I hope that this is something you know as well."

                                        "The Parent stares into your mind, their gaze indicating a request."

                                        p "Despite what transpired, I still believe that you would do us good by building alongside us. A world of your own is a treasure and a gift. It may be a frightening task, but we will support one another."
                                        p "Besides, you already have the ideas you've taken down there. Perhaps several of those would lay the foundation for your world. You should have at minimum a few central ideas of what your world will be like, as we will also have to do."
                                        menu:
                                            "I will do what I must to continue.":
                                                jump ss_place5
                                    label ss_place5:
                                        p "That's the spirit! Now, let us both move on to our tasks. I wish you the best of luck, and may we speak again."

                                        hide parent onlayer Foreground

                                        centered "..."

                                        $ Parent = False
                                        $ tracker += 1
                                        if tracker >= 3:
                                            jump ss_ending
                                        else:
                                            jump ss

                label ss_ending:

                        "You stand on your own, and think."

                        "…"

                        "The Four approach you once more, a buzz of excitement surrounding them."

                        show student onlayer Foreground at student_right

                        s "We have concluded with our brainstorming sessions."

                        hide student onlayer Foreground
                        show child onlayer Foreground at child_right

                        c "It took foreeeeever."

                        hide child onlayer Foreground
                        show parent onlayer Foreground at parent_right

                        p "But we've had a chance to speak amongst ourselves, and we've come to a unanimous decision."

                        hide parent onlayer Foreground
                        show elder onlayer Foreground at elder_right

                        e "If you ignore the separation between indifference and enthusiasm."

                        hide elder onlayer Foreground
                        show child onlayer Foreground at child_right

                        c "Our world will be a world of Fantasy and Adventure!!"

                        hide child onlayer Foreground
                        show student onlayer Foreground at student_right

                        s "There will be plenty of new concepts to explore."

                        hide student onlayer Foreground
                        show child onlayer Foreground at child_right

                        c "And new things to play with!"

                        hide child onlayer Foreground
                        show parent onlayer Foreground at parent_right

                        p "And new hearts to know."

                        hide parent onlayer Foreground
                        show elder onlayer Foreground at elder_right

                        e "..."

                        hide elder onlayer Foreground
                        show parent onlayer Foreground at parent_right

                        p "Well, that is what we have come up with. Did you come to terms with some of the elements of your own world?"
                        menu:
                            "Yes.":
                                jump ss_more_yes
                            "No.":
                                jump ss_more_no
                            
                                label ss_more_yes:

                                    p "Splendid!"

                                    hide parent onlayer Foreground
                                    show student onlayer Foreground at student_right

                                    s "Interesting…"

                                    hide student onlayer Foreground
                                    show parent onlayer Foreground at parent_right

                                    p "Well regardless, it sounds like it will be a wonderful piece of work to draw to and from. Well done."
                                        
                                    label ss_more_no:

                                        "The Parent furrows their expression."

                                        hide parent onlayer Foreground
                                        show student onlayer Foreground at student_right

                                        s "If you are having trouble, something I believe to be helpful is discussing your work with others."
                                        s "If you can find someone in the space where you are to bounce ideas off of, they can often provide a unique insight that unlocks doors that you could not open otherwise. Try finding someone to talk to right now!"
                                        hide student onlayer Foreground
                                        centered "..."

                                show parent onlayer Foreground at parent_right

                                p "Now, what shall we do next?"

                                hide parent onlayer Foreground
                                show student onlayer Foreground at student_right

                                s "I think we should pause and let things settle before moving on. Make sure we're all really happy with our idea."

                                hide student onlayer Foreground
                                show elder onlayer Foreground at elder_right

                                e "Well, don't take too long. We don't even have anything physically there yet."

                                hide elder onlayer Foreground
                                show child onlayer Foreground at child_right

                                c "But that's next, right?! That's next!"

                                hide child onlayer Foreground 
                                show parent onlayer Foreground at parent_right

                                p "Yes. Let us embark on the next step of this journey then."

                                "The Parent gestures to you."

                                p "After you, worldbuilder."
                                hide parent onlayer Foreground
                                hide background1 onlayer master
                                $ Child = True
                                $ Student = True
                                $ Parent = True
                                $ Elder = True
                                $ Tracker = 0

label gf:

    centered "Chapter 2: Gifts of The Four"
    centered "In which Wonder finds its gift"
    show background1 onlayer master at background
    "In the Darkness, in the Light, the motes of Knowledge have come together. They are large and ripe with potential, like the first of the stars."
    "You sit and admire them for all they offer. The space feels different. As though it has been primed to hold something."
    "The Four seem eager to find what that something will be. They speak to you and among themselves, until The Student speaks up."

    show student onlayer Foreground at student_right
    s "All right everyone, I know we're all excited to have reached this moment. We've done much talking, much brainstorming, and now we are to start filling the space around us."
    hide student onlayer Foreground

    "The Parent and The Child give applause."

    show elder onlayer Foreground at elder_right

    e "Finally."

    hide elder onlayer Foreground
    show student onlayer Foreground

    s "Now, in order to give us some direction in this endeavor, I have come up with a plan of action." 
    s "I believe that we should all focus on just one thing to give this world, at least at first."
    s "There is so much we can do, but if we each start from this one thing and work our way out from it, we can better determine how each part will affect each other part of our world. Does that make sense?"

    hide student onlayer Foreground
    show child onlayer Foreground at child_right

    c "Umm…"

    hide child onlayer Foreground
    show parent onlayer Foreground at parent_right

    p "I believe so. We are each to develop our own gift for this world?"

    hide parent onlayer Foreground
    show student onlayer Foreground at student_right

    s "Yes exactly! A gift from each of us."

    hide student onlayer Foreground
    show parent onlayer Foreground at parent_right    

    p "That sounds lovely."

    hide parent onlayer Foreground
    show child onlayer Foreground at child_right    

    c "So, what can we do? For the gift? What are we allowed to make?"

    hide child onlayer Foreground
    show student onlayer Foreground at student_right

    s "You can make your gift anything at all. It could be specific, but I feel that something a bit more general would be a better idea."

    hide student onlayer Foreground
    show child onlayer Foreground at child_right

    "The Child lights up, then suddenly frowns."

    c "Ok…so it can be anything, but it needs to be just one thing?"

    hide child onlayer Foreground
    show student onlayer Foreground at student_right

    s "Yes. I already have an idea for my gift."

    hide student onlayer Foreground

    "The Elder shuffles off, leaving the rest of you to talk amongst yourselves."

    show parent onlayer Foreground at parent_right

    p "Ah. I should also move on. But I trust that you will think of a gift of your own, worldbuilder?"
    hide parent onlayer Foreground
    menu:
        "I suppose":
            jump gf_either
        "I'm good":
            jump gf_either

            label gf_either:

                show student onlayer Foreground at student_right

                s "At any rate, I need a bit more time to develop my gift. Feel free to pop by, worldbuilder."
                hide student onlayer Foreground
                "The Student and The Parent disperse."

                centered "…"
label gf_talk:

    menu:
        "Talk to The Student" if Student:
            jump gf_student

        "Talk to The Parent" if Parent:
            jump gf_parent

        "Talk to The Elder" if Elder:
            jump gf_elder

            label gf_student:
                $ Student = False
                if Child == True:
                        "Before you reach your destination, you feel a presence at your side. You look down and see The Child, uncharacteristically dimmed."

                        show child onlayer Foreground at child_right

                        c "...what if I can't do it?"

                        menu:
                            "Can't do what?":
                                jump gf_cant1

                                label gf_cant1:

                                    c "What if I can't find my gift?"
                                    menu:
                                        "Why would you say that?":
                                            jump gf_why1

                                            label gf_why1:

                                                "The Child looks down."

                                                c "Well, The Student said this was my one gift. They already know what their gift is. But I don't know…"
                                                c "What if I just can't figure it out?"
                                                menu:
                                                    "Have you thought about it?":
                                                        jump gf_thought1

                                                        label gf_thought1:


                                                            c "Yeah…I thought about it a bit. I know I have ideas. But I'm not sure if they'll be as good as everyone else's."
                                                            c "I just don't know if I can do this right."
                                                            menu:
                                                                "You don't need to compare your ideas to others.":
                                                                    jump gf_compare1
                                                                "The first step to making something good is getting started.":
                                                                    jump gf_first1

                                                                    label gf_compare1:

                                                                        c "Ok…Ok. Maybe you could still ask the others about their gifts? Just so we know what they are. Just so I don't do the same one…"
                                                                        jump gf_figure1

                                                                    label gf_first1:

                                                                        "The Child takes a breath."

                                                                        c "Ok…Ok. If you say I can do it, then I can do it. I'll get started. I can work on my ideas some more."
                                                                        jump gf_figure1

                                                                        label gf_figure1:
                                                                            menu:
                                                                                "You can do this!":
                                                                                    jump gf_cando1

                                                                                    label gf_cando1:

                                                                                        c "All right. Yeah! You're right! I can do this! I'm gonna go and figure out all the stuff about my gift!"
                                                                                        c "Thanks worldbuilder!"
                                                                                        hide child onlayer Foreground

                                                                                        "The Child runs off, shining brightly again."
                                                                                        $ Child = False                                                                             
                "You come upon The Student, who is running back and forth over and over again."
                menu:
                    "What are you doing?":
                        jump gf_doing

                        label gf_doing:

                            show student onlayer Foreground at student_right

                            "The Student stops for a second, out of breath."

                            s "I'm…testing…my theory…"

                            "The Student straightens up, taking a few deep breaths."

                            s "It's actually related to my gift, in case you were wondering."

                            menu:
                                "Go on.":
                                    jump gf_goon

                                    label gf_goon:

                                        "The Student grins proudly."

                                        s "Well, as I'm sure you noticed, I was over there."

                                        "The Student points to the spot where they were running back and forth."

                                        s "But now I'm here."

                                        menu:
                                            "Should I be surprised?":
                                                jump gf_time

                                            "So what does that mean?":
                                                jump gf_time

                                                label gf_time:

                                                    s "Well, for you of course, I'm sure that being there and then here seems normal. But do you know how long it took me to get from there to here? How long exactly?"

                                                    "The Student moves from one spot to another, and as you consider their question, you realize you don't know how long it took them."
                                                    "You try to count the seconds, but find yourself coming up with a different number each time. It could've taken five seconds, or months, or somewhere in between."

                                                    menu:
                                                        "I don't...":
                                                            jump gf_dont

                                                            label gf_dont:


                                                                s "Exactly! Things just happen here, and they either happen before or after each other, but that's as specific as you can get."
                                                                s "Your world, the dream world, has time. That's how we know about before, and after, and now, and later, ooh I'm a big fan of later. Time only sort of exists here, but what if we had proper time? A proper way to keep track of things?"
                                                                menu:
                                                                    "I think that would be pretty neat.":
                                                                        jump gf_neat

                                                                    "Time is overrated.":
                                                                        jump gf_overrated

                                                                        label gf_neat:

                                                                            s "Exactly! More than pretty neat! That would be revolutionary!"
                                                                            jump gf_s_gift

                                                                        label gf_overrated:

                                                                            s "Well then you take time for granted. Imagine how hard it would be to get anything done without time. The four of us have managed in this space without it, but it makes things so unpredictable."
                                                                            s "I don't want our world to be like that!"
                                                                            jump gf_s_gift

                                                                            label gf_s_gift:


                                                                                s "So that's why my gift to this world will be the gift of time!"

                                                                                "The Student shakes their hands back and forth with a jazzy motion."

                                                                                s "This will make everything easier for everyone! No more guesswork, no more frustrations! Denizens will be able to learn, grow, and change for the better! Pretty good, right?"
                                                                                menu:
                                                                                    "...":
                                                                                        jump gf_unsure
                                                                                    "Seems like a great idea.":
                                                                                        jump gf_great

                                                                                        label gf_unsure:


                                                                                            s "I can see you need a bit more time to fully understand my gift as it applies to this world."
                                                                                            jump gf_s_finish

                                                                                        label gf_great:

                                                                                            "The Student nods proudly."

                                                                                            s "I think everyone is going to like it."
                                                                                            jump gf_s_finish

                                                                                            label gf_s_finish:



                                                                                                s "Now, I'm sure you've got your own matters to attend to. You've got your own world to build, after all."
                                                                                                s "Maybe some others need help with their gifts, hmm? Until next time."

                                                                                                hide student onlayer Foreground

                                                                                                "Rather full of themselves, The Student walks off."
                                                                                                $ tracker += 1

                                                                                                if tracker >= 3:
                                                                                                    jump gf_next
                                                                                                else:
                                                                                                    jump gf_talk


            label gf_parent:
                $ Parent = False
                if Child == True:
                        "Before you reach your destination, you feel a presence at your side. You look down and see The Child, uncharacteristically dimmed."

                        show child onlayer Foreground at child_right

                        c "...what if I can't do it?"

                        menu:
                            "Can't do what?":
                                jump gf_cant2

                                label gf_cant2:

                                    c "What if I can't find my gift?"
                                    menu:
                                        "Why would you say that?":
                                            jump gf_why2

                                            label gf_why2:

                                                "The Child looks down."

                                                c "Well, The Student said this was my one gift. They already know what their gift is. But I don't know…"
                                                c "What if I just can't figure it out?"
                                                menu:
                                                    "Have you thought about it?":
                                                        jump gf_thought2

                                                        label gf_thought2:


                                                            c "Yeah…I thought about it a bit. I know I have ideas. But I'm not sure if they'll be as good as everyone else's."
                                                            c "I just don't know if I can do this right."
                                                            menu:
                                                                "You don't need to compare your ideas to others.":
                                                                    jump gf_compare2
                                                                "The first step to making something good is getting started.":
                                                                    jump gf_first2

                                                                    label gf_compare2:

                                                                        c "Ok…Ok. Maybe you could still ask the others about their gifts? Just so we know what they are. Just so I don't do the same one…"
                                                                        jump gf_figure2

                                                                    label gf_first2:

                                                                        "The Child takes a breath."

                                                                        c "Ok…Ok. If you say I can do it, then I can do it. I'll get started. I can work on my ideas some more."
                                                                        jump gf_figure2

                                                                        label gf_figure2:
                                                                            menu:
                                                                                "You can do this!":
                                                                                    jump gf_cando2

                                                                                    label gf_cando2:

                                                                                        c "All right. Yeah! You're right! I can do this! I'm gonna go and figure out all the stuff about my gift!"
                                                                                        c "Thanks worldbuilder!"
                                                                                        hide child onlayer Foreground

                                                                                        "The Child runs off, shining brightly again."
                                                                                        $ Child = False
                "The Parent is crouched down, talking to The Child."

                show parent onlayer Foreground at parent_right

                p "Well, here's the thing, little one. Whatever you decide to do, I will be there to support you. My gift will help sustain all of yours, if you'll let it. Understand?"

                hide parent onlayer Foreground
                show child onlayer Foreground at child_right

                c "I understand. I'm just thinking about it a bit."

                hide child onlayer Foreground

                "The Parent smiles sweetly."

                show parent onlayer Foreground at parent_right

                p "That's good, I'm glad to see you being a bit more reflective."
                p "Perhaps you will find your gift in the skies, or possibly the light and dark, or in pain and joy."

                hide parent onlayer Foreground
                show child onlayer Foreground at child_right

                c "Yeah! Those are all great ideas! Ok, I'll do those!"

                hide child onlayer Foreground
                show parent onlayer Foreground at parent_right

                p "But, do you mean-"

                hide parent onlayer Foreground

                "Before The Parent can finish, The Child has run off." 
                "The Parent chuckles to themselves and stands up. They turn to face you."

                show parent onlayer Foreground at parent_right

                p "Oh hello dear. I didn't see you there. Everything going well, I hope?"

                menu:
                    "Things are well.":
                        jump gf_well

                    "Things could be better.":
                        jump gf_better

                        label gf_well:


                            p "That's lovely to hear. It's so nice to see everyone working hard, and equally lovely to see you speaking with them all."
                            jump gf_p_gift

                        label gf_better:

                            p "Oh, I'm sorry to hear that dear. I appreciate you still deciding to talk to everyone. You've been a big help."
                            jump gf_p_gift
                            
                            label gf_p_gift:

                                p "Ah, yes. It took me a bit, but I figured it out. You see, everyone else seems interested in building up their complex systems or concepts. But everyone needs ground to stand on. So that will be my gift."
                                p "The ground, the water, the air. The materials that make up our world. This way, the others will have something to place their creations on."
                                menu:
                                    "How thoughtful of you.":
                                        jump gf_thoughtful

                                        label gf_thoughtful:


                                            "The Parent nods and smiles."

                                            p "Well, it is a necessity. And no one else was thinking about it. So I am happy to step in and put my effort towards this. I hope that my gift will go on to nourish the things of this world, as well as those who created it."
                                            p "And speaking of materials, perhaps you could use some of your own. I am not certain if you have located what you need yet, but when creating a world, one can use materials from all over."
                                            p "If you have access to some, paper, pencil, tools, craft supplies, colored implements, or just anything that would help you create your world, create a realized version of it, then I suggest you find those. You might even get some ideas along the way."

                                            "The Parent gives a knowing wink."

                                            p "Now then, I wish to speak with The Student. I hope to talk again."

                                            centered "…"
                                            $ tracker += 1
                                            if tracker >= 3:
                                                jump gf_next
                                            else:
                                                jump gf_talk

            label gf_elder:
                $ Elder = False
                if Child == True:
                        "Before you reach your destination, you feel a presence at your side. You look down and see The Child, uncharacteristically dimmed."

                        show child onlayer Foreground at child_right

                        c "...what if I can't do it?"

                        menu:
                            "Can't do what?":
                                jump gf_cant3

                                label gf_cant3:

                                    c "What if I can't find my gift?"
                                    menu:
                                        "Why would you say that?":
                                            jump gf_why3

                                            label gf_why3:

                                                "The Child looks down."

                                                c "Well, The Student said this was my one gift. They already know what their gift is. But I don't know…"
                                                c "What if I just can't figure it out?"
                                                menu:
                                                    "Have you thought about it?":
                                                        jump gf_thought3

                                                        label gf_thought3:


                                                            c "Yeah…I thought about it a bit. I know I have ideas. But I'm not sure if they'll be as good as everyone else's."
                                                            c "I just don't know if I can do this right."
                                                            menu:
                                                                "You don't need to compare your ideas to others.":
                                                                    jump gf_compare3
                                                                "The first step to making something good is getting started.":
                                                                    jump gf_first3

                                                                    label gf_compare3:

                                                                        c "Ok…Ok. Maybe you could still ask the others about their gifts? Just so we know what they are. Just so I don't do the same one…"
                                                                        jump gf_figure3

                                                                    label gf_first3:

                                                                        "The Child takes a breath."

                                                                        c "Ok…Ok. If you say I can do it, then I can do it. I'll get started. I can work on my ideas some more."
                                                                        jump gf_figure3

                                                                        label gf_figure3:
                                                                            menu:
                                                                                "You can do this!":
                                                                                    jump gf_cando3

                                                                                    label gf_cando3:

                                                                                        c "All right. Yeah! You're right! I can do this! I'm gonna go and figure out all the stuff about my gift!"
                                                                                        c "Thanks worldbuilder!"
                                                                                        hide child onlayer Foreground

                                                                                        "The Child runs off, shining brightly again."
                                                                                        $ Child = False
                "The Elder sits still, completely unmoving. Their face is unreadable."
                menu:
                    "...":
                        jump gf_e_1

                        label gf_e_1:
                            show elder onlayer Foreground at elder_right
                            e "..."
                            menu:  
                                "What are you doing?":
                                    jump gf_e_2

                                    label gf_e_2:

                                        e "Sitting here with myself. Alone."
                                        menu:
                                            "Do you have a gift?":
                                                jump gf_e_3

                                                label gf_e_3:

                                                    e "No."
                                                    menu:
                                                        "Are you going to create a gift?":
                                                            jump gf_e_4

                                                            label gf_e_4:

                                                                e "No."
                                                                menu:
                                                                    "Why not?":
                                                                        jump gf_e_5

                                                                        label gf_e_5:
                                                                            e "I don't have anything I want to add to this project."
                                                                            menu:
                                                                                "Do you want help?":
                                                                                    jump gf_e_6

                                                                                    label gf_e_6:

                                                                                        e "No."
                                                                                        menu:
                                                                                            "Goodbye.":
                                                                                                jump gf_e_goodbye

                                                                                                label gf_e_goodbye:
                                                                                                    e "Goodbye."
                                                                                                    hide elder onlayer Foreground

                                                                                                    $ tracker += 1
                                                                                                    if tracker >= 3:
                                                                                                        jump gf_next
                                                                                                    else:
                                                                                                        jump gf_talk
label gf_next:
    "As you look around the space, you suddenly see different colored streaks of light shooting off into the Darkness from a ways away."
    menu:
        "Investigate the light.":
            jump gf_investigate

            label gf_investigate:

                "As you get closer to the light, you see its origin point. The Child seems to be performing rather animated motions, shooting light from their body upwards, creating all kinds of twisting shapes and colors."
                "They look towards you with a fervor in their being."
                menu:
                    "Are you ok?!":
                        jump gf_ok

                        label gf_ok:
                            show child onlayer Foreground at child_right

                            c "I heard about everyone else's gifts! They were so cool, and I can't wait to do mine! And I talked to everyone too! They made lots of suggestions!"
                            c "The Parent said I could do some stuff with emotions, so I really want to do that."
                            c "The Student said I should focus on what I like, and I really want to do that too! I like candy. I could make my gift all about emotions and candy. Maybe it could be like, the emotions you feel when eating candy."
                            c "Although I've never eaten candy before. But I still know it's good!"
                            c "And The Elder isn't doing a gift, so I probably should do an extra one for them. I like shiny metal too! So my gift can be metal and candy and feelings. Like, I can make people feel good when they bake cookies on a shiny metal tray. That could be my gift!"

                            "The light starts streaking off of The Child faster and faster. Above them, the distinct shapes of hearts and tears, cookies and chocolate, and shiny coins and brass buttons form."
                            menu:
                                "Be careful!":
                                    jump gf_careful

                                    label gf_careful:
                                        "You call out, shouting above the roaring sound of the bolts of light."
                                        menu:
                                            "It seems like you're trying to do quite a lot of things with this gift!":
                                                jump gf_lots

                                                label gf_lots:

                                                    c "I was just trying to follow what everyone else was saying! Last time you all said I was doing too much, so this time I just did all of what they said! Was I not supposed to do all of it?"
                                                    menu:
                                                        "You were supposed to make your own decision!":
                                                            jump gf_decision
                                                        "You should both your friends, and yourself!":
                                                            jump gf_trust

                                                            label gf_decision:

                                                                c "But last time I got it wrong! That was what I was worried about this time!"
                                                                menu:
                                                                    "You didn't get it wrong.":
                                                                        jump gf_wrong

                                                                        label gf_wrong:

                                                                            "The Child pauses for a moment."

                                                                            c "I didn't?"
                                                                            menu:
                                                                                "You just tried to do it a different way. And sometimes that way works, and sometimes you listen to others when they tell you something needs to change.":
                                                                                    jump gf_different

                                                                                    label gf_different:
                                                                                        "The light surrounding The Child starts to come back down to its usual level."

                                                                                        c "I…I…"
                                                                                        jump gf_resolution

                                                            label gf_trust:

                                                                c "...both?"
                                                                menu:
                                                                    "Yes.":
                                                                        jump gf_mhm

                                                                        label gf_mhm:
                                                                            c "..."                                                                            
                                                                            menu:
                                                                                "Yes. Sometimes you do it your way even when others tell you not to, and sometimes you listen to them when they tell you to try something else.":
                                                                                    jump gf_yourway

                                                                                    label gf_yourway:

                                                                                        "The light surrounding The Child starts to come back down to its usual level."

                                                                                        c "I…I…"
                                                                                        jump gf_resolution

                                                                                        label gf_resolution:

                                                                                            c "I just have all of these things I want to do. And…something others say I'm being silly by trying to do so much. I think that people will say I'm not being r-re-realistic."
                                                                                            menu:
                                                                                                "The others said that?":
                                                                                                    jump gf_others

                                                                                                    label gf_others:
                                                                                                        "The Child sniffles a little and shrugs."

                                                                                                        c "Well…kind of…I know that they think it sometimes. Sometimes I ignore them. But then sometimes when I ignore them, everything blows up in my face."
                                                                                                        c "I figured this time around, if I just did what everyone else said I should do, it would work out ok."
                                                                                                        menu:
                                                                                                            "How do you feel now?":
                                                                                                                jump gf_feel

                                                                                                                label gf_feel:
                                                                                                                    c "I feel like maybe I shouldn't have said yes to everything. I think I get that now."

                                                                                                                    "The Child looks up at you hopefully."

                                                                                                                    c "But…it's not too late, is it? I can still figure out my gift. My own gift. Right?"
                                                                                                                    menu:
                                                                                                                        "Absolutely.":
                                                                                                                            jump gf_absolutely

                                                                                                                            label gf_absolutely:

                                                                                                                                "The Child gives a small grin."

                                                                                                                                c "Well…then I'm gonna do it. Figure out my gift. Just the one gift. I'll listen to myself, and I'll listen to what the others told me, and I'll make a decision from that. Does that sound good?"
                                                                                                                                menu:
                                                                                                                                    "Sounds great.":
                                                                                                                                        jump gf_sounds

                                                                                                                                        label gf_sounds:

                                                                                                                                            c "Ok. Then I need to go think. I'm sure I can figure it out."
                                                                                                                                            c "Thank you, worldbuilder. Thank you for helping me when I felt sad."

                                                                                                                                            hide child onlayer Foreground
                                                                                                                                            jump gf_finish
label gf_finish:

    "After everyone has gone off on their own for a while, the entities start coming together."
    "The Parent and The Student talk to each other, while The Elder maintains a distance. The Child is nowhere to be seen. After another wait, The Student speaks."

    show student onlayer Foreground at student_right

    s "All right, let's see what we've all come up with. What are everyone's gifts?"

    hide student onlayer Foreground
    show parent onlayer Foreground at parent_right

    p "I can speak first. I have decided to give the gift of materials."

    "The Student nods approvingly. The Parent addressed The Elder hopefully."

    p "Do you have anything to share?"

    hide parent onlayer Foreground
    show elder onlayer Foreground at elder_right

    e "I do not."

    hide elder onlayer Foreground

    "The Parent sighs."

    show student onlayer Foreground at student_right

    s "Well, I certainly found my gift. My gift shall be the gift of time!"

    hide student onlayer Foreground
    show parent onlayer Foreground at parent_right

    "The Parent nods slowly."

    p "I believe I understand…and I am excited to see what comes of your gift dear."

    "The Student smiles proudly."

    p "Now, where is The Child?"

    hide parent onlayer Foreground
    show child onlayer Foreground at child_right

    c "BOO!"

    "The Child is suddenly standing among you. You are unsure of when they got there, as you did not see them prior to this point."

    hide child onlayer Foreground
    show parent onlayer Foreground at parent_right

    p "Oh! You seem to have snuck up on us, dear."

    hide parent onlayer Foreground
    show student onlayer Foreground at student_right

    s "How did you manage that?"

    hide student onlayer Foreground
    show child onlayer Foreground at child_right

    c "I have picked my gift. I thought about everything I liked, and I know what I wanna do."
    c "My gift is…magic!"

    hide child onlayer Foreground
    show student onlayer Foreground at student_right

    s "The gift of magic?"

    hide student onlayer Foreground
    show child onlayer Foreground at child_right

    c "The whole world will be magical. Magic will be here and there, and all kinds of crazy stuff will happen! Just you wait!"

    hide child onlayer Foreground

    "The Elder grumbles to themself, which The Parent attempts to cover up."

    show parent onlayer Foreground at parent_right

    p "That is just wonderful. I am so glad you found your gift."
    p "And I'm so proud of all of you for what you have offered. May the world we create be better off with all of these gifts."

    hide parent onlayer Foreground

    "The Student and The Child nod."

    show student onlayer Foreground at student_right

    s "Indeed!"

    p "Then I suppose it is time to start marking the world. We need to create something physical now. Some land, some waves, some magical energies. And whatever else that will be a part of the world's form."
    p "And that means you too, worldbuilder. It's high time you made physical marks of your world, if you haven't already. A map, a drawing, a sculpture. We need to see what your world looks like. Are you all ready?"
    hide parent onlayer Foreground
    menu:
        "As ready as I'll ever be.":
            jump gf_ever

            label gf_ever:
                show student onlayer Foreground at student_right
                s "Then it's time! Let's finally go and put something in the world!"
                hide student onlayer Foreground

                "The Four all soar off in different directions, leaving you alone with the world of your own."
                hide background1 onlayer master

                centered "…"
                $ Child = True
                $ Student = True
                $ Parent = True
                $ Elder = True
                $ Tracker = 0

label cm:
    centered "Chapter 3: Concious Movement"
    centered "In which Craft releases its grasp"

    show background1 onlayer master

    "The Four have been hard at work. The space below is now populated with what resembles a map, sprawling away in all directions."
    "Four distinct land masses are arranged on the map, their landscapes of mountains, forests, and rivers having just been sculpted and shaped. Having rested, The Student stands to face the rest of the group."

    show student onlayer Foreground at student_right

    s "All right everyone! We've done excellent work thus far. We have the physical world all in place."

    hide student onlayer Foreground
    show parent onlayer Foreground at parent_right

    p "I particularly like what everyone has done with their continent. The Elder's looks especially lovely."

    hide parent onlayer Foreground
    show student onlayer Foreground at student_right

    s "But now we must press forward. The next subject to tackle is…"

    hide student onlayer Foreground
    show chil onlayer Foreground at child_right

    "The Child jumps up and down with their hand raised."

    c "Ooh, I know! I know what's next!"

    hide child onlayer Foreground
    show student onlayer Foreground at student_right

    s "...Yes?"

    hide student onlayer Foreground
    show chil onlayer Foreground at child_right

    c "We need people! The world is lonely, so we need to put people there!"
    hide child onlayer Foreground
    show student onlayer Foreground at student_right

    s "Well, I suppose, but I think that creating denizens will be a rather complicated process of collaboration and-"

    hide student onlayer Foreground
    show chil onlayer Foreground at child_right

    c "Nah, it'll be easy! I've got a bunch of ideas right here."

    "The Child reaches into their pocket and pulls out a handful of bright motes, then throws them up into the air, where they float around gently."

    hide child onlayer Foreground
    show elder onlayer Foreground at elder_right

    e "Tch. So messy."

    hide elder onlayer Foreground
    show child onlayer Foreground at child_right

    c "Look at all these animals and people! And they can all be totally magical!"

    hide child onlayer Foreground
    show student onlayer Foreground at student_right

    s "Don't be ridiculous. Any magical capabilities of these denizens must be considered in context with each other." 
    s "We'll have to make a table to compare each single creature with its ecosystem cohabitants. The larger the creature the larger the ecosystem range, of course."
    s "Any changes made to them should be passed through each of us, and the table. We wouldn't want any-"

    hide student onlayer Foreground
    show elder onlayer Foreground at elder_right

    e "If we do all of that, we'll never actually create any creatures."

    hide elder onlayer Foreground
    show child onlayer Foreground at child_right

    c "Yeah! Look, we can think about all that…context stuff while we're creating them."

    hide child onlayer Foreground

    "The Child runs off giggling towards the map. The Parent starts after them, but turns back to look at The Student."

    show parent onlayer Foreground at parent_right

    p "Those were some lovely points you made, dear. Why don't you work on figuring that out, and then come tell us about it. Ok?"

    hide parent onlayer Foreground
    show student onlayer Foreground at student_right

    s "But-"

    hide student onlayer Foreground

    "The Parent goes running after The Child, calling out."

    p "Wait dear! You don't want to trample those freshly laid mountains!"

    show student onlayer Foreground at student_right

    "The Student stands in place, stammering slightly."

    s "Wha…but…but…"

    "The Elder watches The Student for a moment, then plucks a mote of Knowledge out of the air and walks off as well."

    "The Student watches them go. They start to speak out, but then retract and sigh."
    hide student onlayer Foreground
    menu:
        "...":
            jump cm_wow
        "Wow.":
            jump cm_wow

            label cm_wow:
                show student onlayer Foreground at student_right
                s "...You know, I'm starting to regret this whole gift of time thing."
                menu:
                    "Why?":
                        jump cm_why

                        label cm_why:

                            s "It's tough, being stuck on a set timeline now. Now that we're measuring time, there always seems to be less of it than there was before. It's stressful."

                            s "And if we get this wrong, there's no going back. Once we put creatures with independent thoughts in the world, we don't get to make decisions for them anymore."
                            s "That's why it's so important to give them the best start that we can. Set them up to make the right decisions, to live lives full of purpose and fulfillment. The others seemed to pay no mind to that conundrum."
                            menu:
                                "Don't you think you're being a bit controlling?":
                                    jump cm_control

                                "If it's important to you, then you should ask them about it again.":
                                    jump cm_important

                                    label cm_control:

                                        "The Student shakes their head."

                                        s "No, no. You don't understand! I've gifted time to this world. The creatures we create will grow and change."
                                        s "If we don't think this through, think ahead to account for what could happen, it could very well ruin this world forever!"
                                        menu:
                                            "...":
                                                jump cm_fix

                                                label cm_fix:

                                                    "The Student stands straight."

                                                    s "I am going to speak to the others. I wish to hear their individual thoughts on the matter."
                                                    jump cm_off

                                    label cm_important:

                                        s "You think so?"
                                        menu:
                                            "Maybe they've already come up with some ideas to make this process easier.":
                                                jump cm_easier

                                                label cm_easier:

                                                    s "All right! I will go speak to them on the matter once more, individually this time. I hope that you're right."
                                                    jump cm_off

                                                    label cm_off:
                                                        hide student onlayer Foreground
                                                        "The Student walks off." 
label cm_talk:
    menu:
        "Talk to The Child" if Child:
            jump cm_child
        "Talk to The Student and The Parent" if Student:
            jump cm_sp
        "Talk to The Elder" if Elder:
            jump cm_elder

            label cm_child:

                "The Child runs up to you, beaming bright as always."

                show child onlayer Foreground at child_right

                c "Hey! Hey, hey hey! I wanna show you something!"

                menu:
                    "Ok, lead the way.":
                        jump cm_lead

                        label cm_lead:

                            "The Child leads you over to a section of the map. They point to the top left continent."

                            c "That's my part. It's got tons of trees and lakes, and lotsa great places for animals to live. So you know what I'm going to put there?"

                            "The Child grins at you."
                            menu:
                                "What will you put there?":
                                    jump cm_what

                                    label cm_what:

                                        c "Dogs. So many dogs. And not just any dogs. Dogs with flowers growing on them! And trees too! All kinds of plants."
                                        c "And the dogs will be all different sizes! There will be little dogs, and reeeallly big dogs. It'll be great!"
                                        menu:
                                            "I'm not really a dog person...":
                                                jump cm_nodog
                                            "That sounds great. I love dogs.":
                                                jump cm_dog

                                                label cm_nodog:

                                                    "The Child frowns a bit."

                                                    c "Aww…well that's ok. There'll be stuff here that isn't dogs too!"
                                                    menu:
                                                        "Like what?":
                                                            jump cm_explain

                                                label cm_dog:

                                                    "The Child beams."

                                                    c "Right?! And the dogs and the people can be friends! It'll be the best thing ever!"
                                                    menu:
                                                        "What people?":
                                                            jump cm_explain

                                                            label cm_explain:

                                                                c "Right, the people. I made this one person, like, a big person. The Student said it was a god, so I guess I made the God of Light."
                                                                c "And then the God of Light made a bunch of other smaller people out of magic, so I guess those are the children of light?"
                                                                c "Anyways, they're really good at magic, and they'll be walking around the world soon. And in the meantime, I'll be working on a bunch of other guys!"
                                                                menu:
                                                                    "Impressive. You've been doing a lot.":
                                                                        jump cm_impress

                                                                        label cm_impress:

                                                                            c "Thaanks! Have you been doing this stuff too? I can't wait to see your creatures!"
                                                                            menu:
                                                                                "I've been working on it.":
                                                                                    jump cm_working
                                                                                "I haven't gotten around to it yet.":
                                                                                    jump cm_around

                                                                                    label cm_working:

                                                                                        c "Awesome! What do you have?"
                                                                                        $ number = renpy.input("What creatures have you made?", length=128)

                                                                                        c "Wowwww. I wish I had thought of that."
                                                                                        jump cm_fun
                                                                                    label cm_around:
                                                                                        c "Well don't wait too long, ok? If you don't keep making your world, then we won't be able to talk to you anymore."
                                                                                        jump cm_fun

                                                                                        label cm_fun:

                                                                                            c "This has been a lot of fun. I'm glad you showed up."
                                                                                            menu:
                                                                                                "Me too.":
                                                                                                    jump cm_metoo

                                                                                                    label cm_metoo:

                                                                                                        "You and The Child sit quietly next to each other, coinhabiting a workspace."
                                                                                                        hide child onlayer Foreground

                                                                                                        centered "…"
                                                                                                        $ Child = False
                                                                                                        $ tracker += 1
                                                                                                        if tracker >= 3:
                                                                                                            jump cm_next
                                                                                                        else:
                                                                                                            jump cm_talk
            label cm_sp:

                "You approach The Student and The Parent. The two are mid-conversation."

                show parent onlayer Foreground at parent_right

                p "...and I was thinking Stoneborn would be a suitable name for their race."

                hide parent onlayer Foreground
                show student onlayer Foreground at student_right

                s "But hold on, just confirming that you're sure they won't come into conflict with the others' creations?"

                hide student onlayer Foreground
                show parent onlayer Foreground at parent_right

                p "Well, The Elder is still working on their denizens. I am not entirely finished myself. So I can't be sure that whatever is made next won't come into conflict."

                hide parent onlayer Foreground

                "The Student paces nervously back and forth."

                show student onlayer Foreground at student_right

                s "This is no good…All of these groups interacting with each other…It feels like it's only a matter of time until something bad happens…"

                hide student onlayer Foreground
                show parent onlayer Foreground at parent_right

                p "For all it's worth dear, I agree."

                hide parent onlayer Foreground
                show student onlayer Foreground at student_right

                s "Really?"

                hide student onlayer Foreground
                show parent onlayer Foreground at parent_right

                p "Absolutely. I have been hard at work to instill all my creations with a respect for others and the world around them. There's so much to be in balance with."

                hide parent onlayer Foreground
                show student onlayer Foreground at student_right

                s "The people, the creatures…"

                hide student onlayer Foreground
                show parent onlayer Foreground at parent_right

                p "The environment."

                hide parent onlayer Foreground
                show student onlayer Foreground at student_right

                s "What?"

                hide student onlayer Foreground
                show parent onlayer Foreground at parent_right

                p "Well, for these creatures to exist happily for all time, they must be at balance with their environment."
                p "They must be able to lead sustainable lives. One must take diet, size, rate of aging, and life cycle all into consideration."

                hide parent onlayer Foreground
                show student onlayer Foreground at student_right

                "The Student stops dead in their tracks. They look like they feel sick."

                s "I didn't even think about sustainability…"

                hide student onlayer Foreground
                show parent onlayer Foreground at parent_right

                p "It's quite important dear. And you must answer not only the question of your creatures' abilities to sustain themselves, but also if they will be in harmony with their surroundings."
                p "Will they destroy them without even noticing? And if they do so, are such things moral?"

                hide parent onlayer Foreground

                "The Student holds their head. A strained whining noise emits from them."

                menu:
                    "...":
                        jump cm_watch
                    "Ok, I think they've had enough.":
                        jump cm_stop

                        label cm_watch:
                            show parent onlayer Foreground at parent_right

                            p "Presently, I am merely focusing on the sustainability of my Stoneborn, but eventually I hope to analyze them for what they represent in context with the dream world, as well as the world our friend has created."
                            p "And speaking of our friend, here they are now."

                            "The Parent turns to gesture to you."

                            hide parent onlayer Foreground
                            show student onlayer Foreground at student_right

                            s "Help me…"

                            menu:
                                "Perhaps The Student would like to come talk with me?":
                                    jump cm_save

                        label cm_stop:
                            show parent onlayer Foreground at parent_right


                            p "Oh my! My apologies dear, how long have you been standing there? Here, come and join in our conversation."
                            menu:
                                "Perhaps The Student would like to come talk with me?":
                                    jump cm_save

                                    label cm_save:

                                        p "Certainly! Would you like that dear?"

                                        hide parent onlayer Foreground
                                        show student onlayer Foreground at student_right

                                        "The Student quickly straightens up and hurries towards you."

                                        s "Wonderfulconversationthankyoubye!"

                                        "The Student walks past you, indicating for you to follow them. The Parent waves to you both as you leave. You catch up to The Student, who is walking fast."
                                        hide student onlayer Foreground
                                        menu:
                                            "How are you doing?":
                                                jump cm_how
                                            "That sounded really stressful.":
                                                jump cm_stress

                                                label cm_how:
                                                    show student onlayer Foreground at student_right

                                                    s "Well between the thousands of different potential problems that could arise between tens of thousands of entities in our world, I would say I'm doing pretty bad."
                                                    jump cm_sad

                                                label cm_stress:

                                                    "The Student quickens their pace."
                                                    show student onlayer Foreground at student_right

                                                    s "Mhm! Yep! It sure was!"
                                                    jump cm_sad

                                                    label cm_sad:
                                                        "The Student sighs, and comes to a stop."

                                                        s "How could I not have considered the sustainability of it all? The environment? And all those other things The Parent mentioned?"

                                                        s "...I just don't know how I'm ever going to be able to do this."
                                                        menu:
                                                            "Why not?":
                                                                jump cm_whynot

                                                                label cm_whynot:

                                                                    "The Student looks at you, bewildered."

                                                                    s "What?"
                                                                    menu:
                                                                        "You're really good at making stuff, so why wouldn't you be able to do this?":
                                                                            jump cm_good

                                                                            label cm_good:

                                                                                s "Well…I…I just don't have the time to make it right!"
                                                                                menu:
                                                                                    "So are you not going to do this project?":
                                                                                        jump cm_fail

                                                                                        label cm_fail:

                                                                                            s "What? No, of course I'm going to…"

                                                                                            "The Student turns inward. You hear their thoughts as though they were your own."

                                                                                            s "Huh…"

                                                                                            s "I don't want to stop working on the project. I want to keep going. I need to keep going."
                                                                                            s "This world has been the best thing I've ever done. The only thing I've ever done. The first thing I've ever done. So…so…"
                                                                                            menu:
                                                                                                "So you have to do something.":
                                                                                                    jump cm_something

                                                                                                    label cm_something:

                                                                                                        s "I have to do something. But I don't know the right way to start…"
                                                                                                        menu:
                                                                                                            "Will you ever know?":
                                                                                                                jump cm_ever
                                                                                                            "Is there even a right way?"
                                                                                                                jump cm_ever

                                                                                                                label cm_ever:

                                                                                                                    s "I…I don't know. I guess not. If I have to do it the right way, but I can't find the right way, then…"

                                                                                                                    "The Student's mind becomes a buzz of multilayered voices, all bouncing off one another. The sound magnifies to a roaring storm of opinions and ideas. All of a sudden, the storm subsides."

                                                                                                                    s "I need to think. I need just a bit more time. I have to figure out what this means for me."

                                                                                                                    s "There needs to be a reason for all of this. Even if it's a small one. A reason why I choose things to be the way that they will. Does that make sense?"

                                                                                                                    s "We all have a reason for doing what we do. The others do. Even you do. What was your reason? Why did you make your world and the denizens in it the way that you did?"

                                                                                                                    s "I just need more time."

                                                                                                                    "The Student nods to you."

                                                                                                                    s "Thank you for your understanding. And for all your help."

                                                                                                                    hide student onlayer Foreground

                                                                                                                    centered "…"

                                                                                                                    $ Student = False
                                                                                                                    $ tracker += 1

                                                                                                                    if tracker >= 3:
                                                                                                                        jump cm_next
                                                                                                                    else:
                                                                                                                        jump cm_talk
            label cm_elder:

                "The Elder sits quietly by themselves. Their usual demeanor of indifference has been replaced by one of focus. They stretch a mote of Knowledge out, forming a thin sheet of light."
                menu:
                    "Stare from a distance.":
                        jump cm_stare

                    "Approach respectfully.":
                        jump cm_approach

                        label cm_stare:
                            "You stay where you are and watch quietly. The Elder seems to be speaking to themselves, under their breath."
                            "Eventually, you are caught in the corner of their eye. They move towards you."
                            show elder onlayer Foreground at elder_right
                            jump cm_upset
                        label cm_approach:

                            "You carefully approach The Elder and their work. You hear them muttering something under their breath. The words escape you, save for the last two."

                            show elder onlayer Foreground at elder_right

                            e "...the end."

                            "The Elder turns to look at you."
                            jump cm_upset

                            label cm_upset:

                                e "The Student seemed a bit upset. You talked to them?"
                                menu:
                                    "Yes.":
                                        jump cm_yes

                                        label cm_yes:

                                            "The Elder nods."

                                            e "Like I said, it's always one thing or another around here."
                                            e "Poor kid, hands too full, head too heavy. A stressed out collaborator is no good for anyone. And that gift of theirs…"
                                            menu:
                                                "What's wrong with their gift?":
                                                    jump cm_wrong

                                                    label cm_wrong:
                                                        e "Nothing's wrong with it. Just…if it was me, I would've paired them with a different gift is all. To be honest, I probably know how to handle time far better than they do."
                                                        e "They get all caught up in its flow, but I'm the one who's at its end. I'll be there to catch anyone who reaches the end of their journey."
                                                        menu:
                                                            "Maybe you two could...switch?":
                                                                jump cm_switch

                                                                label cm_switch:

                                                                    "The Elder shrugs."

                                                                    e "They made their choice. If I wanted it, I should've acted sooner, before they chose it for themselves. Besides, I think I've finally found something."
                                                                    menu:
                                                                        "Your gift?":
                                                                            jump cm_e_gift

                                                                            label cm_e_gift:

                                                                                e "Yep. Everyone's getting into making this world, so I guess I better get on board or I'm going to be the one holding everyone back."
                                                                                e "I figured that the creatures of this world could use a little guidance. The creators of it too. Just like The Student said."

                                                                                "The Elder stretches the sheet out even more, and starts tracing a pattern in it."

                                                                                e "My gift will be the gift of stories. There will be tales of all kinds of creatures, tales that will help them become who they're supposed to be."
                                                                                e "In a way, the dreams we had were tales too. They were stories that helped us figure out what we wanted to do with this place. Sort of. Now there will be reminders of that dream throughout all of this world."

                                                                                "The Elder looks down at the inscribed sheet. The first story. They smile with satisfaction, as if forgetting all else. Then they catch you out of the corner of their eye again, and quickly regain their reserved exterior."

                                                                                e "At any rate, I hope you've been working on some creatures to populate your own world. You don't want to fall behind either."

                                                                                menu:
                                                                                    "Will do.":
                                                                                        jump cm_will

                                                                                    "Sure...":
                                                                                        jump cm_will

                                                                                        label cm_will:

                                                                                            e "Hey, make sure you’re taking it seriously. The Student was trying to slow things down, but they were right about one thing. There needs to be intention behind the living things in your world. They're the important part of it. If you haven't made cities, you should probably do that too."
                                                                                            e "Now stop bothering me, I need to work."
                                                                                            hide elder onlayer Foreground

                                                                                            "The Elder turns away."

                                                                                            centered "…"

                                                                                            $ Elder = False
                                                                                            $ tracker += 1

                                                                                            if tracker >= 3:
                                                                                                jump cm_next
                                                                                            else:
                                                                                                jump cm_talk
label cm_next:

    "The Parent, The Child, and The Elder all speak with one another. They are comparing their creations. The Child spots you and beckons you over."

    show child onlayer Foreground at child_right

    c "C'mere, c'mere!"

    hide child onlayer Foreground
    show parent onlayer Foreground at parent_right

    p "Let us tell each other of all that we've made thus far."
    hide parent onlayer Foreground
    menu:
        "But we're missing someone.":
            jump cm_missing

            label cm_missing:

                "The Child looks around and counts the number of entities. The Elder nods, yet does not move from their place. The Parent looks concerned."

                show parent onlayer Foreground at parent_right

                p "This is true! Where is The Student?"

                hide parent onlayer Foreground
                show elder onlayer Foreground at elder_right

                "The Elder waves at you."

                e "You should go look for them. Tell them it's time."

                hide elder onlayer Foreground

                "The space around is expansive. The recent additions create obstacles that obscure your search."

                "After some time, you find The Student. They sit isolated, a weeping cloud of emotions hanging over them. They hide their face from you."

                menu:

                    "Sit with them quietly":
                        jump console_one

                    "What's going on?":
                        jump console_two

                        label console_one:

                            "The Student accepts your presence. Their cloud rages and writhes. Eventually, they speak."
                            jump console_three

                        label console_two:

                            s "..."
                            jump console_three

                            label console_three:
                                show student onlayer Foreground at student_right
                                s "It's just…so hard…to…"

                                s "to let go…"

                                s "to let go of what I want…

                                "The Student looks at you"

                                s """
                                There were so many things I wanted to do…

                                There was a way I wanted this to go…

                                I know that if I had just been able to do it that way, it would have been so good

                                It would have been SO GOOD
                                """

                                "The cloud above explodes outward with a thundering cry"

                                s "But I can’t do that. I can’t make it how I wanted. I just have to…"

                                menu:

                                    "...let go?":
                                        jump cm_letgo

                                    "...trust the process?":
                                        jump cm_letgo

                                        label cm_letgo:

                                            s """

                                            Yeah…

                                            Is that what you learned to do?
                                            """

                                            menu:

                                                "I did":
                                                    jump cm_resolution_one

                                                "I'm trying to...":
                                                    jump cm_resolution_two

                                                    label cm_resolution_one:

                                                        "The Student nods"

                                                        s """

                                                        I see.

                                                        Well, if you did it…

                                                        Perhaps I can too.
                                                        """
                                                        menu:
                                                            "Perhaps":
                                                                jump cm_ending

                                                    label cm_resolution_two:

                                                        "The Student looks down"

                                                        s """

                                                        I see…

                                                        …

                                                        Then I suppose it’s something we both need to learn.

                                                        Together?
                                                        """

                                                        menu:
                                                            "Together":
                                                                jump cm_ending

                                                                label cm_ending:

                                                                    "The Student stands. Their cloud has mostly dissipated, and they look towards the direction you came from"

                                                                    s "The others are waiting, yes?"

                                                                    "You nod"

                                                                    s "It is time. I better be…I am ready."
                                                                    hide student onlayer Foreground

                                                                    "The two of you walk back to the rest of the group. They greet you both with welcoming camaraderie."

                                                                    show parent onlayer Foreground at parent_right

                                                                    p "Lovely to have both of you back with us. Now, shall we all go around and say what we've created?"

                                                                    hide parent onlayer Foreground
                                                                    show student onlayer Foreground at student_right

                                                                    "The Student glances at you, and nods."

                                                                    hide student onlayer Foreground
                                                                    show child onlayer Foreground at child_right

                                                                    c """

                                                                    I made the God of light, and magical people that are the Children of the Light, and some plant dogs named Puplants!

                                                                    They helped me come up with the name.
                                                                    """

                                                                    hide child onlayer Foreground
                                                                    show parent onlayer Foreground at parent_right

                                                                    "The Parent laughs."

                                                                    p """

                                                                    I have founded the society of underground giants known as the Stoneborn. They will help hold up the ground beneath the feet of others.

                                                                    I have also created the God of the Hearth, so that all may know a welcoming home.

                                                                    Lastly, we have the Travelers, beings that can step out of the world in one place, and back into it in another.
                                                                    """

                                                                    hide parent onlayer Foreground
                                                                    show elder onlayer Foreground at elder_right

                                                                    e """

                                                                    We got The Driven. They all know how to be mighty warriors of one kind or another.

                                                                    Then we got Kurrents. They're like…ummm…ghosts. They travel all over, floating along the paths of people or things until they come to their end.

                                                                    Does that make sense?
                                                                    """

                                                                    "The others shrug."

                                                                    e """
                                                                    Well, whatever.

                                                                    The last thing I made was the God of Skies and Storms. There, that's all of them.

                                                                    """

                                                                    "They all look at The Student."

                                                                    e "And you?"

                                                                    hide elder onlayer Foreground
                                                                    show student onlayer Foreground at student_right

                                                                    "The Student looks at you, then takes a deep breath."

                                                                    s """

                                                                    First, there are the Knowledge Keepers. They store information in their skin, and pass it on to future generations.

                                                                    They will be able to slowly accrue more and more knowledge, and better themselves with it.

                                                                    Then there are the Changelings. At first they appear to be mundane animals, but if their environment turns unsuitable, they can slowly change to adapt to their surroundings. 

                                                                    They won't be able to do this often, so they will be faced with making tough decisions.

                                                                    Just like me.

                                                                    But if there's one thing I've learned, it's that making tough decisions can hopefully make us stronger.
                                                                    """

                                                                    "The Student smiles gently. Their flame burns just a bit brighter."

                                                                    s "And then there's the God of Eyes. The keeper of truths. Another entity that is closer to the goings on in the world than we might be, and can better determine what needs to happen."
                                                                    

                                                                    s "At least, if we need to step in."

                                                                    s "…So…that's all of mine."
                                                                    

                                                                    hide student onlayer Foreground
                                                                    show parent onlayer Foreground at parent_right

                                                                    "The Parent nods, smiling."

                                                                    p "And what did you make, friend?"

                                                                    hide parent onlayer Foreground

                                                                    $ number = renpy.input("What did you make?", length=124)

                                                                    show child onlayer Foreground at child_right

                                                                    c "Grrreeat!! Everyone did such a good job! It’s time to offishally give our world life!"

                                                                    hide child onlayer Foreground
                                                                    show parent onlayer Foreground at parent_right

                                                                    p "Indeed!"

                                                                    hide parent onlayer Foreground
                                                                    show student onlayer Foreground at student_right

                                                                    s "Woo hoo!"

                                                                    hide student onlayer Foreground

                                                                    "The Elder tries to hide a grin."

                                                                    "Tens of thousands of small sparkles of light drift towards the map. Each one will go on to become their own creature, living, breathing, and ready to greet a new world."
                                                                    jump rs

                                
return