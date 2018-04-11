import os

import cv2
import numpy as np
import matplotlib.pyplot as plt



#Directorio de las imágenes
directorio = 'C://Users//Mik//Desktop//The Open Bacteria Project//img'
for image in os.listdir(directorio):
    #Cargamos la imagen en blanco y negro y un reescalado
    path= os.path.join(directorio, image)
    img= cv2.imread(path, 0)
    img = cv2.resize(img, (0,0), fx=0.1, fy=0.1) 
    img1 = img.copy() #Copia de la imagen
    #Emborronamos la imagen para quitarle ruido
    img = cv2.medianBlur(img,5)
    
    img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
    #Usamos la transformada de Hough para detectar la placa de petri
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,200,
                                param1=150,param2=100,minRadius=70,maxRadius=0)
    
    circles = np.uint16(np.around(circles))
    
    
    #Dibujamos la circunferencia de la placa
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img1,(i[0],i[1]),i[2],(255,0,0),2)
        x, y = i[0], i[1]
        r = i[2]- 30 #reducimos el radio para quedarnos con el interior de la placa
    
    
    #Recortamos la imagen quedándonos con la placa de Petri
    height,width = img.shape
    mask = np.zeros((height,width), np.uint8)
    cv2.circle(mask,(x,y),r,(255,255,255),thickness=-1)
    masked_data = cv2.bitwise_and(img1, img1, mask=mask)
    _,thresh = cv2.threshold(mask,1,255,cv2.THRESH_BINARY)
    contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    x,y,w,h = cv2.boundingRect(contours[0])
    crop = masked_data[y:y+h,x:x+w]
    
    
    #Umbralizamos la imagen para obtener las bacterias
    umbral = 165
    crop_umbral=crop.copy()
    crop_umbral[crop>umbral]=255
    crop_umbral[crop<=umbral]=0
    
    #Calculamos el área que ocupa la poblacion sabiendo que la placa tiene de diámetro 9cm
    area_per_pixel = (9/crop.shape[0])**2
    norm = crop_umbral/255
    area = norm.sum() * area_per_pixel

    
    # display results
        
    plt.imshow(img1)
    plt.show()
    
    
    plt.figure()
    ax = plt.subplot("221")
    ax.set_title("Placa de Petri")
    ax.imshow(crop)
    
    ax = plt.subplot("222")
    ax.set_title("El área ocupada es: %f $cm^{2}$" %(area))
    ax.imshow(crop_umbral)
    plt.tight_layout()
    plt.show()
