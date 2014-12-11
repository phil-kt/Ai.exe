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

image ie neutral = "images/ie/ie_neutral_small.png"
image ie happy = "images/ie/ie_happy_small.png"
image ie angry = "images/ie/ie_angry_small.png"
image ie embarrassed = "images/ie/ie_embarrassed_small.png"
image ie sad = "images/ie/ie_sad_small.png"
image ie crying = "images/ie/ie_crying_crying.png"
image ie surprised = "images/ie/ie_surprised_small.png"

image mozilla neutral = "images/mozilla/mozilla_neutral_small.png"
image mozilla happy = "images/mozilla/mozilla_happy_small.png"
image mozilla angry = "images/mozilla/mozilla_angry_small.png"
image mozilla embarrassed = "images/mozilla/mozilla_embarrassed_small.png"
image mozilla sad = "images/mozilla/mozilla_sad_small.png"
image mozilla crying = "images/mozilla/mozilla_crying_small.png"
image mozilla surprised = "images/mozilla/mozilla_surprised_small.png"

image bg desk = "images/bg/desk.jpg"
image bg classroom = "images/bg/class.jpg"
image bg black = "images/bg/black.jpg"
image bg hallway = "images/bg/hallway.jpg"

# The game starts here.
label start:
    

    $ ie_flag = 0
    $ chrome_flag = 0
    $ mozilla_flag = 0

    $ ie_tan = "???"
    $ kuromi = "???"
    $ mojira = "???"

    scene bg desk

    protag "\"Troll.\""

    protag "\"Idiot.\""

    protag "\"Newfag.\""

    "I've always been a shut in."

    "Since I can remember I've been around computers and Internet games, talking and playing with people around the globe."

    "It's so much more interesting than the real world."

    "Not that there's anything wrong with real world."

    "It's just...not as good as my virtual one." 

    "But ever since I started high school, my social aversion has only gotten worse."

    "I never saw myself going to college. So instead of going to a 'normal' high school, I decided to apply to a technical high school."

    "It's a school designed to teach you applicable technology skills so you can graduate and get a job."

    "I figure work must be better than more school."

    "When I came here, I thought the people would be like me, you know, socially awkward losers."

    "It turns out even at nerd school you have cliques."

    "Kids who play League of something, watch a bunch of anime, they all clump up into their own groups. "

    "I never could fit in to any of them."

    "So instead I sit here arguing on Internet forums to pass my time."

    "Honestly, people online are so-"

    protag "Hey!" with hpunch 

    protag "What's going on?" with vpunch

    protag "What the hell, a blue screen!?"

    protag "This is great."

    protag "My internal monologue is all screwed up."

    $renpy.pause()

    scene bg classroom
    with wipeleft

    "----7 days later----"

    "You'd think an IT school would have competent repair services for computers"

    "Well...apparently not."    

    "Now I'm stuck with a non-working computer and no money for a new one."

    "I've even started going to class to do something to pass the time."

    "So I sit here listening to the student council president go on about student council matters."

    show chrome neutral
    
    chrome "...Christmas party at the end of the month. Right now we're looking for organizers, so please stop by the student council room after school if you're interested!"

    "That's Kuromi, our student council president."

    $ kuromi = "Kuromi"

    "She's pretty strict and serious. However, as you can see she's pretty so she also has a fair amount of popularity, at least among the guys."

    "Ever since she got into office, she's always trying to put into place new policies for the students."

    "Sometimes they're pretty good, like a unified school-wide mailing system, but sometimes they're pretty bad."

    "I remember she once tried to put in place a social network for classes, and boy did that backfire. No one ended up using it."

    "Overall I'd say she does a good job as a leader though."

    chrome "Thank you for listening. Hope to see you all after class!"

    hide chrome
    with dissolve

    teacher "Okay, thank you Kuromi. Now moving onto class. Today we are covering..."

    "Finally, it's lunch time."

    "I don't know how much longer I could listen to that teacher drone on."

    "As usual, everyone splits up to sit with their own little group of friends."

    "I watch from my desk alone, isolated. As usual."

    ie "\"Naoto-kun, you came to school today!\""

    show ie happy
    with dissolve

    ie "\"I've been so worried! Where have you been lately? How come you haven't come to class?\""

    ie "\"All the lunches I've been making for you have gone to waste...at least today they won't!\""

    protag "\"Elsie?\""

    "This is Elsie, my childhood friend."

    "We lived next to each other as kids and always went over to each other's houses to play games."

    "We've been around each other ever since."

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

            ie haopy "I won't take no for an answer!"
            "Of course she wouldn't."

    ie neutral "\"Here, I made your favorite, steamed beef over rice with broccoli.\""

    protag "\"You know I hate broccoli.\""

    ie happy"\"Hehe, but your mom always tells you to eat it.\""

    protag "\"You don't have to listen to every thing my mom says.\""

    "I chow down on the beef and rice, carefully avoiding the broccoli."

    "It's surprisingly good. Elsie was never the best at cooking, but it looks likes dorm life has brought out a bit of the chef in her."

    ie angry "\"Don't think I don't see you!\""

    ie "\"You're only going to get paler if you don't eat it!\""

    protag "\"Sigh, alright alright. You got me.\""

    "I silently chew down my broccoli just as I hear the bell ring."

    "Thank god."

    ie surprised"\"Oh, lunch is over. If you wanna walk home together I'll be by the front gates for a bit after class!\""

    hide ie
    with dissolve

    "And with that she returned to her class."

    teacher "\"Okay, resuming where we left off.\""

    "Oh boy, another monotone lecture to listen to."

    teacher "\"Tamura-san, you look bored. Could you answer this next question?\""

    "Crap, I wasn't paying attention at all."

    protag "\"S-sure I can.\""

    "Why did I just say that. I have no idea what we're covering."

    teacher "\"What is the name of the language used to make websites?\""

    menu:
        "\"CSS\"":
            teacher "\"Sorry, that's not right. Maybe you should pay better attention in class, Tamura-kun.\""
            "I hear snickers around me."
            "What did I expect. I should've just admitted I wasn't looking."
        "\"HTML\"":
            teacher "\"Correct. And here I thought you weren't paying attention. Moving on.\""
            "He continues with his lecture as I bask in the small pride of answering correctly."

    "Finally, I hear the bell signaling the end of class."

    "I mechanically pack up my bags, and quickly try to rush out the classroom."

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

    protag "\"Just follow me, the faculty office isn't far.\""

    mozilla happy "\"Thanks, you're a lifesaver!\""

    protag "\"No problem. So, a transfer student huh?\""

    protag "\"Isn't a bit late to transfer? I mean, we're already in winter.\""

    mozilla "\"Haha, yeah maybe. My dad is a programmer and his job takes him all around the globe.\""

    mozilla "\"This time he brought us to Japan as he works on some new web browser.\""

    protag "\"Your dad's a programmer? Well then you'll fit right in here.\""

    mozilla "\"Thanks, saying that he hasn't taught me much though.\""

    mozilla "\"I came to this school to learn more about what he does, and maybe pick up my own skills.\""

    protag "\"The curriculum is pretty good, so you'll probably learn a lot while you're here.\""

    "Or at least, I hear it's good. I mainly pass based on my prior knowledge."

    "We walk down the various twists and turns and arrive in front of the faculty office."

    protag "\"Well, here we are.\""

    mozilla "\"Thanks so much for your help! I never would have found this place on my own.\""

    mozilla "\"Oh, what was your name by the way? I don't think I caught it. Mine is Mosaic.\""

    $ mojira = "Mosaic"

    protag "\"I'm Naoto. Mosaic? That's a pretty interesting name.\""

    mozilla "\"Yeah, my mom is an artist and she got to chose the name.\""

    mozilla "\"If my dad had his way I'd be named Godzilla or something, haha.\""

    mozilla "\"Anyway, thanks again! Maybe we'll end up in the same class.\""

    "I wouldn't count on myself being so lucky..."

    protag "\"Yeah, that'd be cool. Well...see you around.\""

    mozilla "\"Bye!\""

    hide mozilla
    with dissolve

    "I slowly meandered out the front gates of the school."

    "What a cute girl, I wonder where she's originally from."

    "Certainly not Japanese with that hair color."

    show ie angry
    with dissolve

    ie "\"Hey! You're late!\""

    protag "\"Elsie? You were still waiting?\""

    ie "\"Yeah. It's not good to keep a lady waiting you know.\""

    ie "\"What were you doing, hitting on girls?\""

    protag "\"No, nothing like that. I was just helping a new transfer student find the faculty office.\""

    "...But I guess in a literal sense I did just \"hit\" on a girl."

    ie surprised "\"A transfer student at this time of year? How rare!\""

    protag "\"Yeah, it seems like she's a foreigner as well.\""

    ie "\"A foreigner? How cool! You have to introduce me!\""

    protag "\"Yeah, yeah, I'll get right on it.\""

    "Elsie and I walked home as she raved on and on about the new student she hadn't even met."

    hide ie
    with dissolve

    "Finally I crashed through my door into my room."

    "What an exhausting day."

    "It was refreshing to go to school every once in a while."

    "The last thoughts of the day drifted through my mind as my head hit the pillow."

    $ renpy.pause()

    scene bg desk

    "*BEEP BEEP BEEP*"

    "Ugh"

    "My alarm."

    "It's too early."

    "*boop*"

    $ renpy.pause();

    "*BEEP* *BEEP* *BEEP*"

    "Ugh"

    "My alarm."

    "Wait."

    "What time is it?"

    "11?"

    "...11?"

    "......11!?"

    "Crap, I'm late!"

    "I take a shower and rush out the door, running full sprint to school."

    "*huff* *huff* *huff*"

    "I forgot how hard it is to run. *huff*"

    "And to think I used to be in decent shape in middle school."

    "Curse this digital age."

    "I slowly make my way up the stairs make it to my classroom"

    teacher "Ah, Tamura-san, how nice of you to join us."

    "Yeah, yeah, hilarious."

    protag "\"Sorry, I overslept.\""

    teacher "\"That much is evident by your hairstyle. Now please find a seat.\""

    "The usual snickers abound."

    "I slowly make my way to my seat and promptly lie my head to down to disappear for a bit."

    "The lunch bell chimes as I feel a prodding in my side."

    show ie happy
    with dissolve

    ie "\"Hey, hey. Wake up Naoto-kun!\""

    "Elsie, huh. Well maybe I can just nap for a bit before she wakes me up completely."

    ie angry"\"Are you ignoring me? Well then, I didn't want to do this but...\""

    "I feel her slowly wriggling her fingers near my gut as-"

    protag "\"HAHAHAHAHAHAHA OH GOD ELSIE STOP YOU KNOW I'M SUPER TICKLISH THERE.\""

    "My head lifts up without my control as I roil back laughing."

    "Elsie stops moving her fingers, and I am greeted by the sight of my fellow classmates all staring at me."

    "One of these classmates includes the new transfer student."

    "Great, less than a day into class and I've already embarrassed myself for the rest of the semester."

    "I try my best to stare daggers in Elsie's direction."

    protag "\"What do you want?\""

    ie neutral "\"Well, I was going to offer you lunch, but you seem to be in a bad move."

    ie "Besides that, it seems that the student council president wants to see you in the hallway."

    protag "Kuromi? Why would she want to see me?"

    ie "Maybe it has to do with your tardiness today."

    protag "Yeah that could be it. Wait, how do you know I was late today?"

    ie "I took a peek into your class this morning and saw you weren't there."

    ie "Maybe I should be taking the liberty of waking you up to ensure you wake up on time."

    chrome "Tamura-kun, I'm waiting."

    protag "Oh, sorry! Coming now."

    ie "*whisper* Don't get in trouble! *whisper*"

    hide ie

    "I walk out into the hallway to meet Kuromi."

    "What in God's name could she want from me?"

    show chrome neutral
    with dissolve

    chrome "Tamura-kun, I'm sorry to call you out."

    protag "No, it's alright. I was late today so the least I can expect is a talking to from the student council president.\""

    chrome "Well actually, that's not the entire reason why I called you out here."

    "Huh, what could she mean?"

    protag "\"Huh?\""

    chrome "\"The truth is, you've missed so much school this semester that the teacher told me you were in danger of failing.\""

    "WHAAAAAAAT!? Failing?"

    "This is I what I get for eschewing my lectures in favor of hunting down karmawhores on Reddit."

    protag "\"Are you serious?\""

    chrome "\"Yes. The teacher told me in hopes that we could possibly strike out some sort of deal so you could still pass this year.\""

    chrome "\"As, despite your attendance, you seem to be quite the competent student.\""

    "I didn't exactly enroll here on a whim."

    chrome "\"So I struck out a deal with the teacher.\""

    chrome "\"You'll be allowed to pass this semester, if you continue to attend every class from now until winter vacation.\""

    chrome "\"And you'll also have to join the student council.\""

    protag "\"The student council!?\""

    chrome "\"Yes. This is a non-negotiable part of the deal. It's to show you have some capacity of responsibility towards the school.\""

    "Responsibility!? I've taken charge of thousands of virtual soldiers in wars spanning across the galaxy and you think I can't attend a school council?"

    protag "\"I understand. I guess I see where you and the teacher are coming from.\""

    chrome happy "\"Great! Come down to the student council room after class today then and we'll get you started.\""

    protag "\"Okay, I will see you then.\""

    hide chrome
    with dissolve

    "The bell chimes signifying the end of lunch."

    "I walk back into class just as Elsie is leaving."

    show ie neutral

    ie "\"You were out there for a while, what were you talking about?\""

    protag "\"Apparently I've been drafted to become a part of the student council.\""

    ie happy "\"You? In the student council? That's too funny haha!\""

    protag "\"Yeah, yeah. Head back to your class.\""

    ie "\"Okay, have fun in the student council after class Mr. Executive.\""

    hide ie
    with dissolve

    "And with that clever comment she leaves the room."

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

    "Damn it why do I get nervous around authority figures."

    "She's just a student council president for Christ's sake!"

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

    "I had no idea Kuromi was working with so little tender."

    "I really wish some other students would come and help lighten this load though."

    "If this is what I'm going to be doing for the rest of the semester, I'll never get home before the sun sets."

    protag "\"Umm...Kuromi?\""

    chrome "\"What is it Tamura-kun?\""

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

    "Ah crap I really hit a sweet spot didn't I."

    protag "\"Sorry, I didn't mean to make you angry.\""

    chrome "\"Whatever, just file those papers.\""

    hide chrome

    "With a heavy atmosphere, I went back to filing the class's receipts for the council's expenditures."

    "The school clock chimes that it's six o' clock."

    "I've been here for two and a half hours already."

    show chrome neutral
    with dissolve

    chrome "\"Um, Tamura-kun, I think that's enough work for today.\""

    protag "\"Oh, okay.\""

    chrome "\"I'm sorry for flying off the handle earlier.\""

    protag "\"Oh no, it's fine. I'm sure it must be stressful doing this all alone.\""

    chrome "\"Still, I feel bad for roping you into this for my own selfish benefit.\""

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
            chrome "\"Okay, have a good night.\""
            hide chrome
            with dissolve
            jump home

    label dinner:
        show chrome neutral

        "The two of us leave the school and make our way towards the on campus cafeteria."
        
        "The food here is never that great, but I guess I can't complain much as it saves me time."

        chrome "\"What would you like to eat Tamura-kun? My treat.\""

        protag "\"Naoto-kun is fine, Kuromi. I've already started calling you by your first name anyways.\""

        chrome "\"Oh, sorry, Naoto. What would you like?\""

        protag "\"Um, it's okay, you really don't have to pay for me.\""

        chrome happy "\"It's fine, I insist. The student council gets a discount anyways!\""

        "Really? Finally a perk of this job."

        chrome "\"Although I don't know if that applies to those who were forced to join.\""

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

        chrome "\"Oh look, our eel bowls are here, let's eat!\""

        "We dig into our meal and split up afterward."

        chrome "\"Thank you for all your hard work today!\""

        hide chrome
        with dissolve

        jump bedtime

    label home:
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
            protag "\"Just come in, the door's open.\""

            ie "\"Okay.\""

            show ie surprised
            with dissolve

            ie "\"Wow this place is a pigsty!\""

            "I knew that was coming."

            ie neutral "\"Get up! I'll make space in your room so we can eat dinner.\""

            "I struggle to escape the lure of my comfy bed."

            ie "Here, I made some rice balls and fish. It's a simple meal, I know."

            protag "\"Sometimes simple is nice. I think this is just what I needed.\""

            "I take a rice ball from Elsie's hand, and place it into my mouth."

            "The rice is still warm, and it almost melts into my mouth."

            "This seems to kickstart the hunger in my stomach, and it responds accordingly."

            play sound "sounds/effects/stomach.mp3"

            ie happy "\"Hehe, is is good?\""

            protag "\"Very.\""

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

    label bedtime:

    return