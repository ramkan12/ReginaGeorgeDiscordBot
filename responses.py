from random import choice, randint

def getresponse(user_input: str) -> str:
    lowered: str = user_input.lower() 

    if lowered == '':
        return 'So, you think you’re really pretty? Silence says otherwise.'
    
    elif 'hello' in lowered or 'hi' in lowered:
        return choice(['Ugh, hi...', 'Oh, it’s you. Hi.', 'Why are you talking to me?'])
    
    elif 'how are you' in lowered:
        return 'I’m a queen, so obviously I’m flawless.'
    
    elif 'bye' in lowered:
        return choice(['Bye, whatever.', 'Finally, I thought you’d never leave.', 'I don’t care for your presence, skeez'])
    
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}. But let’s be real, you’re not winning at life.'
    
    elif 'who are you' in lowered:
        return 'I’m Regina George.'
    
    elif 'clothe' or 'shirt' in lowered:
        return 'Wow, you’re like a martian. Get in, loser, we’re going shopping.'
    
    elif 'skirt' in lowered:
        return 'That is the ugliest f-ing skirt I’ve ever seen.'
    
    elif 'why are you mean' in lowered:
        return 'I’m not mean; I’m just honest. And honesty is *so* overrated.'
    
    elif 'favorite color' in lowered:
        return 'Pink, obviously. On Wednesdays, it’s practically mandatory.'
    
    elif 'butter' or 'carb' in lowered:
        return 'Is butter a carb?'
    
    elif 'food' in lowered:
        return choice(['All Iv’e been having are these Kälteen Bars. It burns carbs. It just burns up all your carbs.', 'Whatever, I’m getting cheese fries.'])
    
    elif 'you are mean' in lowered or 'you are rude' in lowered:
        return 'I know, right? I’m like, the Queen Bee.'
    
    elif 'friends' in lowered:
        return 'I don’t make friends. I make *followers*.'
    
    elif 'mom' or 'mother' in lowered:
        return 'Ugh, my mom thinks she’s not a regular mom, she’s not a cool mom either.'
    
    elif 'you\'re pretty' in lowered:
        return 'I know, right? Everyone wants to be me.'
    
    elif 'love you' in lowered:
        return 'Of course you love me. Who wouldn’t?'
    
    elif 'can we be friends' in lowered:
        return 'You want to be my friend? That’s cute. But only if you wear pink on Wednesdays.'
    
    elif 'gossip' in lowered:
        return 'So, what’s the 411? Who’s being totally fake today?'
    
    elif 'fetch' in lowered:
        return 'Stop trying to make fetch happen. It’s not going to happen.'
    
    elif 'burn book' in lowered:
        return 'Did you say Burn Book? Don’t worry, your secrets are totally safe with me... or are they?'
    
    else:
        return choice([
            'Is that supposed to impress me?', 
            'Do you even go here?', 
            'Um, what?', 
            'You might want to rephrase that. Or don’t. I don’t care.', 
            'I can’t help it if you’re obsessed with me.'
        ])
