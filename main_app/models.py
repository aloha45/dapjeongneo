from django.db import models, migrations
from datetime import date

# Create your models here.


class Dream:
    def __init__(self, title, mood, description):
        self.title = title
        self.mood = mood
        self.description = description
        
dreams = [
    Dream('a scary dream', 'freaky', 'big scary werewolf'),
    Dream('a nice dream', 'happy and warm', 'field in summer at dusk, barefeet in grass'),
    Dream('kind of sexy', 'schwing', 'like a nerdy professor in hot pajamas')
]
