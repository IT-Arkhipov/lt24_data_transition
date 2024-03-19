from dataclasses import dataclass
from lib import dataset


@dataclass
class Settings:
    test_env: str = 'dev'
    base_url: str = 'http://'
    session_id: str = ''
    mobile_url: str = 'http://'
    mobile_session_id: str = ''
    api_url: str = 'http://'
    api_key: str = ''
    token: str = ''
    web_url: str = ''
    send_report: bool = False
    receiver_email = ''


settings = Settings()


@dataclass
class Credentials:
    login: str = ''
    password: str = ''
    mobile_login: str = ''
    mobile_password: str = ''
    client_code:  str = ''


credentials = Credentials()


@dataclass
class Endpoints:
    delete_access_plans: str = '/lt24/api/access_plans'
    delete_carriers: str = '/lt24/api/carriers'
    delete_categories: str = '/lt24/api/categories/'
    delete_custom_fields: str = '/lt24/api/customfields'
    delete_customers: str = '/lt24/api/customers/'
    delete_data_views: str = '/lt24/api/data_views'
    delete_divisions: str = '/lt24/api/divisions/'
    delete_drivers: str = '/lt24/api/drivers'
    delete_goods: str = '/lt24/api/goods'
    delete_notification_templates: str = '/lt24/api/notification_templates'
    delete_order_states: str = '/lt24/api/order_states'
    delete_orders: str = '/lt24/api/orders'
    delete_presets: str = '/lt24/api/presets'
    delete_routes: str = '/lt24/api/routes'
    delete_tags: str = '/lt24/api/tags'
    delete_uoms: str = '/lt24/api/uoms'
    delete_users: str = '/lt24/api/users'
    delete_vehicle_brands: str = '/lt24/api/vehicles/brands'
    delete_vehicles: str = '/lt24/api/vehicles'
    delete_warehouses: str = '/lt24/api/warehouses'
    delete_zones: str = '/lt24/api/zones'
    delete_zones_vehicles: str = '//lt24/api/zones/vehicles'

    get_access_plans_list: str = '/lt24/api/access_plans/list'
    get_access_plans_view: str = '/lt24/api/access_plans/view'
    get_carriers_list: str = '/lt24/api/carriers/list'
    get_carriers_view: str = '/lt24/api/carriers/view'
    get_categories_list: str = '/lt24/api/categories/list'
    get_categories_view: str = '/lt24/api/categories/view'
    get_countries_list: str = '/lt24/api/countries/list'
    get_countries_view: str = '/lt24/api/countries/view'
    get_custom_fields_list: str = '/lt24/api/customfields/list'
    get_custom_fields_view: str = '/lt24/api/customfields/view'
    get_customers_list: str = '/lt24/api/customers/list'
    get_divisions_list: str = '/lt24/api/divisions/list'
    get_divisions_view: str = '/lt24/api/divisions/view'
    get_drivers_list: str = '/lt24/api/drivers/list'
    get_drivers_view: str = '/lt24/api/drivers/view'
    get_import_state: str = '/lt24/api/import/state'
    get_goods_list: str = '/lt24/api/goods/list'
    get_gui_settings: str = '/lt24/api/gui/settings'
    get_mobile_token: str = '/lt24/api/auth/mobile'
    get_notification_templates_list: str = '/lt24/api/notification_templates/list'
    get_notification_templates_send: str = '/lt24/api/notification_templates/send'
    get_notification_templates_view: str = '/lt24/api/notification_templates/view'
    get_orders_events: str = '/lt24/api/orders/events'
    get_orders_list: str = '/lt24/api/orders/list'
    get_order_states_list: str = '/lt24/api/order_states/list'
    get_order_states_view: str = '/lt24/api/order_states/view'
    get_orders_report_totals: str = '/lt24/api/orders/report/totals'
    get_orders_scroll: str = '/lt24/api/orders/scroll'
    get_packs_list: str = '/lt24/api/packs/list'
    get_planning_scope: str = '/lt24/api/planning_scope'
    get_presets: str = '/lt24/api/presets'
    get_routes_list: str = '/lt24/api/routes/list'
    get_routes_events: str = '/lt24/api/routes/events'
    get_routes_events_blobs: str = '/lt24/api/routes/events/blobs'
    get_session: str = '/lt24/api/auth/session'
    get_settings: str = '/lt24/api/settings'
    get_tags_list: str = '/lt24/api/tags/list'
    get_tags_view: str = '/lt24/api/tags/view'
    get_token: str = '/lt24/api/auth/token'
    get_uoms_list: str = '/lt24/api/uoms/list'
    get_uoms_view: str = '/lt24/api/uoms/view'
    get_users_list: str = '/lt24/api/users/list'
    get_users_view: str = '/lt24/api/users/view'
    get_vehicle_brands_list: str = '/lt24/api/vehicles/brands/list'
    get_vehicle_brands_view: str = '/lt24/api/vehicles/brands/view'
    get_vehicles_list: str = '/lt24/api/vehicles/list'
    get_vehicles_view: str = '/lt24/api/vehicles/view'
    get_warehouses_list: str = '/lt24/api/warehouses/list'
    get_warehouses_view: str = '/lt24/api/warehouses/view'
    get_zones_list: str = '/lt24/api/zones/list'
    get_zones_view: str = '/lt24/api/zones/view'

    post_access_plans: str = '/lt24/api/access_plans'
    post_carriers: str = '/lt24/api/carriers'
    post_categories: str = '/lt24/api/categories'
    post_custom_fields: str = '/lt24/api/customfields'
    post_customers: str = '/lt24/api/customers/'
    post_divisions: str = '/lt24/api/divisions/'
    post_divisions_file: str = '/lt24/api/divisions/file'
    post_drivers: str = '/lt24/api/drivers'
    post_drivers_file: str = '/lt24/api/drivers/file'
    post_drivers_photo: str = '/lt24/api/drivers/photo'
    post_drivers_push_log: str = '/lt24/api/drivers/push_log'
    post_goods: str = '/lt24/api/goods'
    post_gui_settings: str = '/lt24/api/gui/settings'
    post_notification_templates: str = '/lt24/api/notification_templates'
    post_order_states: str = '/lt24/api/order_states'
    post_order_states_set: str = '/lt24/api/order_states/set'
    post_orders: str = '/lt24/api/orders'
    post_orders_file: str = '/lt24/api/orders/file'
    post_orders_photo: str = '/lt24/api/orders/photo'
    post_presets: str = '/lt24/api/presets'
    post_routes: str = '/lt24/api/routes'
    post_routes_add: str = '/lt24/api/routes/add'
    post_routes_clear_history: str = '/lt24/api/routes/clear_history'
    post_routes_exclude: str = '/lt24/api/routes/exclude'
    post_routes_insert: str = '/lt24/api/routes/insert'
    post_routes_on_fact: str = '/lt24/api/routes/on_fact'
    post_routes_opt: str = '/lt24/api/routes/opt'
    post_routes_purge: str = '/lt24/api/routes/purge'
    post_routes_reorder: str = '/lt24/api/routes/reorder'
    post_routes_set_carrier: str = '/lt24/api/routes/set_carrier'
    post_routes_set_editable: str = '/lt24/api/routes/set_editable'
    post_routes_track: str = '/lt24/api/routes/track'
    post_routes_update: str = '/lt24/api/routes/update'
    post_routes_update_totals: str = '/lt24/api/routes/update_totals'
    post_settings: str = '/lt24/api/settings'
    post_session: str = '/lt24/api/auth/session'
    post_tags: str = '/lt24/api/tags'
    post_uoms: str = '/lt24/api/uoms'
    post_users: str = '/lt24/api/users'
    post_users_drop_sessions: str = '/lt24/api/users/drop_sessions'
    post_users_password: str = '/lt24/api/users/password'
    post_users_photo: str = '/lt24/api/users/photo'
    post_vehicle_brands: str = '/lt24/api/vehicles/brands'
    post_vehicles: str = '/lt24/api/vehicles'
    post_vehicles_file: str = '/lt24/api/vehicles/file'
    post_vehicles_list: str = '/lt24/api/vehicles/list'
    post_warehouses: str = '/lt24/api/warehouses'
    post_warehouses_file: str = '/lt24/api/warehouses/file'
    post_zones: str = '/lt24/api/zones'
    post_zones_vehicles: str = '/lt24/api/zones/vehicles'
    post_import_start: str = '/lt24/api/import/start'
    post_import_xls_upload: str = '/lt24/api/import/xls/upload'

    put_presets: str = '/lt24/api/presets'
    put_orders_photo: str = '/lt24/api/orders/photo'


