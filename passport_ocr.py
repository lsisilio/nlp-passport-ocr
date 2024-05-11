import cv2
import pytesseract
from PIL import Image

# Load passaport image
image = cv2.imread('passaport.webp', 0)  # 0 for greyscale
# Apply threshold - adjust second param
ret, thresholded = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)
# Remove noise
blurred_image = cv2.GaussianBlur(thresholded, (3, 3), 0)
 

# Define ROI - Region of Interest
# x - Upper Left
# y - Upper Left
# w - ROI width
# h - ROI height

# Last Name ROI
last_name_x, last_name_y, last_name_w, last_name_h = 235, 75, 225, 35
# First Name ROI
first_name_x, first_name_y, first_name_w, first_name_h = 230, 120, 130, 20
# Passport Number ROI
passport_number_x, passport_number_y, passport_number_w, passport_number_h = 515, 48, 100, 25
# Date of Birth ROI
date_birth_x, date_birth_y, date_birth_w, date_birth_h = 230, 175, 140, 15
# Date of Expiry ROI
date_expiry_x, date_expiry_y, date_expiry_w, date_expiry_h = 235, 345, 140, 25


# Crop the ROIs
last_name_roi   = blurred_image[last_name_y: last_name_y + last_name_h, last_name_x: last_name_x + last_name_w]
first_name_roi  = blurred_image[first_name_y: first_name_y + first_name_h, first_name_x: first_name_x + first_name_w]
passport_n_roi  = blurred_image[passport_number_y: passport_number_y + last_name_h, passport_number_x: passport_number_x + passport_number_w]
date_birth_roi  = blurred_image[date_birth_y: date_birth_y + date_birth_h, date_birth_x: date_birth_x + date_birth_w]
date_expiry_roi = blurred_image[date_expiry_y: date_expiry_y + date_expiry_h, date_expiry_x: date_expiry_x + date_expiry_w]
 
# Show the ROIs and save its images
cv2.imshow('Last Name ROI', last_name_roi)
cv2.imwrite('./roi_imgs/last_name.png', last_name_roi)
cv2.waitKey(0)
cv2.imshow('First Name ROI', first_name_roi)
cv2.imwrite('./roi_imgs/first_name.png', first_name_roi)
cv2.waitKey(0)
cv2.imshow('Passport Number ROI', passport_n_roi)
cv2.imwrite('./roi_imgs/passport_n.png', passport_n_roi)
cv2.waitKey(0)
cv2.imshow('Date of Birth ROI', date_birth_roi)
cv2.imwrite('./roi_imgs/date_birth.png', date_birth_roi)
cv2.waitKey(0)
cv2.imshow('Date of Expiry ROI', date_expiry_roi)
cv2.imwrite('./roi_imgs/date_expiry.png', date_expiry_roi)

# Load images for Tesseract and extract
im_last_name   = Image.open('./roi_imgs/last_name.png')
txt_last_name  = pytesseract.image_to_string(im_last_name, lang='por')
print(f'Last Name: {txt_last_name}')

im_first_name  = Image.open('./roi_imgs/first_name.png')
txt_first_name = pytesseract.image_to_string(im_first_name, lang='por')
print(f'First Name: {txt_first_name}')

im_passport_n  = Image.open('./roi_imgs/passport_n.png')
txt_passport_n = pytesseract.image_to_string(im_passport_n, lang='por')
print(f'Passport Number: {txt_passport_n}')

im_date_birth  = Image.open('./roi_imgs/date_birth.png')
txt_date_birth = pytesseract.image_to_string(im_date_birth, lang='por')
print(f'Date of Birth: {txt_date_birth}')

im_date_expiry = Image.open('./roi_imgs/date_expiry.png')
txt_date_expiry = pytesseract.image_to_string(im_date_expiry, lang='por')
print(f'Expiry Date: {txt_date_expiry}')

cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Draw a rectangule on the original image
cv2.rectangle(image, (last_name_x, last_name_y), (last_name_x + last_name_w, last_name_y + last_name_h), (255, 0, 255), 5)  # Green, Thickness 5
cv2.rectangle(image, (first_name_x, first_name_y), (first_name_x + first_name_w, first_name_y + first_name_h), (255, 0, 255), 5)  # Green, Thickness 5
cv2.rectangle(image, (passport_number_x, passport_number_y), (passport_number_x + passport_number_w, passport_number_y + passport_number_h), (255, 0, 255), 5)  # Green, Thickness 5
cv2.rectangle(image, (date_birth_x, date_birth_y), (date_birth_x + date_birth_w, date_birth_y + date_birth_h), (255, 0, 255), 5)  # Green, Thickness 5
cv2.rectangle(image, (date_expiry_x, date_expiry_y), (date_expiry_x + date_expiry_w, date_expiry_y + date_expiry_h), (255, 0, 255), 5)  # Green, Thickness 5

# Original image with ROI
cv2.imshow('Original image with ROIs', image)
cv2.waitKey(0)
cv2.destroyAllWindows()