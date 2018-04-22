
def parse_response(response, cls):
        if response.status != 200:
            raise NameHttpError(response)

        try:
            res = cls.from_json(response.body)
        except Exception, description:
            raise NameParseError(description, response.body)

        return res
