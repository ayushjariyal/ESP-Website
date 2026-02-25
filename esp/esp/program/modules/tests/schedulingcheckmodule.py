from django.test import SimpleTestCase
from esp.program.modules.handlers.schedulingcheckmodule import RawSCFormatter


class RawSCFormatterTest(SimpleTestCase):

    def test_format_table(self):
        formatter = RawSCFormatter()
        data = [["A", "B"]]
        self.assertEqual(formatter.format_table(data), data)

    def test_format_list(self):
        formatter = RawSCFormatter()
        data = [{"a": 1}]
        self.assertEqual(formatter.format_list(data), data)