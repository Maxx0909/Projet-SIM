import numpy as np
from graphicPipeline import GraphicPipeline
from camera import Camera
from projection import Projection
from readply import readply
import matplotlib.pyplot as plt


  #définition de la taille de l'image

width = 1280  
height = 720


  #Création des trois pipelines

pipeline1 = GraphicPipeline(width,height)
pipeline2 = GraphicPipeline(width,height)
pipeline3 = GraphicPipeline(width,height)


  #Création de la caméra

#Positionnement de la caméra en X à trois mètres de l'origine
cameraPosition = np.array([3.0, 0.0, 0.0]) 

lookAt = np.array([0.0, 0.0, 0.0]) - cameraPosition
lookAt = lookAt / np.linalg.norm(lookAt)

up = np.array([0, 1, 0])

#Calcul du vecteur right
right = np.cross(up, lookAt)
#Normalisation du vecteur
right /= np.linalg.norm(right)

cam = Camera(cameraPosition, lookAt, up, right)


  #Definition de la projection

nearPlane = 0.1
farPlane = 10.0
fov = 1.91986
aspectRatio = width/height

proj = Projection(nearPlane ,farPlane,fov, aspectRatio) 


  #Définition de la position de la lumière

#On placa la lumière derrière la caméra pour voir tout l'objet
light_offset = lookAt * -0.5 
lightPosition = cameraPosition + light_offset


  #Lecture des trois fichiers pour les cubes

vertices, triangles = readply('img/cube1.ply')
vertices2, triangles2 = readply('img/cube2.ply')
vertices3, triangles3 = readply('img/cube3.ply')

data = dict([
  ('viewMatrix',cam.getMatrix()),
  ('projMatrix',proj.getMatrix()),
  ('cameraPosition',cameraPosition),
  ('lightPosition',lightPosition),
])


  #Définition des valeurs des alphas

# Les valeurs des alphas sont comprises entre 0 et 1 : plus alpha est proche de 0, plus l'objet est transparent
alpha1 = 0.5
alpha2 = 0.5
alpha3 = 0.5


  #Création des différents cubes

#Création du cube 1
r = 255
v = 0
b = 0
color = np.array([r/255, v/255, b/255])
pipeline1.draw(vertices, triangles, data, alpha1, color, True)

#Création du cube 2
r = 0
v = 255
b = 0
color = np.array([r/255, v/255, b/255])
pipeline2.draw(vertices2, triangles2, data, alpha2, color, True)

#Création du cube 3
r = 0
v = 0
b = 255
color = np.array([r/255, v/255, b/255])
pipeline3.draw(vertices3, triangles3, data, alpha3, color, True)



  #création de l'image finale

# On additionne les trois images pour le rendu final
pipeline4 = pipeline1.image + pipeline2.image  + pipeline3.image


imgplot = plt.imshow(np.clip(pipeline4, 0, 1))
plt.show()