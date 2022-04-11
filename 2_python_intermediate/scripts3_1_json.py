import random
import json

count = 10
words = ['Tacos', 'Casserole', 'Chicken Rice bowls', 'BBQ pork chops', 'beef soup', 'chocolate Yogurt']

for id in range(count):
    amount = random.uniform(10.0, 45)
    content = {
        'topic': random.choice(words),
        'value': amount
    }

print(content)