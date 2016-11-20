#!/usr/bin/python env

import re

class Card(object):
    managed = False

    def __init__(self, num, suit = None):
        suits = '[Hh]earts?|[Ss]pades?|[Cc]lubs?|[Dd]iamonds?'
        face_cards = '[Jj]ack|[Qq]ueen|[Kk]ing|[Aa]ce|[Jj]oker'

        # raise exception if suit is not valid
        if suit is not None and not re.match(suits, suit):
            raise ValueError
        else:
            self.suit = suit

        # raise exception if num is not valid
        if isinstance(num, int) and num not in range(2, 11):
            raise ValueError
        elif isinstance(num, str) and not re.match(face_cards, num):
            raise ValueError
        else:
            self.number = num
