import numpy as np,cv2

image = cv2.imread('c/Users/010/Desktop/opencv/bit_test.jpg')
logo = cv2.imread('c/Users/010/Desktop/opencv/logo.jpg')

# if image is None or logo is None:raise Exception("영상파일 읽기 오류")

masks = cv2.threshold(logo,220,255,cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0],masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2],fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H,W) , (h,w) = image.shape[:2], logo.shape[:2]

x,y = (W-w)//2, (H-h)//2
roi = image[y:y+h, x:x+w]

#행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foregrouond = cv2.bitwise_and(logo,logo, mask = fg_pass_mask)
background = cv2.bitwise_and(roi, roi, mask = bg_pass_mask)

dst = cv2.add(background,foregrouond)
image[y:y+h,x:x+w] = dst

cv2.imshow('background', background); cv2.imshow('forground', foregrouond)
cv2.imshow('dst',dst); cv2.imshow('image',image)
cv2.waitKey()