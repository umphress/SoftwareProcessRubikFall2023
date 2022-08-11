from unittest import TestCase
import rubik.create as create 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnCubeWithColors(self):
        """Unit test:  should return 
            1) status code of OK and
            2) cube consists of 54 elements and
            3) cube with nine of each color"""
            
        colors = '123456'
        
        parm = {'op':'create',
                'colors': colors}
        result = create._create(parm)
        
        self.assertIn('status',result)
        self.assertEqual(result['status'], 'ok')
        
        self.assertIn('cube', result)
        self.assertEqual(len(result['cube']), 54)
        
        for color in colors:
            self.assertEqual(result['cube'].count(color), 9)

