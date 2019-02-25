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
    FRIEND_DESC = ' is someone who likes and is on the side of '
    
    ALLY = 'ally'
    ALLY_DESC = ' is an ally of '
    
    OPPONENT = 'opponent'
    OPPONENT_DESC = ' is against a certain'
    OPPONENT_DESC += ' interest in one specific field of '

class Feelings:
    #Love
    LOVE = 'love'
    LOVE_DESC = ' loves '
    
    CRUSH = 'crush'
    CRUSH_DESC = ' has a crush on '
    
    LOW_CRUSH = 'low_crush'
    LOW_CRUSH_DESC = ' has a small crush on '
class Family:
    #Family
    FATHER = 'father'
    FATHER_DESC = ' is the biological father of '
    
    MOTHER = 'mother'
    MOTHER_DESC = ' is the biological mother of '
    
    ADOPTIVE_FATHER = 'adoptive_father'
    ADOPTIVE_MOTHER = 'adoptive_mother'
    
    
    
    #Convenience bindings:
    ADOP_FATH = ADOPTIVE_FATHER
    ADOP_MOTH = ADOPTIVE_MOTHER
