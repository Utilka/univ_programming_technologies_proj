import unittest
import sys
from sortedListNoDubl import SortedListNoDubl


class TestArr(unittest.TestCase):

    def common_result_eq_test(self, cases, results):
        for a, r in zip(cases, results):
            with self.subTest(case=a):
                b = SortedListNoDubl(list(a))
                self.assertTrue(all(x == y for x, y in zip(b.get_list(), r)),
                                msg="Elements changed. a = " + str(a) + ", b = " + str(b))


    def test_sorting(self):
        self.cases = ([], [0], [1], list(range(0, 10)), list(range(10, 0, -1)),
                      [], [-0], [-1], list(range(-10, 0)), list(range(0, -10, -1)))

        self.results = ([], [0], [1], list(range(0, 10)), list(range(1, 11)),
                        [], [0], [-1], list(range(-10, 0)), list(range(-9, 1)))

        self.common_result_eq_test(self.cases, self.results)

    def test_reverse_sorting(self):
        self.cases = ([], [0], [1], list(range(0, 10)), list(range(10, 0, -1)),
                      [], [-0], [-1], list(range(-10, 0)), list(range(0, -10, -1)))

        self.results = ([], [0], [1], list(range(9, -1, -1)), list(range(10, 0, -1)),
                        [], [0], [-1], list(range(-1, -11, -1)), list(range(-1, -11, -1)))

        self.common_result_eq_test(self.cases, self.results)

    def test_duplicates_removal(self):
        self.cases = ([1, 1], [1, 1, 2, 2, 3, 3, 4, 4],
                      [-1, -1], [-1, -1, -2, -2, -3, -3, -4, -4],
                      list(range(0, 10)) + list(range(0, 10)))

        self.results = ([1], [1, 2, 3, 4],
                        [-1], [-4, -3, -2, -1],
                        list(range(0, 10)))

        self.common_result_eq_test(self.cases, self.results)

    def test_universality(self):
        self.cases = ([4, 2, 8], list('abczzefgaa'), [True, False],
                      [float(i) / 10 for i in range(10, 0, -1)],
                      [[6, 7], [3, 4, 5], [3, 4], [2], [1, 2]])

        self.results = ([2, 4, 8], list('abcefgz'), [False, True],
                        [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
                        [[1, 2], [2], [3, 4], [3, 4, 5], [6, 7]])

        self.common_result_eq_test(self.cases, self.results)

    def test_merge(self):
        self.cases = ((list(range(0, 5)), list(range(5, 10))),
                      (list(range(0, 5)), list(range(3, 8))),
                      (list(range(0, 5)), list(range(0, 5))),
                      (list(range(0, 5)), list(range(-5, 0))),
                      (list(range(0, 5)), list(range(-3, 2))))

        self.results = (list(range(0, 10)),
                        list(range(0, 8)),
                        list(range(0, 5)),
                        list(range(-5, 5)),
                        list(range(-3, 5)))

        self.common_result_eq_test(self.cases, self.results)

    def test_exceptions(self):
        self.cases = (([1,2],["a","b"]),
                      ([1,2],[1,2]))

        for a in self.cases:
            with self.subTest(case=a):
                b = SortedListNoDubl(list(a[0]))
                self.assertRaises(ValueError, b.add, a[1])


def sort_test_suite():
    suite = unittest.TestSuite()

    suite.addTest(TestArr('test_sorting'))
    suite.addTest(TestArr('test_reverse_sorting'))
    suite.addTest(TestArr('test_duplicates_removal'))
    suite.addTest(TestArr('test_universality'))
    suite.addTest(TestArr('test_merge'))
    suite.addTest(TestArr('test_exceptions'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    test_suite = sort_test_suite()
    runner.run(test_suite)
