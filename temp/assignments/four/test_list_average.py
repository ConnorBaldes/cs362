import unittest
import list_average

class TestListAverage(unittest.TestCase):

    

    def test_average(self):
        list_one = [2,2,2,2]
        list_two = [1,2]
        list_three = [0,0,0,0,0]
        list_four = [0,0,0,2]
        list_five = [-1,1]
        list_six = []
        list_seven = [2, 'w', 4]
        self.assertEqual(list_average.list_average(list_one),2)
        self.assertEqual(list_average.list_average(list_two),1.5)
        self.assertEqual(list_average.list_average(list_three),0)
        self.assertEqual(list_average.list_average(list_four),.5)
        self.assertEqual(list_average.list_average(list_five),0)
        self.assertEqual(list_average.list_average(list_six),None)
        self.assertEqual(list_average.list_average(list_seven),None)
        #fail case
        self.assertEqual(list_average.list_average(list_one),0)

if __name__ == '__main__':

    unittest.main(verbosity=2)