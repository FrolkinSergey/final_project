esb_schema_data_array = {
        "type": "object",
        "properties": {
            "osbRequestId": {"type": "string"},
            "code": {"type": "integer"},
            "message": {"type": "null"},
            "errorSource": {"type": "null"},
            "messageDetails": {"type": "null"},
            "responseData": {"type": "array"},
        },
        "required": ["osbRequestId", "code", "message", "errorSource", "messageDetails", "responseData"]
    }

esb_schema_data_object = {
    "type": "object",
    "properties": {
        "osbRequestId": {"type": "string"},
        "code": {"type": "integer"},
        "message": {"type": "null"},
        "errorSource": {"type": "null"},
        "messageDetails": {"type": "null"},
        "responseData": {"type": "object"},
    },
    "required": ["osbRequestId", "code", "message", "errorSource", "messageDetails", "responseData"]
}

esb_schema_data_null = {
    "type": "object",
    "properties": {
        "osbRequestId": {"type": "string"},
        "code": {"type": "integer"},
        "message": {"type": "null"},
        "errorSource": {"type": "null"},
        "messageDetails": {"type": "null"},
        "responseData": {"type": "null"},
    },
    "required": ["osbRequestId", "code", "message", "errorSource", "messageDetails", "responseData"]
}

esb_schema_error = {
    "type": "object",
    "properties": {
        "osbRequestId": {"type": "string"},
        "code": {"type": "integer"},
        "message": {"type": "string"},
        "errorSource": {"type": "null"},
        "messageDetails": {"type": "string"},
        "responseData": {"type": "null"},
    },
    "required": ["osbRequestId", "code", "message", "errorSource", "messageDetails", "responseData"]
}

esb_schema_error_data_object = {
    "type": "object",
    "properties": {
        "osbRequestId": {"type": "string"},
        "code": {"type": "integer"},
        "message": {"type": "string"},
        "errorSource": {"type": "null"},
        "messageDetails": {"type": "string"},
        "responseData": {"type": "object"},
    },
    "required": ["osbRequestId", "code", "message", "errorSource", "messageDetails", "responseData"]
}

esb_schema_error_data_array = {
    "type": "object",
    "properties": {
        "osbRequestId": {"type": "string"},
        "code": {"type": "integer"},
        "message": {"type": "string"},
        "errorSource": {"type": "null"},
        "messageDetails": {"type": "string"},
        "responseData": {"type": "array"},
    },
    "required": ["osbRequestId", "code", "message", "errorSource", "messageDetails", "responseData"]
}
