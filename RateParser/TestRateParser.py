import unittest
import RateParser as RateParser

class TestRateParser(unittest.TestCase):

    def test_should_detect_new_page_with_page_number(self):
        self.assertTrue(RateParser.is_line_start_of_new_page("NEW_PAGE 21"))

    def testShouldDetectNewPageWithoutPageNumber(self):
        self.assertTrue(RateParser.is_line_start_of_new_page("NEW_PAGE\n"))

    def testShouldNotFindNewPage(self):
        self.assertFalse(RateParser.is_line_start_of_new_page("OLD_PAGE 38420"))

    def testShouldHandleNewLines(self):
        self.assertFalse(RateParser.is_line_start_of_new_page("\n"))

    def testShouldReturnPageNumber(self):
        self.assertEquals(21, RateParser.get_page_number("NEW_PAGE 21\n"))

    def test_should_fail_when_there_are_no_page_number(self):
        with self.assertRaises(RateParser.ParseError):
            RateParser.get_page_number("NEW_PAGE")

    def test_should_detect_line_with_only_newline(self):
        self.assertTrue(RateParser.is_only_newline("\n"))

    def test_should_not_regard_empty_string_as_newline(self):
        self.assertFalse(RateParser.is_only_newline(""))

    def test_should_not_regard_line_with_other_content_as_newline(self):
        self.assertFalse(RateParser.is_only_newline("TEST\n"))

if __name__ == '__main__':
    unittest.main()
