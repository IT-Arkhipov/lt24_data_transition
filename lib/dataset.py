from dataclasses import dataclass

GET_ORDERS_DATES = ('1704585600000', '1704585600000')

ALL_OBJECTS = ''
ALL_DATES = ('0000000000000', '2000000000000')

skipped_key = ['goods', 'states_history']
custom_fields_limit = 3
list_limit = 3
csv_filename = 'converted_json.csv'

DELETION_CHUNK = 50
RESOURCE_FOLDER = 'tests/resources'
FILE_IMPORT_WAIT_SEC = 10

ORDER_START_TIME = '08:00:00'
ORDER_END_TIME = '19:00:00'
ORDER_START_DATE = '2024-02-05 08:00:00'
ORDER_NEXT_DAY = '2024-02-06 09:17:00'
ROUTE_DATE_TIME = '2024-02-05 08:00:00'
OPTIMIZED_DATE_TIME = '2024-02-05 9:15:00'
ORDER_DATE_TIME = '2024-02-05 8:00:00'
ORDER_DATE = '05.02.2024'

VEHICLE_START = '05.02.2024 07:00:00'
VEHICLE_END = '05.02.2024 19:00:00'

VEHICLE_START1 = '05.02.2024 07:00:00'
VEHICLE_END1 = '05.02.2024 12:00:00'

VEHICLE_START2 = '05.02.2024 13:00:00'
VEHICLE_END2 = '05.02.2024 19:00:00'

EVENT_SOURCES = ('order_loaded', 'order_delivered', 'order_not_delivered', 'order_created', 'order_changed',
                 'route_started', 'order_state_changed')
CHANNELS = ('sms', 'email', 'screen', 'webhook')

CUSTOM_FIELD_TARGET = ('Orders', 'Vehicles', 'Routes', 'Divisions', 'Drivers', 'Warehouses')
CUSTOM_FIELD_TARGET_TYPE = ('String', 'Text', 'Number', 'Checkbox', 'List', 'Radiobutton', 'Link', 'Date', 'Time')
CUSTOM_FIELD_PLACEMENT = ('Common', 'Cargo', 'Departure', 'Arrival')

PROTECTED_USER_LOGIN = ('demo@logdep.ru', 'autotesting@test.ru', 'lt24@mailsac.com')

PRESET_GROUPS = ('planningRoutesPresets', 'planningOrdersPresets', 'markersPresets', 'vehiclesPresets',
                 'driversPresets')

POINT_INFO_LOCATION_KIND = ('default', 'address', 'warehouse', 'auto')
DELIVERY_ORDER_KIND = ('auto', 'delivery', 'return', 'transit', 'movement', 'service')
DELIVERY_POINT_ROUTE_POSITION = ('default', 'begin', 'end')
DELIVERY_POINT_PARK_LATE = ('default', 'late', 'on_time')
GPS_PERIOD_TYPES = ('none', 'parking', 'movement', 'collapsed')
ORDER_ACTIONS = ('pickup', 'drop')
CONDITION_OPERATORS = ('and', 'or', 'equal', 'not_equal', 'contains', 'less', 'less_equal', 'greater',
                       'greater_equal', 'between')
ZONE_KIND = ('allowed', 'banned')

COST_FUNCTION = ('distance', 'cost')
VEHICLE_ASSIGNMENT_STRATEGIES = ('minimize_rounds', 'use_all')
ALGORITHMS = ('cluster', 'fast_cluster', 'genetic', 'evenly_genetic', 'evenly_fast', 'simply_districts',
              'transfer_tasks_between_routes', 'chain_monte_carlo', 'neighborhood_ins', 'sequential_build',
              'schedule_build')
GRAPH_SOURCES = ('internal_o_s_m', 'yandex', 'here')
TRACK_TIME_SOURCE = ('statistics', 'traffic')
OPTIMIZE_FUNCS = ('distance', 'duration', 'distance_weigth', 'cost')
PREFERRED_START_MODE = ('default', 'nearest', 'farest', 'earliest')
TRANSPORT_TYPES = ('car', 'bicycle', 'pedestrian', 'truck')
ROUTE_TIME_ORIGIN = ('plan', 'mobile_event', 'location', 'mobile_state')
ROUTE_POINT_ACTION = ('start', 'finish', 'garage', 'loading', 'unloading', 'drop', 'pickup')

