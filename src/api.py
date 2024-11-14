import requests
from abc import ABC, abstractmethod


class JobAPI(ABC):
    """Абстрактный класс для работы с API вакансий."""

    @abstractmethod
    def get_vacancies(self, query):
        """Метод для получения списка вакансий по поисковому запросу."""
        pass


class HeadHunterAPI(JobAPI):
    """Класс для работы с API HeadHunter (hh.ru)."""

    BASE_URL = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, query):
        """Получает вакансии с hh.ru по указанному запросу."""
        params = {
            'text': query,  # Ключевое слово для поиска
            'area': 113,  # Код региона (113 — Россия)
            'per_page': 20  # Количество вакансий на одной странице
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Проверка на успешный статус ответа
            vacancies = response.json().get('items', [])
            return vacancies
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API hh.ru: {e}")
            return []
