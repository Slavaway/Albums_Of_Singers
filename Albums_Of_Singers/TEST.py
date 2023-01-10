import unittest
import Model

class TestModel(unittest.TestCase):
    

    def test_updateAlbums(self):
        self._model = Model.Model()
        self._model.updateAlbums(2, "Bad")
        test = self._model.getAlbumsSQL()
        self.assertIn(['Bad', 2], test)

    def test_updateAlbums(self):
        self._model = Model.Model()
        self._model.updateAlbums(4, "Justice")
        test = self._model.getAlbumsSQL()
        self.assertIn(['Justice', 4], test)




if __name__ == '__main__':
    unittest.main()