ACCESS_PLAN_TABLES = ('DeliveryOrdersEx', 'Stores', 'ServiceAreas', 'Tags', 'Vehicles', 'Drivers', 'Divisions',
                      'DeliveryOrderCategories', 'DeliveryOrderStyles', 'AllRoutesInPlanning', 'Goods', 'GoodsFolders')

ORDER_LOADING = 'warehouse'
ORDER_WINDOW_SIZE = 3_600_000
ORDER_NEXT_WINDOW = 900_000
ORDER_DURATION = 900_000

VEHICLE_BRANDS = (
    'КамАЗ', 'ГАЗ', 'ЗИЛ', 'Mercedes', 'MAN', 'DAF', 'Scania', 'Iveco', 'Volvo', 'Renault', 'Nissan',
    'Tatra', 'Mitsubishi', 'Isuzu')

CUSTOMERS = ([59.931488, 30.296844], [59.928732, 30.307989], [59.930632, 30.316265], [59.927727, 30.326819],
             [59.926247, 30.318256], [59.931196, 30.304114], [59.932111, 30.328393], [59.925304, 30.303288],
             [59.932714, 30.304364], [59.931820, 30.296961], [59.932111, 30.315168], [59.930226, 30.315264])

BANNED_ZONE = ({'lat': 59.917182, 'lon': 30.290370}, {'lat': 59.918815, 'lon': 30.327086},
               {'lat': 59.914688, 'lon': 30.329254}, {'lat': 59.912398, 'lon': 30.287623})

POINTS_IN_BANNED_ZONE = ({'Lat': 59.917182, 'Lon': 30.290370}, {'Lat': 59.918815, 'Lon': 30.327086},
                         {'Lat': 59.914688, 'Lon': 30.329254}, {'Lat': 59.912398, 'Lon': 30.287623})

POINTS_OUTSIDE_BANNED_ZONE = ({'Lat': 59.918117, 'Lon': 30.283223}, {'Lat': 59.919429, 'Lon': 30.332907},
                              {'Lat': 59.913121, 'Lon': 30.334932}, {'Lat': 59.910823, 'Lon': 30.282720})

ORDER_STATES_UUIDS = (
    'dfab6563-55b8-475d-aac5-01b6705265cd',
    '51e45c11-d5c7-4383-8fc4-a2e2e1781230',
    '01c157f5-ec6a-47b6-a655-981489e6022a',
    '8b176fdd-4718-46eb-b4f6-1cf487e5353b',
    'ceb8edd8-a0d9-4116-a8ee-a6c0be89103b',
    'e11e0bf2-4e34-4789-bdb6-b6c284f93bbf',
    '50b9348e-1da1-44e3-b84b-88b68da829a4',
    '4f7175dc-db87-45f6-902e-0e3737f78e77'
)

ORDER_STATE_PAIR = {
    'Новый': 'dfab6563-55b8-475d-aac5-01b6705265cd',
    'Отменён': '51e45c11-d5c7-4383-8fc4-a2e2e1781230',
    'Запланирован': '01c157f5-ec6a-47b6-a655-981489e6022a',
    'Доставляется': '8b176fdd-4718-46eb-b4f6-1cf487e5353b',
    'Выполнен': 'ceb8edd8-a0d9-4116-a8ee-a6c0be89103b',
    'Частично выполнен': 'e11e0bf2-4e34-4789-bdb6-b6c284f93bbf',
    'Отложен': '50b9348e-1da1-44e3-b84b-88b68da829a4',
    'Перенос на дату': '4f7175dc-db87-45f6-902e-0e3737f78e77'
}

