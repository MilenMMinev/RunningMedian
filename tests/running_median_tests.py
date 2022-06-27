import random
import statistics
import unittest

from running_median import RunningMedian


class RunningMedianTests(unittest.TestCase):
    def test_add_element(self):
        sample = RunningMedian()
        sample.add(3.14)
        self.assertIn(3.14, sample.items())

    def test_get_median_even_sample_size(self):
        vals = [random.uniform(-100, 100) for i in range(1000)]
        sample = RunningMedian()
        for v in vals:
            sample.add(v)
        self.assertEqual(sample.median(), statistics.median(vals))

    def test_get_median_odd_sample_size(self):
        vals = [random.uniform(-100, 100) for i in range(1001)]
        sample = RunningMedian()
        for v in vals:
            sample.add(v)
        self.assertEqual(sample.median(), statistics.median(vals))


if __name__ == '__main__':
    unittest.main()
