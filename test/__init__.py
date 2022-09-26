import os.path

from jsontestrunner import Runner

current_path = os.path.dirname(__file__)

if __name__ == '__main__':
    runner = Runner(current_path, verbosity=2)
    runner.run().save(current_path)