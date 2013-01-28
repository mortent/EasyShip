import unittest
import RateParser as RateParser
import Utils as Utils
import EvenPageRateParser as EvenPageRateParser

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
        with self.assertRaises(Utils.ParseError):
            RateParser.get_page_number("NEW_PAGE")

    def test_should_detect_line_with_only_newline(self):
        self.assertTrue(Utils.is_only_newline("\n"))

    def test_should_not_regard_empty_string_as_newline(self):
        self.assertFalse(Utils.is_only_newline(""))

    def test_should_not_regard_line_with_other_content_as_newline(self):
        self.assertFalse(Utils.is_only_newline("TEST\n"))

    def test_should_strip_non_digit_characters_from_string(self):
        self.assertEquals("12310", Utils.strip_non_digit_characters("!123.10$"))

    def test_should_identify_weight_columns_starting_with_Zones(self):
        self.assertTrue(EvenPageRateParser.is_weight_column("Zones"))

    def test_should_reject_columns_with_extra_text_in_addition_to_Zones(self):
        self.assertFalse(EvenPageRateParser.is_weight_column("Zones 123"))

    def test_should_identify_letter_weights(self):
        self.assertTrue(EvenPageRateParser.is_letter_weight("Letter*"))

if __name__ == '__main__':
    unittest.main()