ORDERS_STATES = [
    {
        'active': True,
        'color': '#FFFFFF',
        'comment_required': False,
        'comment_templates': [],
        'created': 0,
        'disable_comment_edit_by_driver': False,
        'external_id': '',
        'for_arrival': False,
        'for_departure': False,
        'for_intermediate_point': False,
        'id': 'dfab6563-55b8-475d-aac5-01b6705265cd',
        'is_failed': False,
        'is_loading': False,
        'is_moved_to_end': False,
        'is_moved_to_date': False,
        'is_succeeded': False,
        'last_modified': 0,
        'min_photos': 0,
        'name': 'Новый',
        'version': 0
    },
    {
        'active': True,
        'color': '#FF0000',
        'comment_required': False,
        'comment_templates': [],
        'created': 0,
        'disable_comment_edit_by_driver': False,
        'external_id': '',
        'for_arrival': True,
        'for_departure': True,
        'for_intermediate_point': False,
        'id': '51e45c11-d5c7-4383-8fc4-a2e2e1781230',
        'is_failed': True,
        'is_loading': False,
        'is_moved_to_end': False,
        'is_moved_to_date': False,
        'is_succeeded': False,
        'last_modified': 0,
        'min_photos': 0,
        'name': 'Отменён',
        'version': 0
    },
    {
        'active': True,
        'color': '#00FFFF',
        'comment_required': False,
        'comment_templates': [],
        'created': 0,
        'disable_comment_edit_by_driver': False,
        'external_id': '',
        'for_arrival': False,
        'for_departure': False,
        'for_intermediate_point': False,
        'id': '01c157f5-ec6a-47b6-a655-981489e6022a',
        'is_failed': False,
        'is_loading': False,
        'is_moved_to_end': False,
        'is_moved_to_date': False,
        'is_succeeded': False,
        'last_modified': 0,
        'min_photos': 0,
        'name': 'Запланирован',
        'version': 0
    },
    {
        'active': True,
        'color': '#0080FF',
        'comment_required': False,
        'comment_templates': [],
        'created': 0,
        'disable_comment_edit_by_driver': False,
        'external_id': '',
        'for_arrival': False,
        'for_departure': True,
        'for_intermediate_point': False,
        'id': '8b176fdd-4718-46eb-b4f6-1cf487e5353b',
        'is_failed': False,
        'is_loading': False,
        'is_moved_to_end': False,
        'is_moved_to_date': False,
        'is_succeeded': False,
        'last_modified': 0,
        'min_photos': 0,
        'name': 'Доставляется',
        'version': 0},
    {
        'active': True,
        'color': '#00FF00',
        'comment_required': False,
        'comment_templates': [],
        'created': 0,
        'disable_comment_edit_by_driver': False,
        'external_id': '',
        'for_arrival': True,
        'for_departure': False,
        'for_intermediate_point': False,
        'id': 'ceb8edd8-a0d9-4116-a8ee-a6c0be89103b',
        'is_failed': False,
        'is_loading': False,
        'is_moved_to_end': False,
        'is_moved_to_date': False,
        'is_succeeded': True,
        'last_modified': 0,
        'min_photos': 0,
        'name': 'Выполнен',
        'version': 0
    },
    {
        'active': True,
        'color': '#FFA500',
        'comment_required': False,
        'comment_templates': [],
        'created': 0,
        'disable_comment_edit_by_driver': False,
        'external_id': '',
        'for_arrival': True,
        'for_departure': False,
        'for_intermediate_point': False,
        'id': 'e11e0bf2-4e34-4789-bdb6-b6c284f93bbf',
        'is_failed': False,
        'is_loading': False,
        'is_moved_to_end': False,
        'is_moved_to_date': False,
        'is_succeeded': True,
        'last_modified': 0,
        'min_photos': 0,
        'name': 'Частично выполнен',
        'version': 0
    },
    {
        'active': True,
        'color': '#808080',
        'comment_required': False,
        'comment_templates': [],
        'created': 0,
        'disable_comment_edit_by_driver': False,
        'external_id': '',
        'for_arrival': True,
        'for_departure': False,
        'for_intermediate_point': False,
        'id': '50b9348e-1da1-44e3-b84b-88b68da829a4',
        'is_failed': False,
        'is_loading': False,
        'is_moved_to_end': True,
        'is_moved_to_date': False,
        'is_succeeded': False,
        'last_modified': 0,
        'min_photos': 0,
        'name': 'Отложен',
        'version': 0
    },
    {
        'active': True,
        'color': '#A3E7F1',
        'comment_required': False,
        'comment_templates': [],
        'created': 0,
        'disable_comment_edit_by_driver': False,
        'external_id': '',
        'for_arrival': True,
        'for_departure': False,
        'for_intermediate_point': False,
        'id': '4f7175dc-db87-45f6-902e-0e3737f78e77',
        'is_failed': False,
        'is_loading': False,
        'is_moved_to_end': False,
        'is_moved_to_date': True,
        'is_succeeded': False,
        'last_modified': 0,
        'min_photos': 0,
        'name': 'Перенос на дату',
        'version': 0
    },
]

