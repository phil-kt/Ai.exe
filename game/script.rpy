# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define protag = Character("Naoto", color = "#AAFF8D", show_two_window = True)
define teacher = Character("Teacher", color = "FFFFFF", show_two_window = True)
define ie = DynamicCharacter('ie_tan', color="#2672EC", show_two_window = True, image = "ie")
define chrome = DynamicCharacter('kuromi', color = "666666", show_two_window = True, image = "chrome")
define mozilla = DynamicCharacter("mojira", color = "#FF9500", show_two_window = True, image = "mozilla")

image chrome neutral = "images/chrome/chrome_neutral_small.png"
image chrome happy = "images/chrome/chrome_happy_small.png"
image chrome angry = "images/chrome/chrome_angry_small.png"
image chrome embarrassed = "images/chrome/chrome_embarrassed_small.png"
image chrome sad = "images/chrome/chrome_sad_small.png"
image chrome crying = "images/chrome/chrome_crying_small.png"
image chrome surprised = "images/chrome/chrome_surprised_small.png"

image chrome snow neutral = "images/chrome/chrome_snow_neutral_small.png"
image chrome snow happy = "images/chrome/chrome_snow_happy_small.png"
image chrome snow angry = "images/chrome/chrome_snow_angry_small.png"
image chrome snow embarrassed = "images/chrome/chrome_snow_embarrassed_small.png"
image chrome snow sad = "images/chrome/chrome_snow_sad_small.png"
image chrome snow crying = "images/chrome/chrome_snow_crying_small.png"
image chrome snow surprised = "images/chrome/chrome_snow_surprised_small.png"

image ie neutral = "images/ie/ie_neutral_small.png"
image ie happy = "images/ie/ie_happy_small.png"
image ie angry = "images/ie/ie_angry_small.png"
image ie embarrassed = "images/ie/ie_embarrassed_small.png"
image ie sad = "images/ie/ie_sad_small.png"
image ie crying = "images/ie/ie_crying_small.png"
image ie surprised = "images/ie/ie_surprised_small.png"

image ie snow neutral = "images/ie/ie_snow_neutral_small.png"
image ie snow happy = "images/ie/ie_snow_happy_small.png"
image ie snow angry = "images/ie/ie_snow_angry_small.png"
image ie snow embarrassed = "images/ie/ie_snow_embarrassed_small.png"
image ie snow sad = "images/ie/ie_snow_sad_small.png"
image ie snow crying = "images/ie/ie_snow_crying_small.png"
image ie snow surprised = "images/ie/ie_snow_surprised_small.png"

image mozilla neutral = "images/mozilla/mozilla_neutral_small.png"
image mozilla happy = "images/mozilla/mozilla_happy_small.png"
image mozilla angry = "images/mozilla/mozilla_angry_small.png"
image mozilla embarrassed = "images/mozilla/mozilla_embarrassed_small.png"
image mozilla sad = "images/mozilla/mozilla_sad_small.png"
image mozilla crying = "images/mozilla/mozilla_crying_small.png"
image mozilla surprised = "images/mozilla/mozilla_surprised_small.png"

image mozilla snow neutral = "images/mozilla/mozilla_snow_neutral_small.png"
image mozilla snow happy = "images/mozilla/mozilla_snow_happy_small.png"
image mozilla snow angry = "images/mozilla/mozilla_snow_angry_small.png"
image mozilla snow embarrassed = "images/mozilla/mozilla_snow_embarrassed_small.png"
image mozilla snow sad = "images/mozilla/mozilla_snow_sad_small.png"
image mozilla snow crying = "images/mozilla/mozilla_snow_crying_small.png"
image mozilla snow surprised = "images/mozilla/mozilla_snow_surprised_small.png"

image bg desk = "images/bg/desk.jpg"
image bg desk_broken = "images/bg/desk_broken.jpg"
image bg classroom = "images/bg/class.jpg"
image bg black = "images/bg/black.jpg"
image bg hallway = "images/bg/hallway.jpg"
image bg student_council = "images/bg/student_council.jpg"
image bg lab = "images/bg/lab.jpg"
image bg art_wall = "images/bg/art_wall.jpg"
image bg library = "images/bg/library.jpg"
image bg fountain_evening = "images/bg/fountain_evening.jpg"
image bg outside_dorm = "images/bg/outside_dorm.jpg"
image bg cafe = "images/bg/cafe.jpg"

image thanks = "images/thanks_small.png"

