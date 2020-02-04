#!/usr/bin/env python
# coding: utf-8

# In[5]:


import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testNotATriangle(self):
        self.assertNotEqual(classifyTriangle(1,2,'1'),'Isoceles','1,2,1 should not be a triangle')
        self.assertNotEqual(classifyTriangle(201, 201, 202),'Isoceles','201, 201, 202 should not be a triangle')
        self.assertNotEqual(classifyTriangle(-1, -2, -2),'Isoceles','-1, -2, -2 should not be a triangle')
        
    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,1 should be isoceles')
        
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity = 2)


# In[ ]:




