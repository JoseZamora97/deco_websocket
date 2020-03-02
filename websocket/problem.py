import numpy as np


class Problem:
    @staticmethod
    def generate(n: int = 10) -> tuple:
        return list(np.random.rand(n)), list(np.random.rand(n))

    @staticmethod
    def operate(work):

        a = work['row']
        b = work['col']

        out = 0.0
        for x, y in zip(a, b):
            out += x*y

        work['result'] = out


class ThreadLauncher:
    """
    Class that handles w<ith threads.
    """
    @staticmethod
    def launch_threads_and_wait(threads):
        """
        Method that launch threads and wait until they end.
        :return: none.
        """
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()