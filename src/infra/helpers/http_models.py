from typing import Dict


class HttpRequest:
    """ HttpRequest Representation """

    def __init__(self, header: Dict = None, body: Dict = None, query: Dict = None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self):
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"
        )


class HttpResponse:
    """ HttpResponse Representation """

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return (
            f"HttpResponse (status_code={self.status_code}, body={self.body})"
        )
