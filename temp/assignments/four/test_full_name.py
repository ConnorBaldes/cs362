import unittest
import full_name

class TestListAverage(unittest.TestCase):

    def test_name(self):
 
        self.assertEqual(full_name.get_full_name("Connor", "Baldes"),"Connor Baldes")
        self.assertEqual(full_name.get_full_name(2, "Baldes"),"2 Baldes")
        self.assertEqual(full_name.get_full_name("", "Baldes")," Baldes")
        #fail case
        self.assertEqual(full_name.get_full_name("Connor", "Baldes"),"Steve Madden")
        




if __name__ == '__main__':

    unittest.main(verbosity=2)