from nanohttp import RestController, json


class TokenController(RestController):

    @json(prevent_empty_form=True)
    def create(self):
        pass

    @json
    def invalidate(self):
        pass

