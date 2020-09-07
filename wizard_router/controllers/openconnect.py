from nanohttp import RestController, json


class OpenConnectController(RestController):

    @json(prevent_form=True)
    def status(self):
        open_connect= dict(
            status='active',
        )
        return open_connect

    @json(prevent_form=True)
    def reset(self):
        open_connect = dict(
            status='active',
        )
        return open_connect

    @json(prevent_form=True)
    def stop(self):
        open_connect = dict(
            status='in-active',
        )
        return open_connect

