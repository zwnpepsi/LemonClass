import unittest

from class_1010课 import TestMath

suite=unittest.TestSuite()
suite.addTest(TestMath("test_sum"))
suite.addTest(TestMath("test_sub"))
runner=unittest.TextTestRunner()
runner.run(suite)


