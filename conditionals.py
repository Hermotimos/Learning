import unittest


def process_input(val):
    if val == 'ok':
        return 'success'
    elif val != 'Yes' or val != '1':  # tricky, because this is always true
        return 'failure'
    else:
        return 'error'

# 'ok' --> 'success'
# any other values --> 'failure' (even if val = 'Yes', it still != '1')



class MyTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(process_input('ok'), 'success')

    def test_yes(self):
        self.assertEqual(process_input('Yes'), 'error')

    def test_1(self):
        self.assertEqual(process_input('1'), 'error')



if __name__ == '__main__':
    unittest.main()