DARK_COLORS = [0x800000, 0x8B0000, 0xA52A2A, 0xB22222, 0xDC143C, 0xFF0000, 0xFF6347, 0xFF7F50, 0xCD5C5C, 0xF08080,
               0xE9967A, 0xFA8072, 0xFFA07A, 0xFF4500, 0xFF8C00, 0xFFA500, 0xFFD700, 0xB8860B, 0xDAA520, 0x808000,
               0xFFFF00, 0x9ACD32, 0x556B2F, 0x6B8E23, 0x7CFC00, 0x7FFF00, 0xADFF2F, 0x006400, 0x008000, 0x228B22,
               0x00FF00, 0x32CD32, 0x00FA9A, 0x00FF7F, 0x2E8B57, 0x66CDAA, 0x3CB371, 0x20B2AA, 0x2F4F4F, 0x008080,
               0x008B8B, 0x5F9EA0, 0x4682B4, 0x6495ED, 0x00BFFF, 0x1E90FF, 0x191970, 0x000080, 0x00008B, 0x0000CD,
               0x0000FF, 0x4169E1, 0x8A2BE2, 0x4B0082, 0x483D8B, 0x6A5ACD, 0x7B68EE, 0x9370DB, 0x8B008B, 0x9400D3,
               0x9932CC, 0xBA55D3, 0x800080, 0xEE82EE, 0xFF00FF, 0xDA70D6, 0xC71585, 0xDB7093, 0xFF1493, 0xFF69B4,
               0x8B4513, 0xA0522D, 0xD2691E, 0xCD853F, 0xF4A460, 0xDEB887, 0xD2B48C, 0xBC8F8F]

LIGHT_COLORS = [0xAFEEEE, 0x7FFFD4, 0xB0E0E6, 0xFFB6C1, 0xFFC0CB, 0xFAEBD7, 0xF5F5DC, 0xFFE4C4, 0xFFEBCD, 0xF5DEB3,
                0xFFF8DC, 0xFFFACD, 0xFAFAD2, 0xFFFFE0, 0xFFE4B5, 0xFFDEAD, 0xFFDAB9, 0xFFE4E1, 0xFFF0F5, 0xFAF0E6,
                0xFDF5E6, 0xFFEFD5, 0xFFF5EE, 0xF5FFFA, 0xE6E6FA, 0xFFFAF0, 0xF0F8FF, 0xF8F8FF, 0xF0FFF0, 0xFFFFF0,
                0xF0FFFF, 0xFFFAFA]

