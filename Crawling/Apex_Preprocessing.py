# 1차 전처리를 통해 상위 키워드를 추출
# 상위 키워드를 가지고 2차 전처리 실행
# 단어가 상위 키워드의 어간을 포함하는 경우 동일하게 취급



f = open("Apex_legend_DATA.txt", 'w', encoding='utf-8')
Apex_file = open("Apex_legend_inven.txt", 'r', encoding='utf-8')
Apex_list = []
Apex_list2 = []

for a in Apex_file:
    a = a.strip()
    a = a.split(' ')
    a = a[1:]                           # 첫번째 워드가 에러로 인해서 무의미한 데이터가 입력됨
    
    for b in a:
        Apex_list.append(b)

# 1차 전처리
for k, c in enumerate(Apex_list):
    if c == ',':
        continue
    elif c == ' ':
        continue
    elif '...' in c:
        c =c.replace('...', '')
        Apex_list2.append(c)
    elif '..' in c:
        c = c.replace('..', '')
        Apex_list2.append(c)
    elif '.' in c:
        c = c.replace('.', '')
        Apex_list2.append(c)
    elif '?' in c:
        c = c.replace('?', '')
        Apex_list2.append(c)
    elif '??' in c:
        c = c.replace('??', '')
        Apex_list2.append(c)
    elif '???' in c:
        c = c.replace('???', '')
        Apex_list2.append(c)
    elif ',' in c:
        c = c.replace(',', '')
        Apex_list2.append(c)
    elif ',,' in c:
        c = c.replace(',,', '')
        Apex_list2.append(c)
    elif ',,,' in c:
        c = c.replace(',,,', '')
        Apex_list2.append(c)
    elif '~' in c:
        c = c.replace('~','')
        Apex_list2.append(c)
    elif '에펙' in c:
        c = '에이펙스'
        Apex_list2.append(c)
    else:
        Apex_list2.append(c)

Apex_upper = []
for a in Apex_list2:
    a = a.upper()
    Apex_upper.append(a)


