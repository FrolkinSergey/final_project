import random
from datetime import datetime
import pytest
from jsonschema import validate
from api_clients.esb_client import ESBApiClient
from api_clients.esb_schemas import esb_schema_data_array, esb_schema_data_object, esb_schema_data_null, \
    esb_schema_error, esb_schema_error_data_array, esb_schema_error_data_object

esb_client = ESBApiClient()


@pytest.mark.parametrize(("key", "status_code", "schema"),
                         [("option", 200, esb_schema_data_array),
                          ("statusAccessPoint", 200, esb_schema_data_array),
                          ("statusConnection", 200, esb_schema_data_array),
                          ("unknown1", 400, esb_schema_error)])
def test_dic_get(base_esb_api_url, headers, key, status_code, schema):
    data = {
        "dicName": key
    }
    response = esb_client.dic_get(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == status_code
    assert json_response
    validate(instance=json_response, schema=schema)


@pytest.mark.parametrize(("nls", "email"), [("123123456789", "autotest_13@autotest.ru")])
def test_client_create(base_esb_api_url, headers, nls, email):
    data = {
        "nls": nls,
        "email": email,
        "contacts": email
    }
    response = esb_client.client_create(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    data = json_response.get('responseData')
    client_id = data.get('client_id')
    validate(instance=json_response, schema=esb_schema_data_object)
    return client_id


@pytest.mark.parametrize(("nls", "status_code", "schema"),
                         [("850000204241", 200, esb_schema_data_object),
                          ("850000204225", 200, esb_schema_data_object),
                          ("123456789000", 200, esb_schema_error_data_object)])
def test_client_find(base_esb_api_url, headers, nls, status_code, schema):
    count_max = 10
    data = {
        "nls": nls,
        "countMax": count_max
    }
    response = esb_client.client_find(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == status_code
    assert json_response
    validate(instance=json_response, schema=schema)


@pytest.mark.parametrize(("idf_type", "idf_value", "lvl", "status_code", "schema"),
                         [(7, "7715422010", 1, 200, esb_schema_data_object),
                          (1, "146118", 2, 200, esb_schema_data_object),
                          (7, "146118", 2, 400, esb_schema_error)])
def test_client_get(base_esb_api_url, headers, idf_type, idf_value, lvl, status_code, schema):
    data = {
        "clientIdentifyType": idf_type,
        "clientIdentifyValue": idf_value,
        "lvl_info": lvl
    }
    response = esb_client.client_get(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == status_code
    assert json_response
    validate(instance=json_response, schema=schema)


def test_client_list(base_esb_api_url, headers):
    response = esb_client.client_list(base_esb_api_url, headers)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=esb_schema_data_array)


@pytest.mark.parametrize(("idf_value", "lvl", "status_code", "schema"),
                         [("3382", 1, 200, esb_schema_data_object),
                          ("3382", 2, 200, esb_schema_data_object),
                          ("3382", 3, 400, esb_schema_error)])
def test_co_get(base_esb_api_url, headers, idf_value, lvl, status_code, schema):
    data = {
        "id": idf_value,
        "lvl_info": lvl
    }
    response = esb_client.co_get(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == status_code
    assert json_response
    validate(instance=json_response, schema=schema)


@pytest.mark.parametrize(("client_id", "nls", "global_id", "max_ap_count", "service"),
                         [("146055", "850000204225", "20242898", 10, 7)])
def test_co_create(base_esb_api_url, headers, client_id, nls, global_id, max_ap_count, service):
    name_row = esb_client.name_date()
    name = "co/create" + name_row
    data = {
        "client_id": client_id,
        "name": name,
        "nls": nls,
        "address": {
            "global_id": global_id
        },
        "max_access_point_count": max_ap_count,
        "service": service
    }
    response = esb_client.co_create(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    data = json_response.get('responseData')
    co_id = data.get('id')
    validate(instance=json_response, schema=esb_schema_data_object)
    return co_id


def test_co_update(base_esb_api_url, headers):
    co_id = 3483
    name_row = esb_client.name_date()
    name = "co/update" + name_row
    contacts = "contacts" + name_row
    count_list = [5, 10, 50, 100]
    mapc = random.choice(count_list)
    data = {
        "id": co_id,
        "name": name,
        "contacts": contacts,
        "max_access_point_count": mapc
    }
    response = esb_client.co_update(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=esb_schema_data_null)


def test_co_delete(base_esb_api_url, headers):
    co_id = test_co_create(base_esb_api_url, headers, 146055, "850000204225", "20242898",
                           10, 7)
    data = {
        "id": co_id
    }
    response = esb_client.co_delete(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=esb_schema_data_null)


def test_co_deactivate(base_esb_api_url, headers):
    co_id = test_co_create(base_esb_api_url, headers, 146055, "850000204225", "20242898",
                           10, 7)
    data = {
        "id": co_id
    }
    response = esb_client.co_deactivate(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=esb_schema_data_null)


@pytest.mark.parametrize(("client_id", "status_code", "schema"),
                         [("145981", 200, esb_schema_data_array),
                          ("146128", 200, esb_schema_error_data_array)])
def test_ap_list(base_esb_api_url, headers, client_id, status_code, schema):
    data = {
        "clientId": client_id,
    }
    response = esb_client.ap_list(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == status_code
    assert json_response
    validate(instance=json_response, schema=schema)


@pytest.mark.parametrize(("ap_id", "lvl", "status_code", "schema"),
                         [("5580", 1, 200, esb_schema_data_object),
                          ("5580", 2, 200, esb_schema_data_object),
                          ("5580", 3, 200, esb_schema_data_object),
                          ("5580", 4, 400, esb_schema_error)])
def test_ap_get(base_esb_api_url, headers, ap_id, lvl, status_code, schema):
    data = {
        "id": ap_id,
        "lvl_info": lvl
    }
    response = esb_client.ap_get(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == status_code
    assert json_response
    validate(instance=json_response, schema=schema)


def test_ap_create(base_esb_api_url, headers):
    co_id = test_co_create(base_esb_api_url, headers, 146055, "850000204225", "20242898",
                           10, 4)
    mac = esb_client.random_mac_address()
    sn = mac.replace(":", "")
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    name_ap = "ap_create_" + datetime.now().strftime("%d_%m")
    data = {
        "connectionId": co_id,
        "access_point": {
            "name": name_ap,
            "mac": mac,
            "serial_number": sn,
            "model": "Generic",
            "installation_date": f"{date}T{time}.000Z",
            "vendor": "Cambium",
            "status": 1
        }
    }
    response = esb_client.ap_create(base_esb_api_url, headers, data)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=esb_schema_data_object)