endpoint = Endpoints()


@dataclass
class AccessPlanTable:
    table: str
    can_create: bool
    can_modify: bool
    can_delete: bool
    can_view: bool


@dataclass
class AccessPlanTables:
    delivery_orders_ex: AccessPlanTable
    stores: AccessPlanTable
    service_areas: AccessPlanTable
    tags: AccessPlanTable
    vehicles: AccessPlanTable
    drivers: AccessPlanTable
    divisions: AccessPlanTable
    delivery_order_categories: AccessPlanTable
    delivery_order_styles: AccessPlanTable
    all_routes_in_planning: AccessPlanTable
    goods: AccessPlanTable
    goods_folder: AccessPlanTable


access_plan_table = AccessPlanTables(
    delivery_orders_ex=AccessPlanTable(table='DeliveryOrdersEx', can_modify=True, can_delete=True, can_create=True,
                                       can_view=True),
    stores=AccessPlanTable(table='Stores', can_modify=True, can_delete=True, can_create=True,
                           can_view=True),
    service_areas=AccessPlanTable(table='ServiceAreas', can_modify=True, can_delete=True, can_create=True,
                                  can_view=True),
    tags=AccessPlanTable(table='Tags', can_modify=True, can_delete=True, can_create=True, can_view=True),
    vehicles=AccessPlanTable(table='Vehicles', can_modify=True, can_delete=True, can_create=True, can_view=True),
    drivers=AccessPlanTable(table='Drivers', can_modify=True, can_delete=True, can_create=True, can_view=True),
    divisions=AccessPlanTable(table='Divisions', can_modify=True, can_delete=True, can_create=True, can_view=True),
    delivery_order_categories=AccessPlanTable(table='DeliveryOrderCategories', can_modify=True,
                                              can_delete=True, can_create=True, can_view=True),
    delivery_order_styles=AccessPlanTable(table='DeliveryOrderStyles', can_modify=True,
                                          can_delete=True, can_create=True, can_view=True),
    all_routes_in_planning=AccessPlanTable(table='AllRoutesInPlanning', can_modify=True,
                                           can_delete=True, can_create=True, can_view=True),
    goods=AccessPlanTable(table='Goods', can_modify=True,
                          can_delete=True, can_create=True, can_view=True),
    goods_folder=AccessPlanTable(table='GoodsFolders', can_modify=True,
                                 can_delete=True, can_create=True, can_view=True)
)


