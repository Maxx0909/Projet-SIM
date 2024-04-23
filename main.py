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

cameraPosition = np.array([1.1,1.1,1.1])
lookAt = np.array([-0.577,-0.577,-0.577])
up = np.array([0.33333333,  0.33333333, -0.66666667])
right = np.array([-0.57735027,  0.57735027,  0.])

cam = Camera(cameraPosition, lookAt, up, right)


  #Definition de la projection

nearPlane = 0.1
farPlane = 10.0
fov = 1.91986
aspectRatio = width/height

proj = Projection(nearPlane ,farPlane,fov, aspectRatio) 


  #Définition de la position de la lumière

lightPosition = np.array([10,0,10])


  #Lecture des deux fichiers pour Suzanne

vertices, triangles = readply('img/suzanne2.ply')
vertices2, triangles2 = readply('img/suzanne.ply')

data = dict([
  ('viewMatrix',cam.getMatrix()),
  ('projMatrix',proj.getMatrix()),
  ('cameraPosition',cameraPosition),
  ('lightPosition',lightPosition),
])

  #Définition des valeurs des alphas

# Les valeurs des alphas sont comprises entre 0 et 1 : plus alpha est proche de 0, plus l'objet est transparent
alpha1 = 0.5
alpha2 = 1

  #Création des différentes suzannes

#Création de Suzanne en rouge
r = 255
v = 0
b = 0
color = np.array([r/255, v/255, b/255])
pipeline1.draw(vertices, triangles, data, alpha1, color, False)

#Création de Suzanne en bleu
r = 0
v = 255
b = 0
color = np.array([r/255, v/255, b/255])
pipeline2.draw(vertices2, triangles2, data, alpha2, color, False)



  #création de l'image finale

# On additionne les deux images pour le rendu final
pipeline4 = pipeline1.image + pipeline2.image


imgplot = plt.imshow(np.clip(pipeline4, 0, 1))
plt.show()