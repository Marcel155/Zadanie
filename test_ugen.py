import unittest
import ugen

output1 = open('output_file.txt', 'r', encoding='utf-8')
input1 = open('input_file1.txt', 'r', encoding='utf-8')


class TestUgen(unittest.TestCase):

    def test_digits(self):              # id ma 4 čislice
        condition = True
        for i in output1.readlines():
            out_split = i.split(':')
            if len(out_split[0]) != 4:
                condition = False
        self.assertTrue(condition)

    def test_username(self):            # username ma viac ako 2 znaky
        condition = True
        for i in output1.readlines():
            out_split = i.split(':')
            if len(out_split[1]) < 3:
                condition = False
        self.assertTrue(condition)

    def test_first(self):               # meno ma viac ako 2 znaky
        condition = True
        for i in output1.readlines():
            out_split = i.split(':')
            if len(out_split[2]) < 3:
                condition = False
        self.assertTrue(condition)

    def test_last(self):                # priezvisko ma viac ako 2 znaky
        condition = True
        for i in output1.readlines():
            out_split = i.split(':')
            if len(out_split[4]) < 3:
                condition = False
        self.assertTrue(condition)


if __name__ == '__main__':
    unittest.main()

