# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:50:40 2019

@author: Tim Laeufer

A class to be used for convenient use of constants.

For convenience:
    <name_1> + Diplomacy.ENEMY_DISC + <name_2>
    will produce (as an example):
        "Arthur is against the interests and wants to hurt Jonas"
"""


class Diplomacy:
    ENEMY = 'enemy'
    ENEMY_DESC = ' is against the interests'
    ENEMY_DESC +='and wants to hurt '
    def get_enemy_desc(self, name1, name2):
        return name1 + self.ENEMY_DESC + name2
    
    FRIEND = 'friend'
    FRIEND_DESC = ' is someone who likes you and is on the side of '
    def get_friend_desc(self, name1, name2):
        return name1 + self.FRIEND_DESC + name2
    
    ALLY = 'ally'
    ALLY_DESC = 'Ally is someone who will '
    ALLY_DESC += 'help you in trouble that u have a bond with.'
    def get_ally_desc(self, name1, name2):
        return name1 + self.ALLY_DESC + name2
    
    OPPONENT = 'opponent'
    OPPONENT_DESC = 'Opponent is someone that means no harm but has a different.'
    OPPONENT_DESC += ' interest in one specific field'
    def get_opponent_desc(self, name1, name2):
        return name1 + self.OPPONENT_DESC + name2

class Feelings:
    #Love
    LOVE = 'love'
    LOVE_DESC = 'Love is a deep feeling that makes you not see their flaws.'
    
    CRUSH = 'crush'
    
    LOW_CRUSH = 'low_crush'
class Family:
    #Family
    FATHER = 'father'
    FATHER_DESC 
    
    MOTHER = 'mother'
    ADOPTIVE_FATHER = 'adoptive_father'
    ADOPTIVE_MOTHER = 'adoptive_mother'
    
    
    
    #Convenience bindings:
    ADOP_FATH = ADOPTIVE_FATHER
    ADOP_MOTH = ADOPTIVE_MOTHER