ZONES_BOUNDARY = [
    [{'lat': 60.124227, 'lon': 30.139873},
     {'lat': 60.045676, 'lon': 30.150173},
     {'lat': 60.047737, 'lon': 30.321834},
     {'lat': 60.125254, 'lon': 30.317027},
     {'lat': 60.124227, 'lon': 30.139873}],
    [{'lat': 60.124227, 'lon': 30.34724},
     {'lat': 60.03709, 'lon': 30.33488},
     {'lat': 60.022659, 'lon': 30.488689},
     {'lat': 60.123541, 'lon': 30.521648},
     {'lat': 60.124227, 'lon': 30.34724}],
    [{'lat': 60.008749, 'lon': 30.209224},
     {'lat': 59.861269, 'lon': 30.168025},
     {'lat': 59.864032, 'lon': 30.544307},
     {'lat': 60.010811, 'lon': 30.54568},
     {'lat': 60.008749, 'lon': 30.209224}],
    [{'lat': 60.076066, 'lon': 30.11996},
     {'lat': 59.982609, 'lon': 30.169399},
     {'lat': 59.932334, 'lon': 30.593746},
     {'lat': 60.023185, 'lon': 30.523708},
     {'lat': 60.076066, 'lon': 30.11996}],
    [{'lat': 59.857268, 'lon': 30.103481},
     {'lat': 59.795732, 'lon': 30.135066},
     {'lat': 59.828243, 'lon': 30.641811},
     {'lat': 59.92007, 'lon': 30.588252},
     {'lat': 59.857268, 'lon': 30.103481}],
    [{'lat': 60.016455, 'lon': 30.555293},
     {'lat': 59.868319, 'lon': 30.623958},
     {'lat': 60.082385, 'lon': 31.051052},
     {'lat': 60.13928, 'lon': 30.825832},
     {'lat': 60.016455, 'lon': 30.555293}],
    [{'lat': 59.93041, 'lon': 29.696987},
     {'lat': 59.94557, 'lon': 29.517085},
     {'lat': 59.702173, 'lon': 30.043056},
     {'lat': 59.75834, 'lon': 30.291622},
     {'lat': 59.855196, 'lon': 30.22433},
     {'lat': 59.93041, 'lon': 29.696987}],
    [{'lat': 59.830317, 'lon': 30.67065},
     {'lat': 59.800576, 'lon': 30.266902},
     {'lat': 59.703561, 'lon': 30.143306},
     {'lat': 59.64452, 'lon': 30.275142},
     {'lat': 59.653557, 'lon': 30.720088},
     {'lat': 59.830317, 'lon': 30.67065}]
]

CUSTOMERS_BOUNDARY = ([59.921494, 30.271311], [59.903327, 30.256688], [59.886163, 30.25274], [59.858544, 30.225274],
                      [59.839889, 30.255486], [59.813615, 30.315911], [59.820531, 30.409981],
                      [59.852997, 30.479364], [59.873544, 30.451212], [59.89356, 30.439196], [59.917013, 30.39731],
                      [59.924769, 30.385294], [59.934591, 30.390787], [59.947683, 30.397654],
                      [59.949061, 30.382204], [59.948544, 30.351305], [59.943549, 30.323153],
                      [59.930284, 30.277834], [59.921494, 30.271311])

GARAGES_LAT_LON = ({'lat': 59.902794, 'lon': 30.320947},
                   {'lat': 59.926405, 'lon': 30.405958},
                   {'lat': 59.882150, 'lon': 30.299233})


@dataclass
class Garage:
    lat: float
    lon: float
    address: str


garages = [
    Garage(lat=59.894238, lon=30.356241, address='Волковский просп., 59, Санкт-Петербург'),
    Garage(lat=59.926080, lon=30.404842, address='ул. Стахановцев, 7, Санкт-Петербург'),
    Garage(lat=59.902882, lon=30.321067, address='Киевская ул., 4, корп. 2, Санкт-Петербург'),
    Garage(lat=59.920720, lon=30.363264, address='Транспортный пер., 10А, Санкт-Петербург'),
    Garage(lat=59.882215, lon=30.299365, address='Кубинская улица, 1к3, Санкт-Петербург'),
    Garage(lat=59.893682, lon=30.248529, address='улица Калинина, 59, Санкт-Петербург')
]


@dataclass
class Warehouse:
    lat: float
    lon: float
    address: str