# The game starts here.
label start:
    

    $ ie_flag = 0
    $ chrome_flag = 0
    $ mozilla_flag = 0

    $ ie_shopping_date = False
    $ chrome_cafe_date = False
    $ mozilla_skate_date = False

    $ ie_tan = "???"
    $ kuromi = "???"
    $ mojira = "???"

    scene bg desk

    play music "sounds/music/lessBass.wav"

    protag "\"Troll.\""

    protag "\"Idiot.\""

    protag "\"Newfag.\""

    "My name is Naoto Takamura, 14 year old freshman."

    "I've always been a shut in."

    "Since I can remember I've always been the kid on his computer, rather than the one on the playground."

    "Tag and hide 'n seek, sports, these things never interested me."

    "They all seem to boring in comparison to what you can do online."

    "Lead an army of thousands against another, talk with people from around the world about how stupid people are, porn."

    "I recognize that it's unhealthy, however I manage to get by day to day without anyone thinking I'm a freak."

    "But ever since I started high school, my social aversion has only gotten worse."

    "I never saw myself going to college. So instead of going to a 'normal' high school, I decided to apply to a technical high school."

    "North Tech High. It sounds like one of those schools they advertise on television, right?"

    "It's actually a pretty legitimate school, with entrance exams and everything. Not super easy to get into."

    "They aim to make you employable straight out of graduation, and have a pretty good placement rate."

    "However, the first year here is pretty much a joke. At least for someone like me who has pretty much been around computers 24/7."

    "When I came here, I thought the people would be like me, you know, socially awkward outcasts."

    "It turns out even at nerd school you have cliques."

    "Kids who play League of something or watch Boku no Pico, they all clump up into their own groups. "

    "I never could fit in to any of them."

    "After the first week or so I stopped attending classes."

    "It didn't seem worth my time to go."

    "Honestly, I can't wait for these four years to be ov-"

    scene bg desk_broken

    protag "\"Hey!\"" with hpunch 

    "What's going on?" with vpunch

    "What the hell, a fatal system error!?"

    "This is great."

    "My internal monologue is all screwed up."

    scene bg black

    "----7 days later----"

    scene bg classroom
    with wipeleft

    "You'd think an IT school would have competent repair services for computers"

    "Surprisingly, that isn't the case."    

    "Now I'm stuck with a non-working computer and no money for a new one."

    "I've even started going to class to do something to pass the time."

    "So here I sit listening to the student council president go on about ever important student council matters."

    show chrome neutral
    
    chrome "\"...Christmas party at the end of the month. Right now we're looking for organizers, so please stop by the student council room after school if you're interested!\""

    "That's Kuromi, our student council president."

    $ kuromi = "Kuromi"

    "She's pretty strict and serious. However, as you can see she's pretty, so she also has a fair amount of popularity. At least among the guys."

    "Ever since she got into office, she's always been trying to put into place new policies for the students."

    "Sometimes they're pretty good, like a unified school-wide mailing system, but sometimes they're pretty bad."

    "I remember she once tried to put in place a social network for classes, and boy did that backfire. No one ended up using it."

    "Overall I'd say she does a good job as a leader though."

    chrome "\"Thank you for listening. Hope to see you all after class!\""

    hide chrome
    with dissolve

    teacher "\"Okay, thank you Kuromi. Now moving onto class. Today we are covering...\""

    "Finally, it's lunch time."

    "I don't know how much longer I could listen to that teacher drone on."

    "As usual, everyone splits up to sit with their own little group of friends."

    "I watch from my desk alone, isolated. An island unto myself."

    ie "\"Naoto-kun, you came to school today!\""

    show ie happy
    with dissolve

    ie "\"I've been so worried! Where have you been lately? How come you haven't come to class?\""

    ie "\"All the lunches I've been making for you have gone to waste...at least today they won't!\""

    protag "\"Elsie?\""

    "This is Elsie, my childhood friend."

    "Pretty much the only one I have."

    "We lived next to each other as kids and always went over to each other's houses to play games."

    "We've been around each other ever since."

    "She even took an interest in tech stuff, I guess from being around me all the time."

    "She's not very good at it though."

    $ ie_tan = "Elsie"

    ie neutral "\"Heeellooooo are you spacing out again.\""

    protag "\"Oh uhhh. Kinda.\""

    protag "\"What are you doing here? Why aren't you in your class?\""

    ie "\"I decided to wander over here as I've noticed you haven't been around lately.\""

    ie "\"Staying cooped up in your dorm is not healthy you know!\""

    protag "\"I know, I know. \""

    ie "\"So you want to eat lunch together with me for once instead of being all alone?\""

    menu:
        "\"Yeah, okay.\"":
            ie "Yay! Let's eat. It's been a while since we've talked."
        "\"No thanks Elsie, I'm good.\"":
            ie happy "I won't take no for an answer!"
            "Of course she wouldn't."

    ie neutral "\"Here, I made your favorite, steamed beef over rice with broccoli.\""

    protag "\"You know I hate broccoli.\""

    ie happy"\"Hehe, but your mom always tells you to eat it.\""

    protag "\"You don't have to listen to every thing my mom says.\""

    show ie neutral

    "I chow down on the beef and rice, carefully avoiding the broccoli."

    "It's surprisingly good. Elsie was never the best at cooking, but it looks like dorm life has brought out a bit of the chef in her."

    ie angry "\"Don't think I don't see you!\""

    ie "\"You're only going to get paler if you don't eat it!\""

    protag "\"Sigh, alright alright. You got me.\""

    show ie neutral

    "I silently chew down my broccoli just as I hear the bell ring."

    "Thank god."

    ie surprised"\"Oh, lunch is over. If you wanna walk home together I'll be by the front gates for a bit after class!\""

    hide ie
    with dissolve

    "And with that she returned to her class."

    teacher "\"Okay, resuming where we left off.\""

    "Oh boy, another monotone lecture to doze off to."

    teacher "\"Takamura-san, you look bored. Could you answer this next question?\""

    "Crap, I wasn't paying attention at all."

    protag "\"S-sure I can.\""

    "Why did I just say that. I have no idea what we're covering."

    teacher "\"What is the name of the language used to create the basis of a website?\""

    menu:
        "\"CSS\"":
            teacher "\"Sorry, that's not right. Maybe you should pay better attention in class, Takamura-kun.\""
            "I hear snickers around me."
            "What did I expect. I should've just admitted I wasn't looking."
        "\"HTML\"":
            teacher "\"Correct. And here I thought you weren't paying attention. Moving on.\""
            "He continues with his lecture as I bask in the small pride of answering correctly."

    play sound "sounds/effects/bell.mp3"

    "Finally, I hear the bell signaling the end of class."

    "I mechanically pack up my bags, and quickly try to rush out the classroom."

    stop sounds fadeout 1.0

    "I walk out the door and-"

    mozilla "\"Eeep\"" with vpunch

    protag "\"Ooomp\"" with vpunch

    "I feel a thud of pain in my chest."

    "I think I hit something."

    "Or rather, someone."

    "I look down and see the cause of my pain."

    "A red-headed girl, with a large blue pin in her hair, sits on the ground."

    protag "\"Sorry! I didn't see where I was going.\""

    "I offer my hand to help her up."

    show mozilla neutral
    with easeinbottom

    mozilla "\"Ow. No no, it's my fault.\""

    mozilla "\"I got so lost that I didn't look where I was going.\""

    mozilla "\"I just transferred here so I've been running around trying to find where to go.\""

    protag "\"Oh, you're a new student? What are you looking for?\""

    mozilla "\"I'm trying to find the faculty office. Do you think you could help me?\""

    protag "\"Oh yeah, sure.\""

    "I have nothing better to do anyway."

    scene bg hallway

    protag "\"Just follow me, the faculty office isn't far.\""

    mozilla happy "\"Thanks, you're a lifesaver!\""

    protag "\"No problem. So, a transfer student huh?\""

    protag "\"Isn't a bit late to transfer? I mean, we're already in winter.\""

    mozilla neutral "\"Haha, yeah maybe. My dad is a programmer and his job takes him all around the globe.\""

    mozilla "\"This time he brought us to Japan as he works on some new web browser.\""

    protag "\"Your dad's a programmer? Well then you'll fit right in here.\""

    mozilla "\"Thanks, saying that he hasn't taught me much though.\""

    mozilla "\"I came to this school to learn more about what he does, and maybe pick up my own skills.\""

    protag "\"Well, the curriculum is pretty good, so you'll probably learn a lot while you're here.\""

    "Or at least, I hear it's good. I mainly pass based on my prior knowledge."

    "We walk down the various twists and turns and arrive in front of the faculty office."

    protag "\"Well, here we are.\""

    mozilla happy "\"Thanks so much for your help! I never would have found this place on my own.\""

    mozilla "\"Oh, what was your name by the way? I don't think I caught it. Mine is Mosaic.\""

    $ mojira = "Mosaic"

    protag "\"I'm Naoto. Mosaic? That's a pretty interesting name.\""

    mozilla neutral "\"Yeah, my mom is an artist and she got to chose the name.\""

    mozilla "\"If my dad had his way I'd be named Godzilla or something, hehe.\""

    mozilla happy "\"Anyway, thanks again! Maybe we'll end up in the same class.\""

    "I wouldn't count on myself being so lucky..."

    protag "\"Yeah, that'd be cool. Well...see you around.\""

    mozilla "\"Bye!\""

    hide mozilla
    with dissolve

    scene bg fountain_evening

    "I slowly meander out the front gates of the school."

    "What a cute girl, I wonder where she's originally from."

    "Certainly not Japanese with that red hair."

    show ie angry
    with dissolve

    ie "\"Hey! You're late!\""

    protag "\"Elsie? You were still here?\""

    ie "\"Yeah. It's not good to keep a lady waiting you know.\""

    ie "\"What were you doing, hitting on girls?\""

    protag "\"No, nothing like that. I was just helping a new transfer student find the faculty office.\""

    "...But I guess in a literal sense I did just \"hit\" on a girl."

    ie surprised "\"A transfer student at this time of year? How rare!\""

    protag "\"Yeah, it seems like she's a foreigner as well.\""

    ie "\"A foreigner? You have to introduce me!\""

    protag "\"Yeah, yeah, I'll get right on it.\""

    "Elsie and I walked home as she raved on and on about the new student she hadn't even met."

    hide ie
    with dissolve

    scene bg desk_broken

    "Finally I crash through my door into my room."

    "What an exhausting day."

    "But...it was kind of refreshing to go to school every once in a while."

    "The last thoughts of the day drift through my mind as my head hit the pillow."

    scene bg black

    $ renpy.pause()

    play sound "sounds/effects/alarm.mp3"

    "Ugh."

    "My alarm."

    "It's too early."

    stop sound

    $ renpy.pause();

    scene bg desk_broken

    play sound "sounds/effects/alarm.mp3"

    "Ugh."

    "My alarm."

    stop sound

    "Wait."

    "What time is it?"

    "11?"

    "...11?"

    "......11!?"

    protag "\"Crap, I'm late!\""

    scene bg outside_dorm

    "I take a shower and rush out the door, running full sprint to school."

    "*huff* *huff* *huff*"

    "I forgot how hard it is to run. *huff*"

    "And to think I used to be in decent shape in middle school."

    "Curse this digital age."

    "I slowly make my way up the stairs and make it to my classroom"

    scene bg classroom

    teacher "Ah, Takamura-san, how nice of you to join us."

    "Yeah, yeah, hilarious."

    protag "\"Sorry, I overslept.\""

    teacher "\"That much is evident by your hairstyle. Now please find a seat.\""

    "The classroom is filled with snickers."

    "How do they like his jokes?"

    "I slowly make my way to my seat and promptly lie my head to down to disappear for a bit."

    "The lunch bell chimes as I feel a prodding in my side."

    show ie happy
    with dissolve

    ie "\"Hey, hey. Wake up Naoto-kun!\""

    "Elsie, huh. Well maybe I can just nap for a bit before she wakes me up completely."

    ie angry "\"Are you ignoring me? Well then, I didn't want to do this but...\""

    "I feel her slowly wriggling her fingers near my gut as-"

    protag "\"HAHAHAHAHAHAHA OH GOD ELSIE STOP YOU KNOW I'M SUPER TICKLISH THERE.\""

    "My head lifts up without my control as I roil back laughing."

    show ie happy

    "Elsie stops moving her fingers, and I am greeted by the sight of my fellow classmates all staring at me."

    "One of these classmates includes the new transfer student."

    "Great, less than a day into class and I've already embarrassed myself in front of her."

    "I try my best to stare daggers in Elsie's direction."

    protag "\"What do you want?\""

    ie neutral "\"Well, I was going to offer you lunch, but you seem to be in a bad mood.\""

    ie "\"Oh, it seems that the student council president wants to see you in the hallway.\""

    protag "\"Kuromi? Why would she want to see me?\""

    ie "\"Maybe it has to do with your tardiness today.\""

    protag "\"Yeah that could be it. Wait, how do you know I was late today?\""

    ie "\"I took a peek into your class this morning and saw you weren't there.\""

    ie happy "\"Maybe I should be taking the liberty of waking you up to ensure you wake up on time.\""

    chrome "\"Takamura-kun, I'm waiting.\""

    protag "\"Oh, sorry! Coming now.\""

    ie neutral "\"*whisper* Don't get in trouble! *whisper*\""

    scene bg hallway

    "I walk out into the hallway to meet Kuromi."

    "What in God's name could she want from me?"

    show chrome neutral
    with dissolve

    chrome "\"Takamura-kun, I'm sorry to call you out.\""

    protag "\"No, it's alright. I was late today so the least I can expect is a talking to from the student council president.\""

    chrome "\"Well actually, that's not the entire reason why I called you out here.\""

    "What could she mean?"

    protag "\"Huh?\""

    chrome "\"The truth is, you've missed so many classes this semester that the teacher told me you were in danger of failing.\""

    "WHAAAAAAAT!? Failing?" with vpunch

    "This is what I get for eschewing my lectures in favor of debating the superiority of Magic to Yugioh."

    protag "\"Are you serious?\""

    chrome "\"Yes. The teacher told me in hopes that we could possibly strike out some sort of deal so you could still pass this year.\""

    chrome "\"As, despite your attendance, you seem to be quite the competent student.\""

    "I didn't exactly enroll here on a whim."

    chrome "\"So I offered a compromise to the teacher.\""

    chrome "\"You'll be allowed to pass this semester, if you continue to attend every class from now until winter vacation.\""

    chrome "\"And you'll also have to join the student council.\""

    protag "\"The student council!?\""

    chrome "\"Yes. This is a non-negotiable part of the deal. It's to show you have some capacity of responsibility towards the school.\""

    "Responsibility!? I've taken charge of thousands of virtual soldiers in wars spanning across the galaxy and you think I can't attend a school council?"

    "Also, why don't I get a say in this?"

    "But I don't want to get expelled. My parents are disappointed in me as is."

    protag "\"I understand. I guess I see where you and the teacher are coming from.\""

    chrome happy "\"Great! Come down to the student council room after class today then, and we'll get you started.\""

    protag "\"Okay, I will see you then.\""

    scene bg classroom

    play sound "sounds/effect/bell.mp3"

    "The bell chimes signifying the end of lunch."

    "I walk back into class just as Elsie is leaving."

    stop sound fadeout 1.0

    show ie surprised

    ie "\"You were out there for a while, what were you talking about?\""

    protag "\"Apparently I've been drafted to become a part of the student council.\""

    ie happy "\"You? In the student council? That's too funny haha!\""

    protag "\"Yeah, yeah. Head back to your class.\""

    ie "\"Okay, have fun in the student council after class Mr. Executive.\""

    hide ie
    with dissolve

    "And with that clever comment she exits the room."

    teacher "\"Alright, everyone find your seats.\""

    "Based on Kuromi's talk I guess I'd better start paying more attention to these lectures if I want to keep going here."

    "I try my best not to fall asleep; as fascinating as a lecture on the history of Internet browsers is."

    "The bell rings and people begin to file out."

    "I see Kuromi dart out of class. Must be heading down to the council room."

    "Guess I better follow her lead."

    mozilla "\"Ah Naoto-kun!\""

    scene bg hallway

    "I hear someone call my name as I walk down the hall."

    "Sorry, no time to chat this afternoon."

    "I make way down the hall towards the student council office and find myself standing in front of the door."

    "I can't muster up the courage to knock."

    "What's the matter dude, just go in."

    "Why are you so nervous?"

    "You were summoned here, you can't just bail."

    "Don't you want to pass school?"

    "All of a sudden the door opens in front of me."

    show chrome neutral

    chrome "\"What are you doing out here? I've been waiting. Come in!\""

    protag "\"Yeah, s-sorry for being late.\""

    "Damn it why am I nervous?"

    "She's just a student council president for Christ's sake!"

    scene bg student_council

    "I enter the room and look around."

    "It's a nice lounge, lots of seats and bookshelves."

    "However...no one else seems to be in the room."

    chrome "\"Here, take the papers. I need you to file them for our class's Christmas party.\""

    protag "\"Oh yeah, sure.\""

    chrome "\"If you have any questions feel free to ask.\""

    hide chrome
    with dissolve

    "Maybe the other members will come later."

    "I sit down and start going through the papers in silence."

    "Wow, we really don't have all that much of a budget."

    "I had no idea Kuromi was working with such a tight budget."

    "I wonder how she got all those initiatives passed..."

    "I really wish some other students would come and help lighten this load though."

    "If this is what I'm going to be doing for the rest of the semester, I'll never get home before the sun sets."

    protag "\"Umm...Kuromi?\""

    chrome "\"What is it Takamura-kun?\""

    protag "\"When do you think the other student council members will arrive?\""

    protag "\"I'd really appreciate some help with these council files.\""

    chrome "\"Oh, no one else is coming.\""

    protag "\"Huh, why not?\""

    show chrome embarrassed

    chrome "\"Well...the truth is.\""

    chrome "\"I'm the only one on the student council.\""

    "...what."

    protag "\"You're joking, right?\""

    chrome angry "\"No I'm not joking!\""

    chrome "\"I work my hardest to make up for the lack of members!\""

    chrome "\"So if I can handle all these student council matters I trust you can file some papers!\""

    "Ah crap, I really hit a sweet spot didn't I."

    protag "\"Sorry, I didn't mean to make you angry.\""

    chrome neutral "\"Whatever, just file those papers.\""

    hide chrome
    with dissolve

    "With a heavy atmosphere, I went back to filing the class's receipts for the council's expenditures."

    "The school clock chimes that it's six o' clock."

    "I've been here for two and a half hours already."

    show chrome neutral
    with dissolve

    chrome "\"Um, Takamura-kun, I think that's enough work for today.\""

    protag "\"Oh, okay.\""

    chrome embarrassed "\"I'm sorry for flying off the handle earlier.\""

    protag "\"Oh no, it's fine. I'm sure it must be stressful doing this all alone.\""

    chrome neutral "\"Still, I feel bad for roping you into this for my own selfish benefit.\""

    chrome "\"Please at least allow me to buy you dinner at the cafeteria tonight as an apology.\""

    menu:
        "\"Sure, why not.\"":
            chrome happy "\"Great! Just let me clean up here and we can go.\""
            $ chrome_flag += 1
            jump dinner

        "\"Sorry, I'm kinda tired.\"":
            chrome sad "\"Oh, okay. Sorry for making you do so much work today.\""
            protag "\"It was no problem, anything to pass right?\""
            protag "\"I'll see you tomorrow.\""
            chrome neutral "\"Okay, have a good night.\""
            hide chrome
            with dissolve
            jump home

    label dinner:

        scene bg cafeteria

        show chrome neutral

        "The two of us left the school and made our way towards the on campus cafeteria."
        
        "The food here is never that great, but I guess I can't complain much as it saves me time."

        chrome happy "\"What would you like to eat Takamura-kun? My treat.\""

        protag "\"Naoto-kun is fine, Kuromi. I've already started calling you by your first name anyways.\""

        chrome embarrassed "\"Oh, sorry, Naoto. What would you like?\""

        protag "\"Um, it's okay, you really don't have to pay for me.\""

        chrome happy "\"It's fine, I insist. The student council gets a discount anyways!\""

        "Really? Finally a perk of this job."

        chrome neutral "\"Although I don't know if that applies to those who were forced to join.\""

        "Figures."

        protag "\"Okay, I guess I'll get the eel bowl then.\""

        chrome "\"Well, make that two eel bowls please!\""

        "We find a seat and wait for out eel bowls to come to us."

        protag "\"So...I've been dying to ask this, but why are you the only one in the student council?\""

        show chrome surprised

        protag "\"Sorry if it's a bit rude, you don't have to answer.\""

        chrome neutral "\"No, it's okay. I am sure I would ask if I were in your position.\""

        chrome "\"The truth is last year the student council was run by a bunch of seniors who had iron-like control over the school.\""

        chrome "\"After they left, no one was interested in taking over for them except me.\""

        chrome sad "\"I've tried finding new members, but no one wants to take on the work of the student council.\""

        "Crap, I mad her sad. Better try and change the subject."

        protag "\"Well, I'll do my best to try and lighten your load.\""

        protag "\"Even if I was forced into it, I'll give the student council my best effort!\""

        chrome happy "\"Thanks Naoto, that means a lot to me!\""

        chrome neutral "\"Oh look, our eel bowls are here, let's eat!\""

        "We dig into our meal and split up afterward."

        chrome happy "\"Thank you for all your hard work today!\""

        hide chrome
        with dissolve

        jump bedtime

    label home:
        scene bg desk_broken
        
        "I trudge my way home, exhausted from looking at papers all day."

        "As I enter my room and lie down, I shortly hear a knock at my door."

        protag "\"Who is it?\""

        ie "\"It's Elsie. I figured you were hungry after the student council.\""

        ie "\"Do you want to eat with me? I made some food.\""

        menu:
            "\"Sure, sounds great Elsie.\"":
                $ ie_flag += 1 
                jump home_dinner

            "\"I'm too tired, I'm just gonna crash.\"":
                ie "\"Oh, okay Naoto. Good night then!\""
                jump bedtime

        label home_dinner:
            scene bg desk_broken

            protag "\"Just come in, the door's open.\""

            ie "\"Okay.\""

            show ie surprised
            with dissolve

            ie "\"Wow this place is a pigsty!\""

            "I knew that was coming."

            ie neutral "\"Get up! I'll make space in your room so we can eat dinner.\""

            "I struggle to escape the lure of my comfy bed."

            ie "\"Here, I made some rice balls with grilled fish. It's a simple meal, I know.\""

            protag "\"Sometimes simple is nice. I think this is just what I needed.\""

            "I take a rice ball from Elsie's hand, and place it into my mouth."

            "The rice is still warm, and it almost melts into my mouth."

            "This seems to kickstart the hunger in my stomach, and it responds accordingly."

            play sound "sounds/effects/stomach.mp3"

            ie happy "\"Hehe, is is good?\""

            protag "\"Very.\""

            stop sound

            "I manage to speak while stuffing food into my mouth."

            ie neutral "\"I'm glad you like it. It's always better to eat with someone.\""

            protag "\"I agree. Thank you so much Elsie.\""

            protag "\"Without you I would have starved.\""

            ie "\"You're welcome, I'm glad I could keep your stomach from eating itself.\""

            protag "\"This warm food has made me all sleepy.\""

            ie "\"It is late. I think it's time for bed.\""

            ie "\"Try to wake up on time tomorrow!\""

            protag "\"I will, I will. \""

            ie "\"Okay, good night Naoto!\""

            protag "\"Good night Elsie.\""

            hide ie
            with dissolve
            jump bedtime

    label bedtime:
        scene bg desk_broken

        "Oh man, what a tiring day."

        "Ever since I've started going to class it seems like I get one job after the other."

        "It is keeping my busy though."

        "Much better than sitting around wasting my energy on the Internet all day."

        "Although I do kind of miss playing my visual novels."

        "I was about to reach the true ending!"

        "*sigh* I guess I'll have to wait 'til Christmas to see the ending."

        scene bg black

    scene bg desk_broken 

    play sound "sounds/effects/alarm.mp3"

    $ renpy.pause()

    "My alarm again."

    stop sound

    "Time to actually get up."

    "...But bed is so warm."

    "I really can't be late though, or otherwise this might be my last winter in this bed."

    "Struggling, I get up and walk to class."

    scene bg classroom

    "I get to class before the teacher starts homeroom."

    "I'm surprised how early I made it in."

    if ie_flag == 1:
        show ie happy
        with dissolve

        ie "I'm glad you made it today!"
        
        protag "\"Yeah, the dinner last night really helped me sleep well.\""

        ie "\"Great, I have to go back to class now but I'll see you at lunch!\""

        hide ie
        with dissolve

    elif chrome_flag == 1 :
        show chrome happy
        with dissolve

        chrome "\"Naoto-kun, happy to see you came to class on time today.\""

        protag "\"Yeah, It was a real struggle, but I realize I had to in order to keep my seat.\""

        chrome "\"That's a good attitude to have. I'll see you after school at student council!\""

        hide chrome
        with dissolve

    else:
        "I put my head down and fall asleep until the teacher comes in."

    teacher "All right everyone to your seats!"

    "I promptly lie my head back down to my desk."

    scene bg black

    "I feel something hit my back."

    "Oh crap, did I fall asleep?"

    scene bg classroom
    with fade

    "I look around my desk and see a crumpled up note next to me."

    "Puzzled, I look around, but no one looks back."

    "I open the note."

    mozilla "Hi Naoto-kun, I've only been here two days but I already understand why you fall asleep hehe."

    "A note from Mosaic? I scribble back:"

    protag "Haha, you too huh? This teacher knows just the right tone to knock me out."

    "I sneakily toss it back towards her."

    "She picks up the note and giggles at what I wrote."

    "She writes a response, and tosses it back."

    mozilla "You even slept through lunch! Yeah, I'm always feeling sleepy too! This is helping keep me awake."

    "Crap. I slept through lunch? I can't believe Elsie didn't wake me up."

    mozilla "By the way, would you mind showing me around the school again today?" 

    "After class...I have the student council."

    teacher "\"Takamura-kun, are you exchanging notes in my class?\""

    "Caught red-handed."

    protag "\"No sir, I was merely taking notes on a small piece of paper.\""

    protag "\"It makes carrying around the subject material much easier so I can study wherever I am.\""

    teacher "\"Uh huh. Well I'll have my eye on you for the rest of the class.\""

    "Well I guess that ends note swapping time."

    "I look back at Mosaic and give a little shrug."

    "She shrugs back."

    play sound "sounds/effects/bell.mp3"

    "Hey, class is over!"

    "I get up and walk across to Mozilla."

    stop sound fadeout 1.0

    show mozilla neutral

    mozilla embarrassed "\"Sorry I almost got you in trouble.\""

    protag "\"It's no big deal.\""

    mozilla happy "\"Yeah, you managed to give a pretty smooth response. It was funny.\""

    protag "\"Haha, thanks. In response to the question in your note by the way.\""

    menu:
        "I have student council today, so sadly I can't":
            $ chrome_flag += 1
            mozilla sad "\"Oh really? You're on the student council?\""
            protag "\"Yeah, as of yesterday. It's so I can pass this class.\""
            mozilla neutral "\"That's so sudden! Well I understand, it's for school. Maybe next time.\""
            protag "\"Sorry about that.\""
            mozilla "\"It's okay! I have to get going now, so bye!\""
            protag "\"Bye Mosaic.\""
            hide mozilla
            with dissolve
            jump student_council

        "I'd love to show you around the school":
            $ mozilla_flag += 1
            "I'm sure Kuromi can handle herself one day."
            mozilla happy "\"Yay! Thank you. Sorry for taking time out of your schedule.\""
            protag "\"It's no big deal. I didn't really have any other plans.\""
            mozilla "\"Okay, let's go!\""
            jump school_tour

    label student_council:
        scene bg hallway

        "I walk out of the classroom down to the student council room."

        "This time I knock on the door with no fear."

        protag "\"Naoto Takamura, reporting for duty.\""

        scene bg student_council
        with None

        show chrome happy
        with dissolve

        chrome "\"Oh good you're here, I've been waiting!\""

        chrome neutral "\"Today we're gonna be working on flyers for the class's Christmas party.\""

        chrome happy "\"So I hope you'll show me your artistic side today.\""

        protag "\"Oh man, I really can't draw.\""

        chrome neutral "\"Don't say that without even trying!\""

        protag "\"No trust me, I haven't touched a marker in years.\""

        chrome "\"Well you never know. Here! Draw something.\""

        "I take paper from Kuromi's hand a attempt to a Christmas tree."

        chrome "\"Um, Naoto-kun, why does that smokestack have presents underneath it?\""

        protag "\"It's not a saw it's a Christmas tree!\""

        chrome happy "\"Oh I see. You were right, you really can't draw haha.\""

        "I told you..."

        chrome neutral "\"Well okay. Don't worry about the drawing part then.\""

        chrome "\"I'm pretty good at doodling so I'll handle it, you just try to come up with a good slogan.\""

        protag "\"A...slogan? For a class Christmas party?\""

        chrome happy "\"Yeah! Something that will want to make people come and celebrate the holidays with their classmates!\""

        protag "\"Huh, I guess I can try.\""

        show chrome neutral

        "A slogan for a Christmas party?"

        protag "\"Come spread cheer with your classmates!\""

        protag "\"A festive event for finals!\""

        protag "\"Gift giving without gimping!\""

        chrome "\"Please to think quietly, I can't focus on my drawing.\""

        protag "\"Oh, sorry Kuromi.\""

        "The rest of the time passed in silence as I though of slogans watching Kuromi draw."

        scene bg student_council
        with wipeleft

        show chrome neutral

        chrome "\"Okay, I think it's about time to go.\""

        chrome "\"Did you manage to think of anything?\""

        protag "\"What about, \'Forget Starcraft, embrace Secret Santa!\'\""

        chrome "\"...keep thinking about it tonight.\""

        "Guess that one didn't work."

        chrome happy "\"Good night Naoto.\""

        protag "\"Yeah, 'night Kuromi. I'll see you tomorrow.\""

        hide chrome
        with dissolve

        jump bedtime2


    label school_tour:

        scene bg hallway

        "We walked out into the hallway of our class."

        protag "\"So, what exactly would you like to see?\""

        mozilla "\"Everything!\""

        protag "\"Everything huh. Well our school isn't that big so it might not take long.\""

        mozilla "\"That's okay, as long as I get a feel for the place.\""

        mozilla happy "\"I can't keep getting lost in my own school now, can I?\""

        show bg lab
        with pixellate

        show mozilla surprised

        protag "\"This is the lab. It's where we work on most of our coding assignments.\""

        mozilla surprised"\"Ooo coding? I wonder when I'll start to do that.\""

        protag "\"Well I'm pretty sure we have a homework due at the end of the semester dedicated to the code we learned.\""

        protag "\"So I'm guessing pretty soon.\""

        protag "\"Other than that a lot of people use the lab to play flash games and generally goof off.\""

        mozilla happy "\"Like that guy playing Pacman over there?\""

        "There was a person playing Pacman."

        "Pacman Player" "Goddamn you Blinky! I was on the last pellet!"

        "They didn't seem to be all that great at it though."

        protag "\"Yeah, like that guy playing Pacman.\""

        show mozilla neutral

        show bg library
        with pixellate

        protag "\"This is the library.\""

        protag "\"It's your standard fare, with a lot of books about technology.\""

        "Mosaic picked a random book off the shelf."

        mozilla neutral "\"\'The Algorithm Design Manual\', sounds boring.\""

        protag "\"Yeah, mostly only the upperclassmen hang around here.\""

        protag "\"For beginners like us we're better off just reading notes.\""

        mozilla "\"You have to teach me sometime so I can catch up!\""

        protag "\"Sure, that sounds like a good way to brush up on my skills too.\""

        scene bg art_wall
        with pixellate

        show mozilla surprised

        mozilla "\"Woooww, I didn't know this school had arts stuff too!\""

        "Mosaic stared intently at the wall of art."

        protag "\"Yeah, we have some students who are interested in graphic design so they like to sprinkle the campus with their art.\""

        show mozilla neutral

        protag "\"I don't really get it, but it makes this campus look cheerier so I don't mind.\""

        protag "\"Anyway, that's pretty much for a tour of the school.\""

        mozilla neutral "\"Oh, thank you so much Naoto! I know you must be busy and I feel bad for making you take me around.\""

        protag "\"It's fine, like I said I didn't really have another plans.\""

        "Man if Kuromi heard me I probably would be kicked out of school on the spot."

        mozilla "\"Next time I'll have us do something more fun.\""

        mozilla "\"It's late so I should get going home.\""

        mozilla happy "\"Thanks again for showing me around!\""

        protag "\"You're welcome!\""

        hide mozilla
        with dissolve

        jump bedtime2

    label bedtime2:
        scene bg desk_broken

        "Man, I'm exhausted."

        "Every day seems to get busier and busier."

        "Still, feeling tired at the end of the day is a good feeling."

        "Before I used to just sleep at any time I felt like and was always in my bed."

        "Now I feel like I accomplished something in the day."

        "These thoughts drift around in my head as I fall asleep."

        scene bg black

    $ renpy.pause()

    play sound "sounds/effects/alarm.mp3"

    "Another day."

    stop sound

    "Time to get up."

    scene bg classroom

    teacher "\"Good morning class, in case you forgot, tomorrow we will be having an exam on this material.\""

    "Wait, did he just say test."

    "He did say test, didn't he?"

    "Why didn't he mention this sooner?!"

    "Tomorrow? Well I think I'm comfortable enough with this material to pass an exam."

    "I feel a piece of paper hit my back."

    "Another note."

    mozilla "Did he just say test? ;_;"

    "I start to write my just as shocked reply:"

    teacher "*cough*"

    "..and promptly stop. I guess I'm being watched now."

    "I appear to hang on to the teacher's every word for the rest of the lecture."

    play sound "sounds/effects/bell.mp3"

    "Whew, finally lunch."

    stop sound fadeout 1.0

    ie "NAOTOOO HEEEELLP MEEEE!!!!"

    show ie crying
    with vpunch

    protag "\"Woah, Elsie, what's wrong?!\""

    ie "\"We've got a test tomorrow and I'm bound to fail.\""

    "Ah, so that's it."

    "I figured this might happen, she always depended on me in middle school for tests."

    protag "\"Yes, Elsie, I can help.\""

    ie happy "\"Really Naoto? You're the best!\""

    "What a quick turnaround."

    show mozilla neutral at right

    mozilla "\"Ah, Naoto-kun. I was wondering whether you might be able to help me study for this test.\""

    ie surprised "\"Oh my god are you the transfer student? You must be with that hair!\""

    mozilla embarrassed "\"Y-yes, I am.\""

    ie happy "\"You're soooooo pretty!\""

    ie "\"What's your name? Where are you from? How do you get your hair so nice!\""

    protag "\"Stop it Elsie, you're scaring her.\""

    ie neutral "\"Ooops, sorry. Hi, I'm Elsie. Naoto's childhood friend.\""

    mozilla happy "\"It's okay. I'm Mosaic, a transfer student from America. And your hair is nice too Elsie.\""

    ie happy "\"You really think so? A pretty girl from America complimented my hair I can die happy Naoto.\""

    "Talk about dramatic."

    protag "\"Rest in peace Elsie.\""

    ie crying "\"Wait noooo I can't die until I pass this test. Help me Naoto!!\""

    ie neutral "\"Oh yeah, Mosaic, you said you needed help too? Why don't we all study together?\""

    protag "\"Well I don't know if-\""

    mozilla happy "\"That sounds good to me!\""

    "Well that settles it."

    show chrome neutral at left

    chrome angry "\"Do you guys mind being a bit quieter? Some of us are trying to eat.\""

    ie neutral"\"Oh, sorry Kuromi, I'm just super worried about this test.\""

    show mozilla neutral

    chrome neutral "\"I understand Madou-san, but I think our class would like to have some quiet while eating.\""

    chrome "\"That being said, I heard you all were planning to hold a study session for tomorrow's test?\""

    ie happy "\"That's the plan.\""

    chrome "\"Well if you'd like you can hold your review session in the student council office.\""

    "Kuromi looked straight at me."

    chrome "\"That way you can work on your council duties while teaching.\""

    if mozilla_flag == 1:
        "No escaping this time."

    protag "\"Of course I'll be there.\""

    protag "\"Is that okay with you two?\""

    ie "\"Yay I get to study with Kuromi-chan and Mosaic-chan!\""

    mozilla "\"It's fine with me.\""

    chrome "\"Settled then, just come right after class.\""

    play sound "sounds/effects/bell.mp3"

    ie surprised "\"Oop, lunch is over, gotta run!\""

    ie neutral "\"Bye Kuromi, bye Mosaic, bye Naoto!\""

    stop sound fadeout 1.0

    hide ie
    with dissolve

    teacher "\"Okay everyone lunch time is over.\""

    mozilla "\"See you after class.\""

    hide mozilla
    with dissolve

    chrome "\"See you at the student council room.\""

    hide chrome
    with dissolve

    "Great, now I've become the lead of my own little study group."

    "I'll just listen to lecture and hope I can absorb some of what he's saying."

    scene bg classroom
    with wipeleft

    play sound "sounds/effects/bell.mp3"

    "Finally class is over."

    stop sound fadeout 1.0

    show ie neutral

    ie "\"C'mon Naoto let's go!\""

    "She sure is fast."

    protag "\"Yeah hold on just let me get Mosaic.\""

    show mozilla neutral at left

    mozilla "\"I'm right behind you.\""

    protag "\"Alright, let's go then.\""

    scene bg hallway

    "We make our way down to the student council office."

    scene bg student_council
    with None

    show chrome neutral
    with dissolve

    "Kuromi was already there waiting for us, and had cleared away a table."

    show ie happy at right 

    show mozilla neutral at left

    ie "\"Hi Kuromi!\""

    chrome "\"Hello Madou-san, Roelle-san, Naoto-kun.\""

    ie "\"You can just call me Elsie, just like Naoto does.\""

    mozilla "\"And please, just call me Mosaic.\""

    chrome "\"Okay, Kuromi is fine for me too.\""

    chrome "\"So why don't we start studying?\""

    ie "\"Kuromi's gonna study with us too? Yay!\""

    chrome "\"Yes, to be honest I was going to ask Naoto to help me as well seeing as he gets the best grades in the class.\""

    "How did she know that?"

    mozilla surprised "\"Really Naoto-kun? You're the top in our class?\""

    protag "\"Well I don't like to advertise it, but yeah. I am.\""

    mozilla "\"Wow, that's amazing!\""

    ie "\"Yup, that's why I always ask him to help me with my work!\""

    protag "\"She's been doing so since we met.\""

    ie neutral "\"Thanks you for all the good grades Naoto, don't fail me this time either\""

    protag "\"Yeah, yeah Elsie. Just listen to what I say and you won't fail.\""

    hide mozilla
    hide ie
    hide chrome

    "The rest of the night went by quickly as I answered question after question on computer history and structure."
    
    show mozilla neutral

    mozilla "\"Naoto, what do RAM and CPU stand for?\""

    hide mozilla
    with fade

    show chrome neutral
    with fade

    chrome "\"Naoto-kun, in the cache how do you determine what block is least recently used?\""

    hide chrome
    with fade

    show ie crying

    ie "\"NAAOOOTTTOOOO. Who is this 4chan guy the professor mentioned??\""

    hide ie
    with fade

    scene bg student_council
    with wipeleft

    show chrome neutral 
    show ie happy at right
    show mozilla happy at left

    "Finally, it's over."

    protag "\"Does everyone feel prepared for tomorrow's test now?\""

    ie "\"Very! Thank you as always Naoto!\""

    mozilla neutral "\"Yeah, thank you Naoto-kun. Despite just transferring I feel prepared for our exam.\""

    mozilla happy "\"Maybe you should be the one teaching our class.\""

    chrome "\"I'm glad we all got to review like this together.\""

    chrome "\"Perhaps we could all exchange phone numbers so next time this happens we could organize it without disrupting lunch?\""

    protag "\"Well if the student council president says so I doubt we have much choice, haha.\""

    show chrome angry

    "My remark was rewarded with a glare."

    ie "\"Now I have Kuromi's and Mosaic's phone numbers! Yay! \""

    ie "\"I'll make sure to text you guys tonight!\""

    mozilla "\"Hehe I look forward to it Elsie.\""

    protag "\"Alright, now that that's finished let's all go home. Teaching is exhausting.\""

    scene bg desk_broken
    with wipeleft

    "I stumble into my room with my mind running on empty."

    "At least the girls treated me to dinner on the way back as thanks."

    "Still, I should start charging for my tutoring services, especially for Elsie."

    "*bzzzt*"

    "I feel my phone vibrate in my pocket."

    "It looks like I have a text."

    ie "Thank you so much again Naoto! If I do well on tomorrow's test, would you like to go shopping this weekend to celebrate? :) :)"

    "A sweet text from Elsie. At least I know I'm appreciated."

    "I see that I also have two other texts that I must have missed earlier."

    mozilla "Thank you Naoto-kun for today's review. :) I would have been totally lost without you T_T"

    mozilla "If you'd like, and weather permitting, would you like to go ice skating this weekend as my thanks? Let me know ^^"

    "Ice skating huh..."

    "And one last text."

    chrome "Naoto, the tutoring session today was really helpful. I know I kind of barged in on it, but I really needed the assistance so thank you!"

    chrome "If you'd like, would you like to go to a cafe this weekend as my treat for getting me caught up?"

    "Oh boy...three different texts from three different girls."

    "I've never had this problem before."

    "What am I supposed to do?!"

    "I guess I have to accept one invitation and decline the others."

    "But what if the other two find out?!"

    "Maybe I should just tell them all I'm busy."

    "That's the safest bet."

    "But on the other hand...a night out doesn't sound so bad."

    "What should I do!?"

    menu:
        "Go shopping with Elsie":
            $ ie_shopping_date = True
            $ ie_flag += 1
            "Elsie's always fun to be around with, and maybe I can get her to buy me something."
            "That and I do need some new boots for winter."
            "I'll tell the other two that I'm busy this weekend."
            jump bedtime3

        "Ice skating with Mosaic":
            $ mozilla_skate_date = True
            $ mozilla_flag += 1
            "I haven't ice skated in forever."
            "Plus, Mozilla is new in town and probably doesn't have many friends."
            "I'd feel bad if she has to spend the weekend alone because I didn't agree to hang out."
            "I can hang out with the other two some other time."
            jump bedtime3

        "Cafe with Kuromi":
            $ chrome_cafe_date = True
            $ chrome_flag += 1 
            "If I get closer to Kuromi I may be able to escape this student council thing."
            "That, and I can never pass up free food."
            "I'll have to tell Elsie and Mosaic that I'm busy."
            jump bedtime3
        "None of them":
            "I really don't want to cause some sort of conflict here."
            "Plus, I don't even really know how I feel about these girls!"
            "I'll just tell them I'm busy and hang out with them later."
            jump bedtime3

    label bedtime3:
        "That was the first time I've had such a difficult decision to make."

        "At least I know I have something to do after this test."

        "Those girls wiped me out. Sleep is calling me."

        scene bg black

    scene bg outside_dorm

    "Man, that test was a breeze."

    "I even got to leave early and take a nap afterwards."

    "I hope the girls did as well I did."

    "That tutoring session should have helped them out quite a bit."

    if ie_shopping_date == True:
        jump ie_date

    elif mozilla_skate_date == True:
        jump mozilla_date

    elif chrome_cafe_date == True:
        jump chrome_date

    else:
        jump no_date

    label ie_date:
        "My phone rings, it's Elsie calling."

        protag "\"Elsie? You're done already?\""

        ie "\"H\""

        jump end

    label mozilla_date:

        jump end

    label chrome_date:
        "My phone rings, Kuromi is calling me."

    label no_date:
        "I can't believe you didn't pick a girl."

    label end:
        scene thanks

    $renpy.pause()

    "Credits" "Writing: Philippe Kimura-Thollander \n Programming: Philippe Kimura-Thollander \n Art: Roslyn Dong"

    return