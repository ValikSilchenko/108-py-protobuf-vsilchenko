from unittest import TestLoader
from unittest.runner import TextTestRunner

import TestHelpers
import TestParser

if __name__ == "__main__":
    parser_test = TestLoader().loadTestsFromModule(TestParser)
    helpers_test = TestLoader().loadTestsFromModule(TestHelpers)
    TextTestRunner().run(parser_test)
    TextTestRunner().run(helpers_test)
