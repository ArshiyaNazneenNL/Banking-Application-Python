import random

def generate_card_number():
    return "4000" + ''.join([str(random.randint(0, 9)) for _ in range(12)])
