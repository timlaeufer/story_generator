# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:50:40 2019

@author: Tim Laeufer

"""
class Relation:
    def __init__(self, name1, name2):
        """A relation between <name1> and <name2>, directed from 1 to 2"""
        #Example: <name1> considers <name2> an ally.
        self.name1 = name1
        self.name2 = name2

    def __repr__(self):
        return self.name1 + " has a relation with " + self.name2

class DiploRel(Relation):
    def __init__(self, name1, name2):
        super.__init__(name1, name2)
    
    def __repr__(self):
        return self.name1 + " has a diplomatic relation with " + self.name2
    
class EnemRel(DiploRel):
    def __init__(self, name1, name2):
        super.__init__(name1, name2)
        
    def __repr__(self):
        return self.name1 + " considers " + self.name2 + " an enemy."
    
class FriendRel(DiploRel):
    def __init__(self, name1, name2):
        super.__init__(name1, name2)
        
    def __repr__(self):
        return self.name1 + " considers " + self.name2 + " a friend."
    


    

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
