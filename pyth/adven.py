from typing import Annotated, Dict, Literal, TypeVar, Union, final
import time

Storyline = Dict[str, Annotated[Dict, ...]]

story: Storyline = {"Your pet pig has escaped from your home! You need to get him back! You could search the forest, one of your rooms, or go to the roof for a better view.": {
    'forest': {'You enter the forest and notice some broken sticks and leaves following a direction. You can follow it, or go elsewhere.': {
        'follow': {'You follow the path and find it stops at a river, but in the corner of your eye, you find a pig attracting-horn. You can grab and blow it, or look around elsewhere.': {'blow': {'You grabbed the horn and blew it, and you heard a noise from outside the forest, you go over and see that the pig evolved a pair of wings, and was flying away to a mountain. You could evolve your own wings and catch it, or go back home.': {'evolve': 'You evolved your own wings that were more powerful than the pig\'s, caught it, and went back home together to live happily ever after.', 'quit': 'You went back home and your pig flew into the sunset, never ot be seen again.'}}, 'elsewhere': 'You found your pig near the mountain, it grew wings and was about to fly away! But luckily, you got there just in time to catch it. Nice.'}}, 
        'elsewhere': {'You walked in another direction and found a pink tail-like feature poking out a bush! Do you grab it, or sneak up?': {'grab': {'It was a decoy! The pig left a sock there and you triggered the trap, now it\'s skateboarding away. But look, there\'s an abandoned car at the side of the road.': {'drive': 'You drove faster than it could skateboard! You caught your pig!'}}, 'sneak': 'The pig had found a skateboard and was preparing to skate away, however, you snuck up on it right before it took off and caught him! Well done.'}}}},

    'room': {'You found an open window with footprints. Is it bait? Do you follow, or go the other direction?': {
        'other': {'You find skateboard tracks leading into the forest, you could grab your hoverboard and follow it, but that would be loud but faster, or could follow it silently, but slow in the shadows.': {'hoverboard': 'The sound didn\'t matter, your board was so fast you caught it even while letting the pig know where you were.', 'sneak': {"You found your pig that evolved wings and was about to take flight! Do you sprint and jump for it, or grow your own wings?": {"jump": 'You caught it! Nice jump.', 'wings': 'It took longer than if you were to jump, but you caught it as well. Congrats.'}}}}, 
        'follow': {'You find sticks in sight! Is this the right direction, or more bait? Continue following or turn around?': {'continue': 'You find the trail ends, with a sign next to it pointing at yourself, you turn around and see your pig flying away while laughing and looking at you! You lost your pet.', 'turn around': {'You walk up and see your pig that just got off the ground and is flying away! You could chase it with your human kite, or give up and go back home to chill.': {'kite': 'It took a while, but you eventually caught up to it and went back home together happily ever after.', 'chill': 'You enjoyed some hobbies and went to bed.'}}}}}},

    'roof': {'You got onto the roof and found him near a mountain and it was flying towards a skydiving platform in the sky! Do you kite towards it, it would be slow but safe, or use your human catapault aimed towards the pig, it would be faster, but more dangerous?': {
        'kite': {'You slowly, but safely, flew there, but it was already at the skydive platform at that point and now it\'s too high to do anything': {'wait': {'It\'s skydiving now! You look around frantically, and somehow found a landmat, but it isn\'t in the location of your pig\'s landing spot! Do you move it, or watch the amazing spectacle?': {'landmat': 'It landed safely on it\'s own, looks like you didn\'t need to do that.', 'watch': 'Well, it looks like it landed safely on it\'s own, looks like you didn\'t need to do that.'}}}}, 
        'catapault': {'Luckily you landed well, but didn\'t aim well enough and barely missed grabbing the pig. But it\'s not too late to use this opportunity where you two are close. You could use a nearby trampoline, or sprint and jump for it.': {'trampoline': {'You missed and fell, but as you look around from the ground, you find a net under the trampoline. Do you try the trampoline again, or throw the net?': {'again': 'You didn\'t miss this time, congrats on getting his leg! Your pig laughed and you went home together.', 'net': {'Your net missed, and now it\'s too high to try the trampoline again, your only option is to wait.': {'wait': 'It skydived slowly into  your arms, guess it caught itself. You two went back home.'}}}}, 'jump': 'You barely got it\'s leg, but got him nonetheless. Congrats.'}}}}
    }
}


def play(story: Storyline) -> Union[str, Literal["The Adventure"]]:
    """plays adventure game"""

    # infinite loop while player is playing adventure
    try:
        while True:
            # gathers the keys of the next dictionary (the moves) by looking forward
            possible_moves = story[list(story)[0]].keys()

            # the current dictionary setting (the starting phrase) 
            # by selecting key (will be automaticlly in position by selecting last user move)
            phrase = list(story.keys())[0]
            
            print('\n')
            for char in f"{phrase} | {'/'.join(possible_moves)}: ":
                print(char, end='')
                time.sleep(0.01)
            user_move = input().lower()

            # N
            if user_move not in possible_moves: 
                return f"That move, \"{user_move}\" is invalid."

            # move the current setting 1 move forward (deleting previous storyline), to enable a  
            # recursive-like loop till the storyline ends, when it ends, it will set the current
            # setting to the last nested dictionary's value, which is the end of adventure message 
            story = story[phrase][user_move]
            
    # exceptions occurs when the adventure is over
    except TypeError:
        return f"\n{story}"

        
        
print(play(story))
