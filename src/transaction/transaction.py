from abc import ABC, abstractmethod 

class transaction: 
    """The transaction abstract class defines methods that may be
    implemented by an Account class. 
    """    
    @abstractmethod
    def getBalance(self):
        """Returns the current balance of this account
        """        
        pass 

    @abstractmethod
    def isEmpyty(self):
        """Checks if the balance for this account is zero.
        """        
        pass 
    
    @abstractmethod
    def credit(self,amount:int):
        """Increases the balance of this account by the specified amount.

        Args:
            amount (int): the amount to increase the balance by
        """        
        pass 

    @abstractmethod
    def debit(self,amount:int):
        """Decreases the balance of this account by the specified amount. 

        Args:
            amount (int): the amount to decrease the balance by 
        """        
        pass 