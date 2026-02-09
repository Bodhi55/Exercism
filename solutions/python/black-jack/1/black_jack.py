def value_of_card(card):
    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 1
    return int(card)

def higher_card(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    
    if v1 > v2:
        return card_one
    if v2 > v1:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    # L'As vaut 11 si le total actuel + 11 ne dépasse pas 21
    # Mais attention : la consigne précise que si un As est déjà en main, il vaut 11
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    
    # Correction de la valeur si c'est un As (car value_of_card renvoie 1)
    if card_one == 'A': v1 = 11
    if card_two == 'A': v2 = 11
        
    return 11 if v1 + v2 + 11 <= 21 else 1

def is_blackjack(card_one, card_two):
    # Un blackjack = un As (11) et une figure ou un 10 (10)
    v1 = 11 if card_one == 'A' else value_of_card(card_one)
    v2 = 11 if card_two == 'A' else value_of_card(card_two)
    return v1 + v2 == 21

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)