# 2차 전처리
Apex_list3 = []
for a in Apex_upper:
    if '윙맨' in a:
        a = '윙맨'
        Apex_list3.append(a)
    elif '파티' in a:
        a = '파티'
        Apex_list3.append(a)
    elif '스쿼드' in a:
        a = '스쿼드'
        Apex_list3.append(a)
    elif '핵' in a:
        a = '핵'
        Apex_list3.append(a)
    elif '베그' in a:
        a = '배틀그라운드'
        Apex_list3.append(a)
    elif '배그' in a:
        a = '배틀그라운드'
        Apex_list3.append(a)
    elif '패파' in a:
        a = '패스파인더'
        Apex_list3.append(a)
    elif '코스틱' in a:
        a = '코스틱'
        Apex_list3.append(a)
    elif '라라' in a:
        a = '라이프라인'
        Apex_list3.append(a)
    elif '피스키퍼' in a:
        a = '피스키퍼'
        Apex_list3.append(a)
    elif '버그' in a:
        a = '버그'
        Apex_list3.append(a)
    elif '프레임' in a:
        a = '프레임'
        Apex_list3.append(a)

    elif '방송' in a:
        a = '방송'
        Apex_list3.append(a)
    elif '에펙' in a:
        a = 'APEX'
        Apex_list3.append(a)
    elif '에이펙스' in a:
        a = 'APEX'
        Apex_list3.append(a)
    elif '모잠' in a:
        a = '모잠비크'
        Apex_list3.append(a)
    elif '모잠비크' in a:
        a = '모잠비크'
        Apex_list3.append(a)
    elif '지브롤터' in a:
        a = '지브롤터'
        Apex_list3.append(a)
    elif '레이스' in a:
        a = '레이스'
        Apex_list3.append(a)
    elif '방갈' in a:
        a = '방갈로르'
        Apex_list3.append(a)
    elif 'VPN' in a:
        a = 'VPN'
        Apex_list3.append(a)
    elif '초보' in a:
        a = '초보'
        Apex_list3.append(a)
    elif '차단' in a:
        a = '차단'
        Apex_list3.append(a)
    elif '피방' in a:
        a = 'PC방'
        Apex_list3.append(a)
    elif '스트리머' in a:
        a = '스트리머'
        Apex_list3.append(a)
    elif '트위치' in a:
        a = '트위치'
        Apex_list3.append(a)
    elif '너프' in a:
        a = '너프'
        Apex_list3.append(a)
    elif '버프' in a:
        a = '버프'
        Apex_list3.append(a)
    elif '스킨' in a:
        a = '스킨'
        Apex_list3.append(a)
    elif '퍼블리싱' in a:
        a = '퍼블리싱'
        Apex_list3.append(a)
    elif '업뎃' in a:
        a = '업데이트'
        Apex_list3.append(a)
    elif '업데이트' in a:
        a = '업데이트'
        Apex_list3.append(a)
    elif '패치' in a:
        a = '패치'
        Apex_list3.append(a)
    elif '치킨' in a:
        a = '치킨'
        Apex_list3.append(a)
    elif '갓겜' in a:
        a = '갓겜'
        Apex_list3.append(a)
    elif '팅' in a:
        a = '팅김'
        Apex_list3.append(a)
    elif '디코' in a:
        a = '디스코드'
        Apex_list3.append(a)
    elif '디스코드' in a:
        a = '디스코드'
        Apex_list3.append(a)
    elif '렉' in a:
        a = '렉'
        Apex_list3.append(a)
    elif '욕' in a:
        a = '욕'
        Apex_list3.append(a)
    elif '밸런스' in a:
        a = '밸런스'
        Apex_list3.append(a)
    elif '수리검' in a:
        a = '수리검'
        Apex_list3.append(a)
    elif a == ' ':
        continue
    elif a == ',':
        continue
    elif '고인물' in a:
        a = '고인물'
        Apex_list3.append(a)
    elif '실드' in a:
        a = '쉴드'
        Apex_list3.append(a)
    elif '쉴드' in a:
        a = '쉴드'
        Apex_list3.append(a)
    elif '넥슨' in a:
        a = '넥슨'
        Apex_list3.append(a)
    elif '무료' in a:
        a = '무료'
        Apex_list3.append(a)
    elif '튕' in a:
        a = '팅김'
        Apex_list3.append(a)
    elif '오류' in a:
        a = '오류'
        Apex_list3.append(a)
    elif '심의' in a:
        a = '심의'
        Apex_list3.append(a)
    elif '쿠나이' in a:
        a = '수리검'
        Apex_list3.append(a)
    #
    elif '레벨' in a:
        a = '레벨'
        Apex_list3.append(a)
    elif '재미' in a:
        a = '재밌다'
        Apex_list3.append(a)
    elif '재밌' in a:
        a = '재밌다'
        Apex_list3.append(a)
    elif '오리진' in a:
        a = '오리진'
        Apex_list3.append(a)
    elif '국내' in a:
        a = '국내'
        Apex_list3.append(a)
    elif '챔피언' in a:
        a = '챔피언'
        Apex_list3.append(a)
    elif '분대' in a:
        a = '분대'
        Apex_list3.append(a)
    elif '캐릭' in a:
        a = '캐릭터'
        Apex_list3.append(a)
    elif '게임' in a:
        a = '게임'
        Apex_list3.append(a)
    elif '공지' in a:
        a = '공지'
        Apex_list3.append(a)

    elif '헴록' in a:
        a = '헴록'
        Apex_list3.append(a)
    elif '햄록' in a:
        a = '헴록'
        Apex_list3.append(a)
    elif '우승' in a:
        a = '우승'
        Apex_list3.append(a)
    elif '총' in a:
        a = '총'
        Apex_list3.append(a)
    elif '축하' in a:
        a = '축하'
        Apex_list3.append(a)
    elif 'ㅊㅋ' in a:
        a = '축하'
        Apex_list3.append(a)
    elif '환불' in a:
        a = '환불'
        Apex_list3.append(a)
    elif 'ㅋㅋ' in a:
        a = 'ㅋㅋ'
        Apex_list3.append(a)
        #
    elif '오픈' in a:
        a = '오픈'
        Apex_list3.append(a)
    elif '카드' in a:
        a = '카드'
        Apex_list3.append(a)
    elif '성인' in a:
        a = '성인'
        Apex_list3.append(a)
    elif '뉴비' in a:
        a = '뉴비'
        Apex_list3.append(a)
    elif '시작' in a:
        a = '시작'
        Apex_list3.append(a)
    #
    elif '총' in a:
        a = '총'
        Apex_list3.append(a)
    elif '축하' in a:
        a = '축하'
        Apex_list3.append(a)
    elif 'ㅊㅋ' in a:
        a = '축하'
        Apex_list3.append(a)
    elif '환불' in a:
        a = '환불'
        Apex_list3.append(a)
    elif 'ㅋㅋ' in a:
        a = 'ㅋㅋ'
        Apex_list3.append(a)
        #
    elif '착륙' in a:
        a = '착륙'
        Apex_list3.append(a)
    elif '픽' in a:
        a = '픽'
        Apex_list3.append(a)
    elif '성인' in a:
        a = '성인'
        Apex_list3.append(a)
    elif '방법' in a:
        a = '방법'
        Apex_list3.append(a)
    elif '결제' in a:
        a = '결제'
        Apex_list3.append(a)
    elif '우회' in a:
        a = '우회'
        Apex_list3.append(a)
    #
    elif '관전' in a:
        a = '관전'
        Apex_list3.append(a)
    elif '보상' in a:
        a = '보상'
        Apex_list3.append(a)
    elif '방법' in a:
        a = '방법'
        Apex_list3.append(a)
    elif '플레이' in a:
        a = '플레이'
        Apex_list3.append(a)
    elif '사용자' in a:
        a = '사용자'
        Apex_list3.append(a)
    #
    elif '팀' in a:
        a = '팀'
        Apex_list3.append(a)
    elif '보상' in a:
        a = '보상'
        Apex_list3.append(a)
    elif '방법' in a:
        a = '방법'
        Apex_list3.append(a)
    elif '플레이' in a:
        a = '플레이'
        Apex_list3.append(a)
    elif '사용자' in a:
        a = '사용자'
        Apex_list3.append(a)
    elif '인스펙터' in a:
        a = '인스펙터'
        Apex_list3.append(a)
    elif '플랫라인' in a:
        a = '플랫라인'
        Apex_list3.append(a)
    elif '옵치' in a:
        a = '오버워치'
        Apex_list3.append(a)
    elif '오버워치' in a:
        a = '오버워치'
        Apex_list3.append(a)
    elif '겜' in a:
        a = '게임'
        Apex_list3.append(a)
    elif '유튭' in a:
        a = '유튜브'
        Apex_list3.append(a)
    elif '유튜브' in a:
        a = '유튜브'
        Apex_list3.append(a)
    elif '파밍' in a:
        a = '파밍'
        Apex_list3.append(a)
    elif '설정' in a:
        a = '설정'
        Apex_list3.append(a)
    elif '포나' in a:
        a = '포트나이트'
        Apex_list3.append(a)
    elif '친추' in a:
        a = '친구추가'
        Apex_list3.append(a)
    elif '타이탄폴' in a:
        a = '타이탄폴'
        Apex_list3.append(a)
    elif '점검' in a:
        a = '점검'
        Apex_list3.append(a)
    elif '외국' in a:
        a = '외국'
        Apex_list3.append(a)
    elif 'EA' in a:
        a = 'EA'
        Apex_list3.append(a)
    elif '패스파' in a:
        a = '패스파인더'
        Apex_list3.append(a)
    elif '슈라우드' in a:
        a = '슈라우드'
        Apex_list3.append(a)
    elif '유튜버' in a:
        a = '유튜버'
        Apex_list3.append(a)
    elif '매너' in a:
        a = '매너'
        Apex_list3.append(a)
    elif '정발' in a:
        a = '정발'
        Apex_list3.append(a)
    elif '실행' in a:
        a = '실행'
        Apex_list3.append(a)

    elif '상자' in a:
        a = '상자'
        Apex_list3.append(a)
    elif '서버' in a:
        a = '서버'
        Apex_list3.append(a)
    elif '망' in a:
        a = '망함'
        Apex_list3.append(a)
    elif '1등' in a:
        a = '1등'
        Apex_list3.append(a)
    elif 'GTX' in a:
        a = 'GTX'
        Apex_list3.append(a)
    elif '씨발' in a:
        a = '욕설'
        Apex_list3.append(a)
    elif '존나' in a:
        a = '욕설2'
        Apex_list3.append(a)
    else:
        Apex_list3.append(a)

Apex_dict = {}

for a in Apex_list3:
    if a in Apex_dict:
        Apex_dict[a] += 1
    else:
        Apex_dict[a] = 1

for a in Apex_dict:
    f.write(str(a) + ',' + str(Apex_dict[a]) + '\n')

print(Apex_list)
print(Apex_list3)
print(len(Apex_dict))

Apex_file.close()