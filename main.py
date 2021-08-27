import cv2 as cv

ruta = "figura.png"
imagen = cv.imread(ruta)
alto, ancho = imagen.shape[:2]
print(alto, ancho)

r,g,b = {},{},{}

for y in range(alto):
    for x in range(ancho):
        b = imagen.item(y,x,0)
        g = imagen.item(y,x,1)
        r = imagen.item(y,x,2)
        if r>0:
            r,g,b = 255,255,255
        print(r,g,b)


# cv.imshow("imagen",imagen)
# cv.waitKey(0)
# cv.destroyAllWindows()