# -*- coding: utf-8 -*-

from unittest import TestCase

import vantage as v

daily_adjusted_columns: [
                         '1. open',
                         '2. high',
                         '3. low',
                         '4. close',
                         '5. adjusted close',
                         '6. volume',
                         '7. dividend amount',
                         '8. split coefficient'
 ]


class TestToDf(TestCase):
    def test_time_series_adjusted_daily(self):
        df = v.to_df('vantage/tests/time_series_adjusted_daily.json')
        self.assertTrue(df.shape == (3, 8))
        self.assertTrue(list(df.columns) == daily_adjusted_columns)
