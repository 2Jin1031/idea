import datetime
import json

data = [
    (1, 627000, 1, '시설사용료', '2023-11-15 05:30:00', 1),
    (2, 15000, 1, '장례용품', '2023-11-15 05:45:00', 1),
    (3, 110000, 1, '시설사용료', '2023-11-15 06:30:00', 1),
    (4, 510000, 1, '제사음식비', '2023-11-15 06:45:00', 1),
    (5, 382000, 1, '장례용품', '2023-11-15 07:10:00', 1),
    (6, 20000, 2, '조문식사', '2023-11-15 11:15:00', 1),
    (7, 30000, 3, '조문식사', '2023-11-15 11:17:00', 1),
    (8, 35000, 3, '조문식사', '2023-11-15 11:23:00', 1),
    (9, 10000, 1, '조문식사', '2023-11-15 11:25:00', 1),
    (10, 10000, 1, '조문식사', '2023-11-15 12:44:00', 1),
    (11, 30000, 3, '조문식사', '2023-11-15 13:11:00', 1),
    (12, 20000, 2, '조문식사', '2023-11-15 13:44:00', 1),
    (13, 20000, 2, '조문식사', '2023-11-15 14:30:00', 1),
    (14, 35000, 3, '조문식사', '2023-11-15 15:12:00', 1),
    (15, 10000, 1, '조문식사', '2023-11-15 15:40:00', 1),
    (16, 40000, 3, '조문식사', '2023-11-15 16:15:00', 1),
    (17, 10000, 1, '조문식사', '2023-11-15 16:40:00', 1),
    (18, 30000, 3, '조문식사', '2023-11-15 17:23:00', 1),
    (19, 40000, 4, '조문식사', '2023-11-15 17:25:00', 1),
    (20, 20000, 2, '조문식사', '2023-11-15 17:44:00', 1),
    (21, 20000, 1, '조문식사', '2023-11-15 18:52:00', 1),
    (22, 20000, 2, '조문식사', '2023-11-15 18:10:00', 1),
    (23, 25000, 2, '조문식사', '2023-11-15 18:30:00', 1),
    (26, 25000, 2, '조문식사', '2023-11-15 20:00:00', 1),
    (27, 20000, 1, '조문식사', '2023-11-15 20:45:00', 1),
    (28, 20000, 2, '조문식사', '2023-11-15 21:30:00', 1),
    (29, 30000, 2, '조문식사', '2023-11-15 22:15:00', 1),
    (30, 10000, 1, '조문식사', '2023-11-15 23:00:00', 1)
]

transformed_data = []

idx = 0

for record in data:
    id, cost, count, item_type, use_time, account_book_id = record

    # 조건에 따라 itemType을 결정
    if '식사' in item_type:
        item_type = '식사'
    elif '장례용품' in item_type:
        item_type = '장례용품'
    elif '장묘시설' in item_type:
        item_type = '장묘시설'

    # use_time을 datetime 형식으로 변환
    use_time = datetime.datetime.strptime(use_time, '%Y-%m-%d %H:%M:%S').isoformat()

    transformed_data.append({
        "itemType": item_type,
        "cost": cost,
        "count": count,
        "useTime": use_time
    })
    #print(idx)
    #print('{"itemType": "' + item_type + '", "cost": ' + str(cost) + ', "count": ' + str(count) + ', "useTime": "' + use_time + '"}')
    idx += 1;
    print('(' + str(cost) + ', ' + str(count) + ", '" + item_type + "', '" + use_time + "', " + str(account_book_id) + "),")



'''
for record in transformed_data:
    print(record);
'''

'''
# 전체 합계 계산
total_cost = sum(record['cost'] for record in transformed_data)
total_count = sum(record['count'] for record in transformed_data)

# 최종 결과 생성
result = {
    "itemType": "식사",  # 원하는 형식에 맞추어 적절한 값을 선택
    "cost": total_cost,
    "count": total_count,
    "useTime": transformed_data[-1]['useTime']  # 마지막 레코드의 useTime 사용
}

# JSON 형식으로 변환
json_result = json.dumps(result, indent=2)
print(json_result)
'''