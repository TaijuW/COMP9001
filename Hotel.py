import sys
import json
import requests
import uuid
from datetime import datetime

def gen_uuid():
    return str(uuid.uuid4())

def main(argv):
    if len(argv) != 2:
        print('argv is too short.')
        return

    token_arg = argv[0]
    token = gen_uuid()

    try:
        conditions = json.loads(argv[1])
    except json.JSONDecodeError:
        print('Invalid input')
        return

    try:
        checkin_date = datetime.strptime(conditions['checkin'], '%Y-%m-%d')
        checkout_date = datetime.strptime(conditions['checkout'], '%Y-%m-%d')
        if checkin_date >= checkout_date:
            print('checkin_date must be before checkout_date')
            return
    except Exception as e:
        print('Invalid date format: {}'.format(e))
        return

    days = (checkout_date - checkin_date).days
    ppl = conditions['number']

    search_url = 'https://challenge-server.tracks.run/hotel-reservation/hotels'
    headers = {'X-ACCESS-TOKEN': token}
    params = {
        'keyword': conditions.get('keyword', ''),
        'number': ppl
    }

    if 'condition' in conditions:
        for cond in conditions['condition']:
            params.setdefault('condtion', []).append(cond)

    res = requests.get(
        'https://challenge-server.tracks.run/hotel-reservation/hotels',
        headers = headers,
        params = params
    )

    hotels = res.json()

    cheapest = None
    for hotel in hotels:
        for room in hotel['rooms']:
            if 'plans' not in room:
                continue
            for plan in room['plans']:
                total = plan['price'] * ppl * days
                plan_info = {
                    'plan_id': plan['id'],
                    'total_price': total,
                    'hotel_name': hotel['name'],
                    'room_name': room['name'],
                    'plan_name': plan['name']
                }
                if (cheapest is None or total < cheapest['total_price'] or (total == cheapest['total_price'] and plan['id'] < cheapest['plan_id'])):
                    cheapest = plan_info

    if cheapest is None:
        print('Plan not found.')
        return

    reserve_url = 'https://challenge-server.tracks.run/hotel-reservation/reservations'
    reservation_headers = {
        'X-ACCESS-TOKEN': token,
        'Content-Type': 'application/json'
    }
    reserve_body = {
        'checkin': condisions['checkin'],
        'checkout': conditions['checkout'],
        'plan_id': cheapest['plan_id'],
        'number': ppl
    }

    reserve_res = requests.post(reserve_url, headers=reserve_headers, json=reserve_body)

    if reserve_res.status_code == 200:
        data = reserve_res.json()
        print('The cheapest plan has been successfully reserved.')
        print('- hotel name: {}'.format(cheapest['hotel_name']))
        print('- room name: {}'.format(cheapest['room_name']))
        print('- plan name: {}'.format(cheapest['plan_name']))
        print('- total price: {}'.format(cheapest['total_price']))
    else:
        print('The cheapest plan is fully booked.')

if __name__ == '__main__':
    main(sys.argv[1:])