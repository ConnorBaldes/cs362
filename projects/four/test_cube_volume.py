import unittest
import cube_volume

class TestCubeVolume(unittest.TestCase):

    def test_volume(self):
        self.assertEqual(cube_volume.cube_volume(3),27)
        self.assertEqual(cube_volume.cube_volume(0),0)
        self.assertEqual(cube_volume.cube_volume(-3),-27)
        self.assertEqual(cube_volume.cube_volume("7"),343)
        self.assertEqual(cube_volume.cube_volume("3w"),None)
        #fail case
        self.assertEqual(cube_volume.cube_volume(4),16)
        



if __name__ == '__main__':

    unittest.main(verbosity=2)
