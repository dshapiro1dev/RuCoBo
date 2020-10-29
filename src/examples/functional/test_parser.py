# Create a function that takes a large piece of text and breaks it apart
from super_parser import word_counter

# Referencing some truly great monologues from classic movies
rudyMono = "Since when are you the quitting kind? So you didn't make the dress list. There are greater tragedies in \
    the world... Oh, you are so full of crap. You're 5 feet nothin', a 100 and nothin', and you got hardly a speck of \
    athletic ability. And you hung in with the best college football team in the land for two years. And you're also \
    gonna walk outta here with a degree from the University of Notre Dame. In this lifetime, you don't have to prove \
    nothin' to nobody - except yourself. And after what you've gone through, if you haven't done that by now, it ain't \
    gonna never happen. Now go on back... Hell, I've seen too many games in this stadium...I've never seen a game from \
    the stands... I rode the bench for two years. Thought I wasn't bein' played because of my color. I got filled up \
    with a lotta attitude. So I quit. Still not a week goes by I don't regret it. And I guarantee a week won't go by \
    in your life you won't regret walkin' out, letting them get the best of ya. You hear me clear enough?"
caddyShackMono = "What an incredible Cinderella story! This unknown, comes out of nowhere, to lead the pack at \
    Augusta. He's at the final hole. He's about 455 yards away, he's gonna hit about a 2-iron, I think. Oh, he got all \
    of that. The crowd is standing on its feet here at Augusta. The normally reserved crowd is going wild...for this \
    young Cinderella who's come out of nowhere. He's got about 350 yards left, he's going to hit about a 5-iron, it \
    looks like, don't you think? He's got a beautiful backswing... that's- oh, he got all of that one! He's gotta be \
    pleased with that! The crowd is just on its feet here. He's a Cinderella boy. Tears in his eyes, I guess, as he \
    lines up this last shot. He's got about 195 yards left, and he's got a, looks like he's got about an 8-iron. This \
    crowd has gone deadly silent... Cinderella story, out of nowhere, former greenskeeper, now about to become the \
    Masters champion. It looks like a mirac- it's in the hole! It's in the hole!"
itsAWonderfulLifeMono = "Just remember this, Mr. Potter, that this rabble you're talking about, they do most of the \
    working and paying and living and dying in this community. Well, is it too much to have them work and pay and live \
    and die in a couple of decent rooms and a bath? Anyway, my father didn't think so. People were human beings to \
    him, but to you, a warped, frustrated old man, they're cattle. Well, in my book he died a much richer man than \
    you'll ever be... I know very well what you're talking about. You're talking about something you can't get your \
    fingers on, and it's galling you. That's what you're talking about, I know. Well...I've said too much. I -- You're \
    the Board here. You do what you want with this thing. There's just one thing more, though. This town needs this \
    measly one-horse institution if only to have some place where people can come without crawling to Potter"
jurassicParkMono = "Don’t you see the danger, John, in what you’re doing here? Genetic force is the most awesome power \
    the planet’s ever seen, but you wield it like a kid that found his dad’s gun. I’ll tell you the problem with the \
    scientific power that you’re using here. It didn’t acquire any discipline to attain it. You read what others have \
    done and you took the next step. You didn’t earn the knowledge for yourself so therefore you don’t take any \
    responsibility for it. You stood on the shoulders of geniuses to accomplish something as fast as you could and \
    before you even knew it you had it. You patented it and packaged it and slapped it on a plastic lunch box, and \
    now your selling it! You wanna sell it! Well, your scientists were so preoccupied with whether or not they could \
    they didn’t stop if they should. No, hold on John, this is not an animal wiped out by deforestation or the \
    building of a dam. Dinosaurs had their shot and nature selected them for extinction"


# call our shiny new function to parse through one of our monologues
wordCount = word_counter(caddyShackMono, 12)
# sort the results by the count and loop through the results
for word, count in sorted(wordCount.items(), key=lambda item: item[1], reverse=True):
    print(f"The word '{word}' was used {count} times")
