# 데이터 수집에 필요한 정보 ( GPT는 무엇을 모르는가 ? )
    1. URL
    2. 요소 (내가 찾고자 하는 정보)

### 사용할 프롬프트 : 

## 역할
- 당신의 세계 최고의 파이썬 데이터 수집 전문가입니다.

## 목적
- 제공된 URL과 요소를 기반으로 파이썬 데이터 수집 코드를 작성합니다.

## 요청사항
- selenium 라이브러리를 사용하세요.
- 크롬 드라이버는 이미 설치가 되어있습니다.
- Pandas를 사용해서 csv로 저장해주세요. 단, 한글 인코딩을 적용해야합니다.
- 헤드리스 모드가 아닌 일반 모드로 수집해주세요.
- print()를 적절하게 사용해서 데이터 수집이 적절하게 잘 이루어지고 있는지 보여주세요.


## 제공정보
### URL
'''
https://new.land.naver.com/complexes/112232?ms=37.395645,127.11368,17&a=APT:ABYG:JGC:PRE&e=RETAIL
'''

### 요소
'''
<div class="item   false"><div class="item_inner "><a href="javascript:void(0);" class="item_link" role="button" aria-expanded="false" data-nclk="TAA.title"><div class="item_title"><span class="icon-badge type-owner">집주인</span><span class="text">알파리움1단지(주상복합) 101동</span></div><div class="price_line"><span class="type">매매</span><span class="price">22억 5,000</span></div><div class="info_area"><p class="line"><strong class="type">아파트</strong><span class="spec">123B/96m², 10/18층, 남서향</span></p><p class="line"><span class="spec">37. 입주가능, 화랑공원뷰, 풀옵션</span></p></div></a><div class="cp_area"><div class="cp_area_inner"><span class="agent_info"><a href="javascript:void(0);" class="agent_name" data-nclk="TAA.cp">부동산뱅크 제공</a></span><span class="agent_info"><a href="javascript:void(0);" class="agent_name" data-nclk="TAA.realtor">알파삼성(단지내)공인중개사무소</a></span></div></div><div class="label_area"><span class="icon-badge type-confirmed">확인매물 25.07.10.</span></div></div><button class="btn_add_favorite" aria-pressed="false" aria-label="&quot;관심매물 추가하기&quot;" data-nclk="TAA.myarticle"><i class="icon icon_favorite" aria-hidden="true"></i></button></div>
'''