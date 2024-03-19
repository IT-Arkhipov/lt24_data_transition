import random
from typing import Union

from lib import dataset, convert
from lib.api import api_request
from lib.definition import endpoint, Endpoints, defined
from lib.logger import logger


def get_entities(entity_endpoint: Union[Endpoints, str], params: dict = None) -> Union[dict, list]:
    response = api_request.get(endpoint=entity_endpoint, params=params)
    api_request.assert_response(response)
    return response.json()


def access_plans() -> list:
    logger.log.info('Запрос списка планов доступа')
    return get_entities(endpoint.get_access_plans_list).get('plans')


def carriers() -> list:
    logger.log.info('Запрос списка перевозчиков')
    return get_entities(endpoint.get_carriers_list).get('carriers')


def categories() -> list:
    logger.log.info('Запрос списка категорий заказа')
    return get_entities(endpoint.get_categories_list).get('categories')


def custom_fields() -> list:
    logger.log.info('Запрос списка пользовательских полей')
    return get_entities(endpoint.get_custom_fields_list).get('custom_fields')


def custom_fields_view() -> dict:
    logger.log.info('Запрос списка пользовательских полей')
    return get_entities(endpoint.get_custom_fields_view)


def customer(object_id: str) -> dict:
    logger.log.info(f'Запрос контрагента {object_id}')
    _objects = customers()
    for _object in _objects:
        if _object.get('id') == object_id:
            return _object
    return {}


def customers() -> list:
    logger.log.info('Запрос списка контрагентов')
    return get_entities(endpoint.get_customers_list).get('customers')


def countries() -> list:
    logger.log.info('Запрос списка категорий заказа')
    return get_entities(endpoint.get_countries_list).get('countries')


def division(object_id: str) -> dict:
    logger.log.info(f'Запрос подразделения {object_id}')
    _objects = divisions()
    for _object in _objects:
        if _object.get('id') == object_id:
            return _object
    return {}


def divisions() -> list:
    logger.log.info('Запрос списка подразделений')
    return get_entities(endpoint.get_divisions_list).get('divisions')


def driver(object_id: str) -> dict:
    logger.log.info(f'Запрос водителя {object_id}')
    params = {'id': object_id}
    _object = get_entities(endpoint.get_drivers_list, params=params).get('drivers')
    return _object[0] if _object else {}


def drivers() -> list:
    logger.log.info('Запрос списка водителей')
    return get_entities(endpoint.get_drivers_list).get('drivers')


def good(object_id: str) -> dict:
    logger.log.info(f'Запрос товара {object_id}')
    _objects = goods()
    for _object in _objects:
        if _object.get('id') == object_id:
            return _object
    return {}


def goods() -> list:
    logger.log.info(f'Запрос списка товаров')
    return get_entities(endpoint.get_goods_list).get('goods')


def notification_template(object_id: str) -> dict:
    logger.log.info(f'Запрос подразделения {object_id}')
    _objects = notification_templates()
    for _object in _objects:
        if _object.get('id') == object_id:
            return _object
    return {}


def notification_templates() -> list:
    logger.log.info('Запрос списка шаблона уведомлений')
    return get_entities(endpoint.get_notification_templates_list).get('templates')


def order(object_id: str) -> dict:
    logger.log.info('Запрос заказа')
    params = {'id': object_id}
    _object = get_entities(endpoint.get_orders_list, params=params)
    return _object[0] if _object else {}


def orders(start_date: str, end_date: str) -> list:
    logger.log.info('Запрос списка заказов')
    params = {'date': [start_date, end_date]}
    return get_entities(endpoint.get_orders_list, params=params)


def orders_scroll(start_date: str, end_date: str) -> list:
    logger.log.info('Запрос набора данных для грида заказов')
    params = {'date': [start_date, end_date]}
    return get_entities(endpoint.get_orders_scroll, params=params).get('orders')


def order_states() -> list:
    logger.log.info('Запрос списка типов состояния заказа')
    return get_entities(endpoint.get_order_states_list).get('states')


def packs() -> list:
    logger.log.info('Запрос списка упаковок')
    return get_entities(endpoint.get_packs_list).get('packs')


def presets(group_name: str) -> list:
    logger.log.info('Запрос списка пресетов')
    return get_entities(f"{endpoint.get_presets}/{group_name}")


def route(object_id: str) -> dict:
    logger.log.info(f'Запрос рейса {object_id}')
    params = {
        'id': object_id,
        'tracks': defined.route.get('tracks', True)
    }
    _object = get_entities(endpoint.get_routes_list, params=params).get('routes')
    return _object[0] if _object else {}


