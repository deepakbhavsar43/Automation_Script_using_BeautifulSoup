import cv2

# reading the image
image = cv2.imread("bill.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 140, 255)
# cv2.imshow("Edges", gray)
# cv2.waitKey(0)

# applying closing function
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("Closed", gray)
# cv2.waitKey(0)

# finding_contours
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    cv2.drawContours(gray, [approx], -1, (0, 255, 0), 2)
cv2.imshow("Output", gray)
cv2.waitKey(0)