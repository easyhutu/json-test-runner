import time
import unittest


class RunnerTestCase(unittest.TestCase):

    def test_success(self):
        print('success')
        self.assertTrue(1)

    def test_failed(self):
        time.sleep(1)
        self.assertTrue(0)