import unittest
from unittest.mock import patch
import app as acc_test


class UnitTestApp(unittest.TestCase):

    @patch('builtins.input')
    def test_add_new_doc(self, inputs):
        inputs.side_effect = ["998", "id", "Ryan Gosling", "3"]
        acc_test.add_new_doc()
        result = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                  {"type": "id", "number": "998", "name": "Ryan Gosling"}]
        self.assertListEqual(acc_test.show_all_docs_info(), result)

    @patch('builtins.input')
    def test_delete_doc(self, inputs):
        inputs.side_effect = "998"
        acc_test.delete_doc()
        self.assertFalse(acc_test.check_document_existance(inputs.side_effect))

    @patch('builtins.input', lambda *args: "11-2")
    def test_get_doc_owner_name(self):
        self.assertEqual(acc_test.get_doc_owner_name(), "Геннадий Покемонов")

    @patch('builtins.input', lambda *args: "11-2")
    def test_get_doc_shelf(self):
        self.assertEqual(acc_test.get_doc_shelf(), "1")


if __name__ == '__main__':
    unittest.main()