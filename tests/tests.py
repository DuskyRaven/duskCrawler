import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from duskcrawler.POC_crawler.py import process_page

class TestProcessPage(unittest.TestCase):

    @patch('requests.get')
    def test_process_page(self, mock_get):
        # Mock the response for the main page
        with open('main_page.html', 'r', errors="ignore") as file:
            main_page_content = file.read()
        mock_response_main = MagicMock()
        mock_response_main.text = main_page_content
        mock_get.return_value = mock_response_main

        # Mock the response for the article page
        with open('article_page.html', 'r') as file:
            article_page_content = file.read()
        mock_response_article = MagicMock()
        mock_response_article.text = article_page_content
        mock_get.side_effect = [mock_response_main, mock_response_article]

        # Call the function to test
        process_page('https://www.astrology.com/horoscope/daily.html')

        # Assert the behavior based on the mock
        mock_get.assert_called_with('https://www.astrology.com/horoscope/daily.html')
        mock_get.assert_called_with('<article_page_url>')


if __name__ == '__main__':
    unittest.main()