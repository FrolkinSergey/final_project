from datetime import datetime
import random
import requests


class ESBApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.verify = False

    def name_date(self):
        currentday = datetime.now().strftime("%d")
        currentmonth = datetime.now().strftime("%m")
        currentyear = datetime.now().strftime("%Y")
        now = datetime.now().strftime("%H:%M:%S")
        name = "autotest " + "{year}.{month}.{day}" + ":" + now
        time_name = name.format(year=currentyear, month=currentmonth, day=currentday)
        return time_name

    def random_mac_address(self):
        mac_row = [0x00, 0x16, 0x3e,
                   random.randint(0x00, 0x7f),
                   random.randint(0x00, 0xff),
                   random.randint(0x00, 0xff)]
        mac = ':'.join(map(lambda x: "%02x" % x, mac_row))
        return mac

    def dic_get(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/dic/get",
                                     headers=headers,
                                     json=data)
        return response

    def client_create(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/client/create",
                                     headers=headers,
                                     json=data)
        return response

    def client_find(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/client/find",
                                     headers=headers,
                                     json=data)
        return response

    def client_get(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/client/get",
                                     headers=headers,
                                     json=data)
        return response

    def client_list(self, base_esb_api_url, headers):
        response = self.session.post(url=f"{base_esb_api_url}/client/list",
                                     headers=headers)
        return response

    def co_get(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/co/get",
                                     headers=headers,
                                     json=data)
        return response

    def co_create(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/co/create",
                                     headers=headers,
                                     json=data)
        return response

    def co_update(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/co/update",
                                     headers=headers,
                                     json=data)
        return response

    def co_delete(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/co/delete",
                                     headers=headers,
                                     json=data)
        return response

    def co_deactivate(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/co/deactivate",
                                     headers=headers,
                                     json=data)
        return response

    def ap_list(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/ap/list",
                                     headers=headers,
                                     json=data)
        return response

    def ap_get(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/ap/get",
                                     headers=headers,
                                     json=data)
        return response

    def ap_create(self, base_esb_api_url, headers, data):
        response = self.session.post(url=f"{base_esb_api_url}/ap/create",
                                     headers=headers,
                                     json=data)
        return response
