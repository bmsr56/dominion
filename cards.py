class Card:
    """ Base class for a Dominion Card.
    """
    cardType = None
    abilities = {
        'plusActions': None,
        'plusDraws': None,
        'plusBuys': None, 
        'plusMoney': None
    }

    def __init__(self):
        self.title = title 
        self.parentSet = parentSet
    
    def set_plusActions(self, val: int) -> None:
        self.abilities['plusActions'] = val
        return

    def set_plusDraws(self, val: int) -> None:
        self.abilities['plusDraws'] = val
        return

    def set_plusBuys(self, val: int) -> None:
        self.abilities['plusBuys'] = val
        return

    def set_plusMoney(self, val: int) -> None:
        self.abilities['plusMoney'] = val
        return
    
    def print(self) -> None:
        """ Print the card in a human-readable format
        """
        pass


class ActionCard(Card):
    
    def __init__(self):
        super().__init__()


class TreasureCard(Card):

    def __init__(self):
        super().__init__()


class AttackCard(Card):

    def __init__(self):
        super().__init__()


class ReactionCard(Card):

    def __init__(self):
        super().__init__()


class CurseCard(Card):

    def __init__(self):
        super().__init__()
