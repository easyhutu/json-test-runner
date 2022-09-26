import os.path
import unittest


class RunnerCase(unittest.TestCase):
    def setUp(self) -> None:
        super(RunnerCase, self).setUp()
        self.save_path = os.path.join(os.path.dirname(__file__), 'report.json')

    def test_pass(self):
        """
        this is pass
        :return:
        """
        print('1 == 1')
        self.assertEqual(1, 1)

    def test_failed(self):
        print('1 != 2')
        self.assertEqual(1, 2)

    def test_error(self):
        print('raise with error')
        raise Exception('this is error')
