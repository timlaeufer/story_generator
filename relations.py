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


#Diplomacy:
class DiploRel(Relation):
    def __init__(self, name1, name2, is_mutual = False):
        super.__init__(name1, name2)
        
    @property
    def is_mutual(self):
        return self.__is_mutual
    
    @is_mutual.setter
    def is_mutual(self, is_mutual):
        """Sets is_mutual. Can be string, int or bool"""
        if(isinstance(is_mutual, bool)):
            self.__is_mutual = is_mutual
            
        elif(isinstance(is_mutual, int)):
            if(is_mutual > 0):
                self.__is_mutual = True
            else:
                self.__is_mutual = False
                
        elif(isinstance(is_mutual, str)):
            if("yes" in is_mutual.lower()):
                self.__is_mutual = True
            else:
                self.__is_mutual = False
    @is_mutual.getter
    def is_mutual(self):
        return self.__is_mutual
    
    def __repr__(self):
        if(self.is_mutual):
            s = self.name1 + " has a mutual diplomatic relation with "
            s+= self.name2 + "."
        else:
            s = self.name1 + " has a non-mutual diplomatic relation with "
            s +=self.name2 + "."
        return s
    
class EnemRel(DiploRel):
    def __init__(self, name1, name2, is_mutual = False):
        super.__init__(name1, name2)
        
    def __repr__(self):
        return self.name1 + " considers " + self.name2 + " an enemy."
    
class FriendRel(DiploRel):
    def __init__(self, name1, name2, isMutual = False):
        super.__init__(name1, name2)
        self.isMutual = isMutual
        
    def __repr__(self):
        return self.name1 + " considers " + self.name2 + " a friend."
    
#Family:
class FamRel(Relation):
    def __init__(self, name1, name2):
        super.__init__(name1, name2, is_mutual = True)
        
    def __repr__(self):
        return self.name1 + " is a part of the family of " + self.name2

    

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
