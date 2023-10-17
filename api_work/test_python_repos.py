import unittest
import python_repos as pr

class TestPythonRepos(unittest.TestCase):
    """Тесты для python_repos"""
    
    def setUp(self):
        self.r = pr.r
        self.repo_dicts = pr.repo_dicts
        self.response_dict = pr.response_dict
    
    def test_python_repos(self):
        """Значение status_code равно 200?"""
        self.assertEqual(self.r.status_code, 200)
    
    def test_len_repo_dicts(self):
        """Длина repo_dicts равна 30"""
        self.assertEqual(len(self.repo_dicts), 30)
    
    def test_element_in_repo(self):
        """
        Проверяет входит ли элемент 'items' и элемент 'total_count'
        в response_dict
        """
        self.assertIn('items', self.response_dict)
        self.assertIn('total_count', self.response_dict)
        
    def test_element_not_in_repo(self):
        """
        Проверяет, что элемент 'comments' действительно
        не входит в response_dict
        """
        self.assertNotIn('comments', self.response_dict)
        
unittest.main()
    
