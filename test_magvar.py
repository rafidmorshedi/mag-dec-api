#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:02:58 2019

@author: rafid
"""

import unittest
from magvar import get_mag_var

class MagvarTestCase(unittest.TestCase):
    """Tests for magvar.py"""
    
    def test_magvar_1(self):
        """Test for lat=-24.09,lon=135,elev=0,year=2015,month=1,day=1"""
        mag_variation = get_mag_var(lat=-24.09,lon=135,year=2015,month=1,day=1)
        self.assertEqual(mag_variation,5.136)
    
    def test_magvar_2(self):
        """Another test"""
        mag_variation = get_mag_var(-33.805615,150.01938,2009,10,10,0.8)
        self.assertEqual(mag_variation,12.096)


unittest.main()