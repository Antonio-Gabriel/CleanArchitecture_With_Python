class HttpErrors:
    """ Class to define http errors """

    @staticmethod
    def _400():
        """ Http error 400 - Bad Request """

        return {"status_code": 400, "body": {"error": "Bad Request"}}

    def _404():
        """ Http error 404 - Not Found """

        return {"status_code": 404, "body": {"error": "Not Found"}}