def routes(start_date: str, end_date: str) -> list:
    logger.log.info('Запрос списка рейсов')
    params = {'date': [start_date, end_date]}
    return get_entities(endpoint.get_routes_list, params=params).get('routes')


def tags() -> list:
    logger.log.info('Запрос списка тегов')
    return get_entities(endpoint.get_tags_list).get('tags')


def uoms() -> list:
    logger.log.info(f'Запрос списка единиц измерения')
    return get_entities(endpoint.get_uoms_list).get('uoms')


def users() -> list:
    logger.log.info('Запрос списка пользователей')
    return get_entities(endpoint.get_users_list).get('users')


def vehicle(vehicle_id: str) -> dict:
    logger.log.info('Запрос транспорта по id')
    params = {'id': vehicle_id}
    _object = get_entities(endpoint.get_vehicles_list, params=params).get('vehicles')
    return _object[0] if _object else {}


def vehicles() -> list:
    logger.log.info('Запрос списка транспорта')
    return get_entities(endpoint.get_vehicles_list).get('vehicles')


def vehicle_brands() -> list:
    logger.log.info('Запрос списка марок транспорта')
    return get_entities(endpoint.get_vehicle_brands_list).get('brands')


def warehouse(object_id: str) -> dict:
    logger.log.info(f'Запрос склада {object_id}')
    _objects = warehouses()
    for _object in _objects:
        if _object.get('id') == object_id:
            return _object
    return {}


def warehouses() -> list:
    logger.log.info('Запрос списка складов')
    return get_entities(endpoint.get_warehouses_list).get('warehouses')


def zone(object_id: str) -> dict:
    logger.log.info(f'Запрос зоны {object_id}')
    _objects = zones()
    for _object in _objects:
        if _object.get('id') == object_id:
            return _object
    return {}


def zones() -> list:
    logger.log.info('Запрос списка зон')
    return get_entities(endpoint.get_zones_list).get('zones')


def assigned_orders_ids() -> list:
    logger.log.info('Запрос списка назначенных заказов')
    _routes = routes(*dataset.ALL_DATES)
    assigned_routes_ids = []
    for _route in _routes:
        for point in _route.get('points'):
            if isinstance(point.get('order_ids'), list):
                assigned_routes_ids.extend(point.get('order_ids'))
    return list(set(assigned_routes_ids))


def unassigned_order_id() -> str:
    _unassigned_orders_ids = unassigned_orders_ids()
    return random.choice(_unassigned_orders_ids) if _unassigned_orders_ids else ''


def unassigned_orders_ids() -> list:
    logger.log.info('Запрос списка неназначенных заказов')
    _assigned_orders_ids = assigned_orders_ids()
    _orders = orders(*dataset.ALL_DATES)
    _orders_ids = []
    for _order in _orders:
        _orders_ids.append(_order.get('id'))
    _unassigned_orders_ids = [order_id for order_id in _orders_ids if order_id not in _assigned_orders_ids]
    return list(set(_unassigned_orders_ids))


def route_orders_ids(_route) -> list:
    logger.log.info('Запрос списка назначенных на рейс заказов')
    route_points = _route.get('points')
    orders_list = []
    for point in route_points:
        if point.get('order_ids') is not None:
            for order_ids in point.get('order_ids'):
                orders_list.append(order_ids)
    return orders_list


def orders_position_in_route(_route: dict) -> dict:
    logger.log.info('Запрос списка назначенных на рейс заказов')
    if _route is None:
        return {}
    route_orders = {}
    _orders = route_orders_ids(_route)
    for _order in _orders:
        route_orders[_order] = {
            'loading': 999,
            'unloading': -1
        }
    for i in range(len(_route.get('points'))):
        if _route.get('points')[i]['action'] in ("loading", "pickup"):
            for order_id in _route.get('points')[i].get('order_ids'):
                route_orders[order_id]['loading'] = i
        if _route.get('points')[i]['action'] in ("unloading", "drop"):
            for order_id in _route.get('points')[i].get('order_ids'):
                route_orders[order_id]['unloading'] = i
    return route_orders


def entities_ids(entities: list) -> list:
    _ids = []
    for entity in entities:
        _ids.append(entity.get('id'))
    return _ids


def entities_key_value(entities: list, key: str) -> list:
    values = []
    for entity in entities:
        values.append(entity.get(key))
    return values


def orders_from_scope_planning(date_time: str, division: list) -> list:
    params = {
        'date': convert.ymd_to_dmy(date_time)[:10],
        'division': division
    }
    _orders = get_entities(endpoint.get_planning_scope, params=params).get('orders')
    return _orders
