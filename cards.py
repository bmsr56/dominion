class Card:
    """ Base class for a Dominion Card.
    """
    category = []
    abilities = {
        'plusActions': None,
        'plusDraws': None,
        'plusBuys': None, 
        'plusMoney': None,
        'curse': None
    }

    def __init__(self):
        pass
    
    def print(self) -> None:
        """ Print the card in a human-readable format
        """
        pass


class ActionCard(Card):

    cardTypes = 'action'

    def __init__(self):
        super().__init__()

    

class TreasureCard(Card):

    cardType = 'treasure'

    def __init__(self):
        super().__init__()


class AttackCard(ActionCard):

    def __init__(self):
        super().__init__()


class ReactionCard(Card):

    def __init__(self):
        super().__init__()


class CurseCard(Card):

    def __init__(self):
        super().__init__()