# Create objects
warehouses = [
    Warehouse(lat=59.911253, lon=30.292877, address='Морской переулок, 3Р, Санкт-Петербург, 197110'),
    Warehouse(lat=59.910442, lon=30.306426, address='Измайловский проспект, 29И, Санкт-Петербург, 190005'),
    Warehouse(lat=59.911425, lon=30.313893, address='7-я Красноармейская улица, 12-14, Санкт-Петербург, 190005'),
    Warehouse(lat=59.911451, lon=30.322985, address='Малодетскосельский проспект, 28А, Санкт-Петербург, 190013')
]


@dataclass
class Customer:
    lat: float
    lon: float
    address: str


customers = [
    Customer(lat=59.931488, lon=30.296844, address='Конногвардейский переулок, 4, Санкт-Петербург'),
    Customer(lat=59.928732, lon=30.307989, address='Вознесенский проспект, 13, Санкт-Петербург'),
    Customer(lat=59.930632, lon=30.316265, address='Казанская улица, 25, Санкт-Петербург'),
    Customer(lat=59.927727, lon=30.326819, address='Апраксин переулок, 13, Санкт-Петербург'),
    Customer(lat=59.926247, lon=30.318256, address='Сенная площадь, 6, Санкт-Петербург'),
    Customer(lat=59.931196, lon=30.304114, address='Большая Морская улица, 54, Санкт-Петербург'),
    Customer(lat=59.932111, lon=30.328393, address='Садовая улица, 17, Санкт-Петербург'),
    Customer(lat=59.925304, lon=30.303288, address='Средняя Подьяческая улица, 11, Санкт-Петербург'),
    Customer(lat=59.932714, lon=30.304364, address='Почтамтская улица, 4, Санкт-Петербург'),
    Customer(lat=59.931820, lon=30.296961, address='улица Якубовича, 24, Санкт-Петербург'),
    Customer(lat=59.932111, lon=30.315168, address='набережная реки Мойки, 58АГ, Санкт-Петербург'),
    Customer(lat=59.930226, lon=30.315264, address='Казанская улица, 27, Санкт-Петербург')
]

additional_point = [
    Customer(lat=59.927652, lon=30.328098, address='Апраксин переулок, 18, Санкт-Петербург'),
    Customer(lat=59.927967, lon=30.322456, address='Гороховая улица, 45, Санкт-Петербург'),
    Customer(lat=59.930572, lon=30.311257, address='переулок Антоненко, 6, Санкт-Петербург'),
    Customer(lat=59.927798, lon=30.306275, address='Казанская улица, 47, Санкт-Петербург'),
]

ORDERS_FILE_COLUMNS = {
    'Код заказа': 'order_external_id',
    'Грузоотправитель': 'departure_customer',
    'Адрес отправления': 'departure_address',
    'Код склада отправления': 'departure_store',
    'Грузополучатель': 'arrival_customer',
    'Адрес прибытия': 'arrival_address',
    'Код склада получателя': 'arrival_store',
    'Подразделение': 'order_division',
    'Категория заказа': 'order_category',
    'Транспорт рейса': 'order_route_vehicle_id',
    'Требуемый транспорт': 'order_required_vehicle_tags',
    'Метки': 'order_tags',
    'Несовместимые метки': 'order_banned_tags',
    'Код рейса': 'order_route_id',
    'Страна отправления': 'departure_country',
    'Страна прибытия': 'arrival_country'
}

UOMS = [
    {'name': 'штука', 'code': '796', 'abbr': 'шт'},
    {'name': 'упаковка', 'code': '778', 'abbr': 'упак'},
    {'name': 'единица', 'code': '642', 'abbr': 'ед'},
    {'name': 'пачка', 'code': '728', 'abbr': 'пач'},
    {'name': 'ящик', 'code': '812', 'abbr': 'ящ'},
]


@dataclass
class ErrorMessages:
    ok: str = 'OK'
    session_not_found: str = 'SessionNotFound'
    no_api_key: str = 'NoAPIKey'
    mobile_client_not_found: str = 'ClientNotFound'
    old_api_client_not_found: str = 'Client not found'
    out_of_range: str = 'Index was out of range.'
    invalid_login_password: str = 'InvalidLoginOrPassword'
    no_orders = 'No orders'
    order_not_found = 'Order not found'


error_message = ErrorMessages()
