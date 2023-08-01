import cv2
import numpy as np

# 변수 초기화
drawing = False  # 마우스가 클릭된 상태 확인
mode = True  # True이면 사각형을 그림, False이면 원을 그림
start_x, start_y = -1, -1
color = (0, 255, 0)  # 초기 색상은 초록색 (BGR 형식)
thickness = -1  # 초기 두께는 내부를 채움

# 마우스 이벤트 콜백 함수
def draw_shape(event, x, y, flags, param):
    global start_x, start_y, drawing, mode, color, thickness

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(image, (start_x, start_y), (x, y), color, thickness)
        else:
            cv2.circle(image, (x, y), int(np.sqrt((x - start_x) ** 2 + (y - start_y) ** 2)), color, thickness)
        label_shape(x, y)

# 라벨링 함수
def label_shape(x, y):
    shape_type = 'Rectangle' if mode else 'Circle'
    color_name = get_color_name(color)

    label = f'{shape_type} - {color_name}'
    cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# 색상 이름 반환 함수
def get_color_name(color):
    color_names = {
        (0, 255, 0): 'Green',
        (0, 0, 255): 'Red',
        (255, 0, 0): 'Blue',
        (255, 255, 255): 'White'
    }
    return color_names.get(color, 'Unknown')

# 검은 배경 이미지 생성
width, height = 1000, 1000
image = np.zeros((height, width, 3), dtype=np.uint8)

# OpenCV 창 생성 및 이벤트 콜백 설정
cv2.namedWindow('Drawing')
cv2.setMouseCallback('Drawing', draw_shape)

while True:
    cv2.imshow('Drawing', image)

    # 키보드 입력 처리
    key = cv2.waitKey(1)
    if key == ord('m'):
        mode = not mode
        image = np.zeros((height, width, 3), dtype=np.uint8)
    elif key == ord('g'):
        color = (0, 255, 0)  # 초록색 (Green)
    elif key == ord('r'):
        color = (0, 0, 255)  # 빨간색 (Red)
    elif key == ord('b'):
        color = (255, 0, 0)  # 파란색 (Blue)
    elif key == ord('w'):
        color = (255, 255, 255)  # 흰색 (White)
    elif key == ord('1'):
        thickness = -1  # 내부를 채우는 두께
    elif key == ord('2'):
        thickness = 1  # 두께 1

    # 'q' 키를 누르면 종료합니다.
    elif key == ord('q'):
        break

cv2.destroyAllWindows()