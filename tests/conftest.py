import pytest

@pytest.fixture
def test_dict_hh():
    test_dict = {'items': [
        {
            'id': '81264801',
            'premium': False,
            'name': 'Административный менеджер',
            'department': None,
            'has_test': False,
            'response_letter_required': False,
            'area': {
                'id': '160',
                'name': 'Алматы',
                'url': 'https://api.hh.ru/areas/160'
            },
            'salary': {
                'from': 300000,
                'to': None,
                'currency': 'KZT',
                'gross': True
            },
            'type': {
                'id': 'open',
                'name': 'Открытая'
            },
            'address': None,
            'response_url': None,
            'sort_point_distance': None,
            'published_at': '2023-05-29T19:21:05+0300',
            'created_at': '2023-05-29T19:21:05+0300',
            'archived': False,
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=81264801',
            'insider_interview': None,
            'url': 'https://api.hh.ru/vacancies/81264801?host=hh.ru',
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/81264801',
            'relations': [],
            'employer': {
                'id': '1268020',
                'name': 'Юридическая фирма Сентил',
                'url': 'https://api.hh.ru/employers/1268020',
                'alternate_url': 'https://hh.ru/employer/1268020',
                'logo_urls': None,
                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1268020',
                'accredited_it_employer': False,
                'trusted': True
            },
            'snippet': {
                'requirement': 'English. Отличное владение оргтехникой. Стрессоустойчивость. Исполнительность.',
                'responsibility': 'Организация работы и жизнеспособности офиса. Организация и документарное сопровождение процессов, связанных с командировками сотрудников офисов Алматы/Астана. Организация подписки сотрудников...'
            },
            'contacts': None,
            'schedule': None,
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': [],
            'accept_temporary': False,
            'professional_roles': [
                {
                    'id': '110',
                    'name': 'Секретарь, помощник руководителя, ассистент'
                }
            ],
            'accept_incomplete_resumes': True,
            'experience': {
                'id': 'between3And6',
                'name': 'От 3 до 6 лет'
            },
            'employment': {
                'id': 'full',
                'name': 'Полная занятость'
            }
        },
        {
            'id': '78652817',
            'premium': False,
            'name': 'Бортпроводница в авиакомпанию SKYWINGS',
            'department': None,
            'has_test': False,
            'response_letter_required': False,
            'area': {
                'id': '2759',
                'name': 'Ташкент',
                'url': 'https://api.hh.ru/areas/2759'
            },
            'salary': {
                'from': 10000000,
                'to': 15000000,
                'currency': 'UZS',
                'gross': True
            },
            'type': {
                'id': 'open',
                'name': 'Открытая'
            },
            'address': None,
            'response_url': None,
            'sort_point_distance': None,
            'published_at': '2023-05-16T13:11:04+0300',
            'created_at': '2023-05-16T13:11:04+0300',
            'archived': False,
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=78652817',
            'insider_interview': None,
            'url': 'https://api.hh.ru/vacancies/78652817?host=hh.ru',
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/78652817',
            'relations': [],
            'employer': {
                'id': '9358150',
                'name': 'SkyWings',
                'url': 'https://api.hh.ru/employers/9358150',
                'alternate_url': 'https://hh.ru/employer/9358150',
                'logo_urls': None,
                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9358150',
                'accredited_it_employer': False,
                'trusted': True
            },
            'snippet': {
                'requirement': 'Требуемый опыт работы: не требуется. На должность бортпроводницы предъявляются следующие требования: от18 до 25. - образование: не ниже среднего;в...',
                'responsibility': None
            },
            'contacts': None,
            'schedule': None,
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': [],
            'accept_temporary': False,
            'professional_roles': [
                {
                    'id': '159',
                    'name': 'Бортпроводник'
                }
            ],
            'accept_incomplete_resumes': False,
            'experience': {
                'id': 'noExperience',
                'name': 'Нет опыта'
            },
            'employment': {
                'id': 'full',
                'name': 'Полная занятость'
            }
        }
    ],
        'found': 1379124,
        'pages': 20,
        'per_page': 100,
        'page': 1,
        'clusters': None,
        'arguments': None,
        'alternate_url': 'https://hh.ru/search/vacancy?enable_snippets=true&items_on_page=100&page=1'
    }
    return test_dict
