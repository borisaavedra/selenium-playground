from unittest import TestSuite, TestLoader
from pyunitreport import HTMLTestRunner
from assertions import AssertionTest
from searchtest import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertions_test, search_test])

parameters = {
    "output": "smoke_report",
}

runner = HTMLTestRunner(**parameters)
runner.run(smoke_test)

