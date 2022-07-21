orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

buy = orders.split(',')

s = set(orders.split(','))

menu = list(s)
menu.sort(reverse=True)

print("총 {}잔의 주문이 들어왔습니다".format(len(buy)))
print("내리차순으로 정리한 메뉴는 이렇습니다\n", menu)
