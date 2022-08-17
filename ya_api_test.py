import requests


def yd_new_folder(token, folder):
    params = {'path': folder}
    headers = {'Authorization': token}
    create_folder = requests.put(f'https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)
    response = create_folder.json()
    print(response)
    return response


class TestYDAPI:
    @classmethod
    def teardown_class(cls):
        params = {'path': 'aaaa'}
        headers = {'Authorization': ' '}
        requests.delete(f'https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)

    def test_create_folder(self):
        assert yd_new_folder(' ', 'aaaa')['method'] == 'GET'

    def test_same_folder(self):
        assert yd_new_folder(' ', 'aaaa')['message'] == \
                                'По указанному пути "aaaa" уже существует папка с таким именем.'

    def test_wrong_token(self):
        assert yd_new_folder('token', 'aaaa')['description'] == 'Unauthorized'

    def test_yd_not_avail(self):
        assert yd_new_folder(' ', 'aaaa')['message'] != \
                                'Сервис временно недоступен.'