@dataclass
class AccessPlanTableSections:
    sections: dict


access_plan_sections = AccessPlanTableSections(
    sections={
        'PAGE.REPORTS.TITLE': True,
        'PAGE.PLANNING.TITLE': True,
        'PAGE.SETTINGS.TITLE': True,
        'PAGE.MONITORING.TITLE': True,
        'PAGE.NOTIFICATIONS.TITLE': True,
        'ACCESS_PLANS_SECTIONS.SETTINGS.USERS': True,
        'ACCESS_PLANS_SECTIONS.SETTINGS.INTEGRATIONS': True,
        'ACCESS_PLANS_SECTIONS.SETTINGS.NOTIFICATIONS': True
    }
)


class EntitiesDefinition:
    def __init__(self):
        self.order = {
            'order_date': '',  # deprecated
            'start_date': dataset.ORDER_START_DATE,  # дата заказа, поле start_date, default = ''
            'start_time': dataset.ORDER_START_TIME,  # время первого заказа, поле start_time, default = ''
            'set_window': True,  # установка временных окон заказов, default = False, погрузка/разгрузка круглосуточно
            'window_size': dataset.ORDER_WINDOW_SIZE,
            # временное окно времени погрузки/разгрузки в мс, default = 3_600_000 мс = 1 час
            'next_window': dataset.ORDER_NEXT_WINDOW,
            # смещение времени следующего заказа в мс, default = 900_000 мс = 15 минут
            'duration': dataset.ORDER_DURATION,
            # время на доставку (погрузка-разгрузка) в мс, default = 900_000 мс = 15 минут
            'orders_quantity': 5,  # количество заказов, default = 1
            'loading': dataset.ORDER_LOADING,  # место погрузки заказов, default = 'warehouse' alternative = 'address'
            'geocode': False,
            'warehouse_id': '',
            'division_id': '',
            'goods': [],
            'custom_fields': [],
            'weight': 0.0,
            'volume': 0.0,
            'units': 0.0,
            'invoice_total': 0.0,
            'kind': 'delivery',
            'external_id': '',
            'customer_id': '',
            'location': {
                'lat': 0,
                'lon': 0,
                'raw': ''
            }
        }
        self.vehicle = {
            'garage_start': False,  # признак старта транспорта из гаража, default = False
            'do_not_return': False,  # не возвращаться в точку в начальную точку погрузки, default = False
            'is_hgv': False,  # признак грузового транспорта, default = False
            'division_id': '',
            'driver_id': '',
            'start_location': {
                'lat': 0,
                'lon': 0,
                'set_manually': False,
                'raw': ''
            },
            'id': '',
        }
        self.route = {
            'route_date': dataset.ROUTE_DATE_TIME,  # deprecated
            'fixed_start_time': dataset.OPTIMIZED_DATE_TIME,  # дата/время при оптимизации рейса, default = ''
            'optimization': 'none',  # вид оптимизации создаваемого рейса, default = 'none'
            'algorithm': 'exp',  # алгоритм при оптимизации рейса, default = ''
            'online': False,  # признак оптимизации онлайн
            'vehicle_id': '',
            'driver_id': '',
            'orders_ids': [],
            'tracks': True,
            'name': '',
            'external_id': '',
            'id': ''
        }
        self.driver = {
            'use_mobile_api': True,  # признак доступа водителя к рейсам из мобильного приложения, default = True
            'mobile_api_login': '',
            'mobile_api_password': '',
            'id': '',
        }
        self.zone = {
            'kind': 'banned',  # тип генерируемой зоны, default = 'banned'
            'apply_to_all': False,  # признак применения зоны ко всему транспорту, default = False
            'apply_to_hgv': False,  # признак применения зоны ко грузовому транспорту, default = False
            'boundary': dataset.BANNED_ZONE,  # границы зоны (запрета), default = ''
            'external_id': '',
            'id': '',
        }
        self.warehouse = {
            'division_id': '',
            'external_id': '',
            'location': {
                'lat': '',
                'lon': '',
                'raw_original': '',
                'set_manually': False,
                'fuzzy_geocoded': False
            },
            'id': '',
        }
        self.access_plan = {
            'id': '',
        }
        self.customer = {
            'external_id': '',
            'name': '',
            'id': '',
        }
        self.division = {
            'external_id': '',
            'name': '',
            'id': '',
        }
        self.carrier = {
            'custom_fields': [],
            'external_id': '',
            'name': '',
            'id': '',
        }
        self.category = {
            'external_id': '',
            'name': '',
            'id': ''
        }
        self.tag = {
            'external_id': '',
            'name': '',
            'id': ''
        }
        self.notification_template = {
            'external_id': '',
            'name': '',
            'id': ''
        }
        self.order_state = {
            'external_id': '',
            'name': '',
            'id': ''
        }
        self.custom_field = {
            'field_target': '',
            'field_type': '',
            'placement': '',
            'show_always': True,
            'web_visible': True,
            'web_editable': True,
            'mobile_visible': True,
            'mobile_editable': True,
            'mobile_required_for_complete': True,
            'mobile_required_for_cancel': False,
            'id': '',
            'name': ''
        }
        self.uom = {
            'abbreviation': '',
            'external_id': '',
            'id': '',
        }
        self.good = {
            'external_id2': '',
            'article': '',
            'barcodes': [],
            'description': '',
            'is_serial': False,
            'packs': [],
            'folder': '',
            'name': '',
            'external_id': '',
            'id': '',
        }
        self.pack = {
            'id': '',
            'quantity': 0.0,
            'uom_id': '',
            'weight': 0.0,
            'volume': 0.0,
            'volume_alt': 0.0,
            'barcode': {}
        }
        self.user = {
            'login': '',
            'password': '',
            'client_code': '',
            'contact_name': '',
            'contact_phone': '',
            'carrier_id': '',
            'admin_account': False,
            'main_account': False,
            'blocked': False,
            'access_plan': '',
            'divisions': [],
            'id': ''
        }

    def reset(self):
        self.order = {
            'order_date': '',  # deprecated
            'start_date': dataset.ORDER_START_DATE,  # дата заказа, поле start_date, default = ''
            'start_time': dataset.ORDER_START_TIME,  # время первого заказа, поле start_time, default = ''
            'set_window': True,  # установка временных окон заказов, default = False, погрузка/разгрузка круглосуточно
            'window_size': dataset.ORDER_WINDOW_SIZE,
            # временное окно времени погрузки/разгрузки в мс, default = 3_600_000 мс = 1 час
            'next_window': dataset.ORDER_NEXT_WINDOW,
            # смещение времени следующего заказа в мс, default = 900_000 мс = 15 минут
            'duration': dataset.ORDER_DURATION,
            # время на доставку (погрузка-разгрузка) в мс, default = 900_000 мс = 15 минут
            'orders_quantity': 5,  # количество заказов, default = 1
            'loading': dataset.ORDER_LOADING,  # место погрузки заказов, default = 'warehouse' alternative = 'address'
            'geocode': False,
            'warehouse_id': '',
            'division_id': '',
            'goods': [],
            'custom_fields': [],
            'weight': 0.0,
            'volume': 0.0,
            'units': 0.0,
            'invoice_total': 0.0,
            'kind': 'delivery',
            'external_id': '',
            'customer_id': '',
            'location': {
                'lat': 0,
                'lon': 0,
                'raw': ''
            }
        }
        self.vehicle = {
            'garage_start': False,  # признак старта транспорта из гаража, default = False
            'do_not_return': False,  # не возвращаться в точку в начальную точку погрузки, default = False
            'is_hgv': False,  # признак грузового транспорта, default = False
            'division_id': '',
            'driver_id': '',
            'start_location': {
                'lat': 0,
                'lon': 0,
                'set_manually': False,
                'raw': ''
            },
            'id': '',
        }
        self.route = {
            'route_date': dataset.ROUTE_DATE_TIME,  # deprecated
            'fixed_start_time': dataset.OPTIMIZED_DATE_TIME,  # дата/время при оптимизации рейса, default = ''
            'optimization': 'none',  # вид оптимизации создаваемого рейса, default = 'none'
            'algorithm': 'exp',  # алгоритм при оптимизации рейса, default = ''
            'online': False,  # признак оптимизации онлайн
            'vehicle_id': '',
            'driver_id': '',
            'orders_ids': [],
            'tracks': True,
            'name': '',
            'external_id': '',
            'id': ''
        }
        self.driver = {
            'use_mobile_api': True,  # признак доступа водителя к рейсам из мобильного приложения, default = True
            'mobile_api_login': '',
            'mobile_api_password': '',
            'id': '',
        }
        self.zone = {
            'kind': 'banned',  # тип генерируемой зоны, default = 'banned'
            'apply_to_all': False,  # признак применения зоны ко всему транспорту, default = False
            'apply_to_hgv': False,  # признак применения зоны ко грузовому транспорту, default = False
            'boundary': dataset.BANNED_ZONE,  # границы зоны (запрета), default = ''
            'external_id': '',
            'id': '',
        }
        self.warehouse = {
            'division_id': '',
            'external_id': '',
            'location': {
                'lat': '',
                'lon': '',
                'raw_original': '',
                'set_manually': False,
                'fuzzy_geocoded': False
            },
            'id': '',
        }
        self.access_plan = {
            'id': '',
        }
        self.customer = {
            'external_id': '',
            'name': '',
            'id': '',
        }
        self.division = {
            'external_id': '',
            'name': '',
            'id': '',
        }
        self.carrier = {
            'custom_fields': [],
            'external_id': '',
            'name': '',
            'id': '',
        }
        self.category = {
            'external_id': '',
            'name': '',
            'id': ''
        }
        self.tag = {
            'external_id': '',
            'name': '',
            'id': ''
        }
        self.notification_template = {
            'external_id': '',
            'name': '',
            'id': ''
        }
        self.order_state = {
            'external_id': '',
            'name': '',
            'id': ''
        }
        self.custom_field = {
            'field_target': '',
            'field_type': '',
            'placement': '',
            'show_always': True,
            'web_visible': True,
            'web_editable': True,
            'mobile_visible': True,
            'mobile_editable': True,
            'mobile_required_for_complete': True,
            'mobile_required_for_cancel': False,
            'id': '',
            'name': ''
        }
        self.uom = {
            'abbreviation': '',
            'external_id': '',
            'id': '',
        }
        self.good = {
            'external_id2': '',
            'article': '',
            'barcodes': [],
            'description': '',
            'is_serial': False,
            'packs': [],
            'folder': '',
            'name': '',
            'external_id': '',
            'id': '',
        }
        self.pack = {
            'id': '',
            'quantity': 0.0,
            'uom_id': '',
            'weight': 0.0,
            'volume': 0.0,
            'volume_alt': 0.0,
            'barcode': {}
        }
        self.user = {
            'login': '',
            'password': '',
            'client_code': '',
            'contact_name': '',
            'contact_phone': '',
            'carrier_id': '',
            'admin_account': False,
            'main_account': False,
            'blocked': False,
            'access_plan': '',
            'divisions': [],
            'id': ''
        }


defined = EntitiesDefinition()
