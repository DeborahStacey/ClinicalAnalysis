#!/usr/bin/env python
# Primary Owner: Russell Dunk

# #test timing and performance

import unittest

host = "19"


#Testing imports
import os


class TestClinacalAnalysisEngine(unittest.TestCase):
    def test_ping(self):
        self.assertEqual(os.system("ping -c 1 " + host), 0)

if __name__ == '__main__':
    unittest.main()

#ping the server
#tests db login credentials

#test db for required tables

#get any data from fields


#simple lookup
#Cats with desease diabetes

#complex lookup with ands and ors


#correlations


#complex correlations



#Predictions

#Complex Predictions

