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

                                                    c "..."

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
        "Talk to The Student":
            jump gf_student

        "Talk to The Parent":
            jump gf_parent

        "Talk to The Elder":
            jump gf_elder

            label gf_student:
                $ Student = False
                if Child = True:
                    jump gf_child1

            label gf_parent:
                $ Parent = False
                if Child = True:
                    jump gf_child1
            label gf_elder:
                $ Elder = False
                if Child = True:
                    jump gf_child1            

                    label gf_child1:


                        "Before you reach your destination, you feel a presence at your side. You look down and see The Child, uncharacteristically dimmed."

                        show child onlayer Foreground at child_right

                        c "...what if I can't do it?"

                        menu:
                            "Can't do what?":
                                jump gf_cant

                                label gf_cant:

                                    c "What if I can't find my gift?"
                                    menu:
                                        "Why would you say that?":
                                            jump gf_why

                                            label gf_why:

                                                "The Child looks down."

                                                c "Well, The Student said this was my one gift. They already know what their gift is. But I don't know…"
                                                c "What if I just can't figure it out?"
                                                menu:
                                                    "Have you thought about it?":
                                                        jump gf_thought

                                                        label gf_thought:


                                                            c "Yeah…I thought about it a bit. I know I have ideas. But I'm not sure if they'll be as good as everyone else's."
                                                            c "I just don't know if I can do this right."
                                                            menu:
                                                                "You don't need to compare your ideas to others.":
                                                                    jump gf_compare
                                                                "The first step to making something good is getting started.":
                                                                    jump gf_first

                                                                    label gf_compare:

                                                                        c "Ok…Ok. Maybe you could still ask the others about their gifts? Just so we know what they are. Just so I don't do the same one…"
                                                                        jump gf_figure

                                                                    label gf_first:

                                                                        "The Child takes a breath."

                                                                        c "Ok…Ok. If you say I can do it, then I can do it. I'll get started. I can work on my ideas some more."
                                                                        jump gf_figure

                                                                        label gf_figure:
                                                                            menu:
                                                                                "You can do this!":
                                                                                    jump gf_cando

                                                                                    label gf_cando:

                                                                                        c "All right. Yeah! You're right! I can do this! I'm gonna go and figure out all the stuff about my gift!"
                                                                                        c "Thanks worldbuilder!"
                                                                                        hide child onlayer Foreground

                                                                                        "The Child runs off, shining brightly again."
                                                                                        if Student = False:
                                                                                            jump gf_student
                                                                                        else if Parent = False:
                                                                                            jump gf_parent
                                                                                        else:
                                                                                            jump gf_elder



return