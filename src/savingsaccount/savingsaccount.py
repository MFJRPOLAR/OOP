from account.account import * 


class savingsaccount(account):
    """The SavingsAccount class has methods to manage the balance 
    and interest rate of a savings account

    Args:
        account (account): class that includes methods to manage the balance
    of a bank account.
    """    
    def __init__(self, balance,interestRate):
        """Constructs a savings account with a specified balance and interest rate.

        :ivar __balance: balance of this account 
        :ivae __interestRate: interest rate of this savingsaccount

        Args:
            balance (float): balance
            interestRate (float): interest rate
        """        
        super().__init__(balance)
        self.__interestRate = interestRate

    def setInterestRate(self, interestRate: float):
        """Sets the interest rate for the calling savings account.

        Args:
            interestRate (float): interest rate
        """        
        self.__interestRate = interestRate

    def getInterestRate(self): 
        """Returns the interest rate for the calling savings account.

        Returns:
            float: interest rate
        """        
        return self.__interestRate 

    def getInterest(self): 
        """Return the interest for the calling savings account.

        Returns:
            float: interest
        """        
        return self.getBalance() * self.__interestRate  

    def credit(self, amount: float):
        """Increases the balance of the calling savings account by the specified 
        amount times the interest rate of this savings account.

        Args:
            amount (float): the amount to increase the balance by
        """        
        super().credit(amount * self.__interestRate) 

    def __str__(self):
        """Returns string representation of the calling savings account

        Returns:
            str: string representation of the calling savings account. 
        """        
        return f"savings account balance={self.getBalance()} interestRate= {self.__interestRate}"

    def __eq__(self, other):
        """Tests is the calling savngs account is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling savings account is equal to the specified 
            object, else False. 
        """        
        # check if other is not None 
        if other is not None:
            # check if other is an account type
            if isinstance(other,savingsaccount):
                # check if other's balance is equal to the balance 
                # of the calling object 
                if other.getBalance() == self.getBalance() and other.__interestRate == self.__interestRate:
                    return True 
                
        return False
