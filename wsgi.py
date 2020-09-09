from wizard_router import wizard_router


wizard_router.configure()
wizard_router.initialize_orm()

verbs = [
    'GET',
    'CREATE',
    'DEFINE',
    'LIST',
    'LOGOUT',
    'METADATA',
    'REVOKE',
    'UPDATE',
    'CHECK',
    'CLAIM',
    'REGISTER',
    'INVITE',
    'JOIN',
    'CHANGE',
    'RESET',
    'BIND',
    'ASK',
    'INVALIDATE',
    'STOP',
    'RESTART',
    'STATUS',
]


http_headers = [
    'X-Pagination-Count',
    'X-Pagination-Take',
    'X-Pagination-Skip',
    'X-Identity',
    'X-New-JWT-Token',
]


def cross_origin_helper_app(environ, start_response):

    def better_start_response(status, headers, *args, **kw):
        headers.append(('Access-Control-Allow-Origin', '*'))
        headers.append(('Access-Control-Allow-Headers', 'Content-Type, Authorization, Cache-Control'))
        headers.append(('Access-Control-Allow-Credentials', 'true'))
        headers.append(('Access-Control-Cache-Control', 'true'))
        headers.append(('Access-Control-Allow-Methods', ', '.join(verbs)))
        headers.append(('Access-Control-Expose-Headers', ', '.join(http_headers)))
        start_response(status, headers, *args, **kw)

    if environ['REQUEST_METHOD'] == 'OPTIONS':
        better_start_response('200 Ok', [])
        return []

    return wizard_router(environ, better_start_response)


app = cross_origin_helper_app

