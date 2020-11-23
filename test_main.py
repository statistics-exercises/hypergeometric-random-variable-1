import unittest
import scipy.stats
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) : 
        for N in range(5,9) : 
            for R in range(1,N) : 
                mean = 0 
                for k in range(100) : mean = mean + choice(R,N) 
                prob = R/N
                bar = np.sqrt(prob*(1-prob)/100)*scipy.stats.norm.ppf( (0.99 + 1) / 2 )
                self.assertTrue( np.fabs( mean/100 - prob )<bar, "Your function for choosing the ball colour is not working correctly" )
