import unittest
from test_doctors import Doctors

class TestDoctors(unittest.Testcase):
    def test_email(self):
        doct_1 = Doctors('Faruq', 'Hasan', 500000)
        doct_2 = Doctors('Hasib', 'Jaman', 600000)

        self.assertEqual(doct_1.email, 'Faruq.Hasan@gmail.com')
        self.assertEqual(doct_1.email, 'Hasib.Jaman@gmail.com')

    def test_fullname(self):
        doct_1 = Doctors('Faruq', 'Hasan', 500000)
        doct_2 = Doctors('Hasib', 'Jaman', 600000)

        self.assertEqual(doct_1.fullname, 'Faruq Hasan')
        self.assertEqual(doct_2.fullname, 'Hasib Jaman')
# testing
        doct_1 = 'John'
        doct_2 = 'Joni'
        
        self.assertEqual(doct_1.fullname, 'Faruq Hasan')
        self.assertEqual(doct_2.fullname, 'Hasib Jaman')
    def test_apply_raise(self):

        doct_1 = Doctors('Faruq', 'Hasan', 500000)
        doct_2 = Doctors('Hasib', 'Jaman', 600000)
# testing
        doct_1.apply_raise()
        doct_2.apply_raise()

        self.assertEqual(doct_1, 5289)
        self.assertEqual(doct_2, 6289)
if __name__ == '__main__':
    unittest.main()
