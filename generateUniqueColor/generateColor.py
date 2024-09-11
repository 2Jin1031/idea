import random

# 색상 계열에 따른 기본 Hue 값 설정
def get_hue_base(color_choice):
    hue_values = {
        'red': 0,        # 빨간색
        'orange': 30,    # 주황색
        'yellow': 60,    # 노란색
        'green': 120,    # 초록색
        'blue': 240,     # 파란색
        'navy': 210,     # 남색
        'purple': 270    # 보라색
    }
    return hue_values.get(color_choice.lower(), 120)  # 기본은 초록색

# 색상을 생성하는 함수
def generate_color(color_choice, birth_date):
    hue_base = get_hue_base(color_choice)
    
    # 생일을 숫자로 변환 (YYYYMMDD 형식)
    birth_sum = sum(int(digit) for digit in str(birth_date))
    
    # 랜덤으로 hue 조정 (각 계열별로 ±20 범위 내에서 변동)
    hue = hue_base + random.randint(-20, 20)
    
    # 생일에 따른 Saturation (채도)와 Lightness (명도) 설정
    saturation = (birth_sum % 50) + 50  # 50% ~ 100%
    lightness = (birth_sum % 30) + 40   # 40% ~ 70%
    
    return f"hsl({hue}, {saturation}%, {lightness}%)"

# 예시 실행
color_choice = 'blue'  # 사용자가 고른 색상 (파란색)
birth_date = 20031103  # 생일 예시

color = generate_color(color_choice, birth_date)
print(f"Generated Color: {color}")