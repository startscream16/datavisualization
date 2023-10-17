import unittest
from country_codes import get_country_code

class TestCountryCode(unittest.TestCase):
    """Тесты для 'get_country_code'"""
    
    def test_country_code(self):
        """Функция возвращает код страны переданной в аргументе?"""
        country_code = get_country_code('Ukraine')
        self.assertEqual(country_code, 'ua')
        
        country_code = get_country_code('Arab')
        self.assertEqual(country_code, None)
        
        country_code = get_country_code('Iran, Islamic Rep.')
        self.assertEqual(country_code, 'ir')
        
        country_code = get_country_code('United Kingdom')
        self.assertEqual(country_code, 'gb')
        
        country_code = get_country_code('Portugal')
        self.assertEqual(country_code, 'pt')
        
unittest.main()
