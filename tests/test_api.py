import unittest
from unittest.mock import patch
import requests

from src.api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.api = HeadHunterAPI()

    @patch('src.api.requests.get')
    def test_get_vacancies_success(self, mock_get):
        """Тест успешного запроса к API hh.ru с правильными данными."""
        mock_response = {
            'items': [
                {
                    'name': 'Python Developer',
                    'url': 'https://hh.ru/vacancy/123456',
                    'salary': {'from': 100000, 'to': 150000},
                    'snippet': {'requirement': 'Опыт работы с Python'}
                },
                {
                    'name': 'Data Scientist',
                    'url': 'https://hh.ru/vacancy/654321',
                    'salary': {'from': 120000, 'to': 180000},
                    'snippet': {'requirement': 'Знание ML и Data Analysis'}
                }
            ]
        }

        # Настраиваем mock, чтобы вернуть mock_response с кодом 200
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Выполняем запрос
        vacancies = self.api.get_vacancies('Python')

        # Проверяем, что метод возвращает правильные данные
        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]['name'], 'Python Developer')
        self.assertEqual(vacancies[0]['url'], 'https://hh.ru/vacancy/123456')
        self.assertEqual(vacancies[1]['name'], 'Data Scientist')

    @patch('src.api.requests.get')
    def test_get_vacancies_empty_result(self, mock_get):
        """Тест запроса, который возвращает пустой список вакансий."""
        mock_response = {'items': []}

        # Настраиваем mock, чтобы вернуть пустой ответ с кодом 200
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        vacancies = self.api.get_vacancies('NonexistentJob')

        # Проверяем, что результат пустой
        self.assertEqual(vacancies, [])

    @patch('src.api.requests.get')
    def test_get_vacancies_request_exception(self, mock_get):
        """Тест обработки исключения при сбое подключения к API."""
        # Настраиваем mock для генерации исключения
        mock_get.side_effect = requests.RequestException("Ошибка сети")

        vacancies = self.api.get_vacancies('Python')

        # Проверяем, что в случае ошибки возвращается пустой список
        self.assertEqual(vacancies, [])

    @patch('src.api.requests.get')
    def test_get_vacancies_invalid_status_code(self, mock_get):
        """Тест обработки неверного статус-кода."""
        mock_get.return_value.status_code = 404

        vacancies = self.api.get_vacancies('Python')

        # Проверяем, что при статус-коде 404 возвращается пустой список
        self.assertEqual(vacancies, [])


if __name__ == '__main__':
    unittest.main()
