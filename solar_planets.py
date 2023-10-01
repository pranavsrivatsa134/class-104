import cv2

cv2.imread("solar-systen.jpg")
cv2.imshow("output",img)

cv2.putText(img,
            "Sun"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,300,255)
            )

cv2.putText(img,
            "Venus"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,355,255)
            )

cv2.putText(img,
            "Earth"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,425,255)
            )

cv2.putText(img,
            "Mars"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,475,255)
            )

cv2.putText(img,
            "Jupiter"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,255)
            )

cv2.putText(img,
            "Saturn"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,625,255)
            )

cv2.putText(img,
            "Uranus"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,675,255)
            )

cv2.putText(img,
            "Neptune"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,755,255)
            )

cv2.imwrite("Solar_systemwithname.jpg",img)
