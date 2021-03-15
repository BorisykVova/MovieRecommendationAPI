TORTOISE_ORM = {
    'connections': {
        'mysql': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '172.29.0.2',
                'port': 3306,
                'user': 'root',
                'password': 'root',
                'database': 'MovieRecommendAPI',
            }
        }
    },
    'apps': {

        # 'auth': {
        #     'models': ['auth.models'],
        #     'default_connection': 'mysql',
        # },
    }
}
