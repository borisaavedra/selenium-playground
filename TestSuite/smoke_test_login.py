from unittest import TestSuite, TestLoader
from pyunitreport import HTMLTestRunner
from create_new_user import CreateNewUserTest
from log_in import LogInTest

newuser_test = TestLoader().loadTestsFromTestCase(CreateNewUserTest)
login_test = TestLoader().loadTestsFromTestCase(LogInTest)

smoke_test = TestSuite([newuser_test, login_test])

parameters = {
    "output": "reportes",
    "failfast": True
}

runner = HTMLTestRunner(**parameters)
runner.run(smoke_test)
