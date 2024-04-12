import numpy as np

width = 1280  
height = 720

from graphicPipeline import GraphicPipeline


pipeline1 = GraphicPipeline(width,height)
pipeline2 = GraphicPipeline(width,height)
pipeline3 = GraphicPipeline(width,height)


from camera import Camera
from projection import Projection


cameraPosition = np.array([1.1,1.1,1.1])
lookAt = np.array([-0.577,-0.577,-0.577])
up = np.array([0.33333333,  0.33333333, -0.66666667])
right = np.array([-0.57735027,  0.57735027,  0.])

cam = Camera(cameraPosition, lookAt, up, right)

nearPlane = 0.1
farPlane = 10.0
fov = 1.91986
aspectRatio = width/height

proj = Projection(nearPlane ,farPlane,fov, aspectRatio) 


lightPosition = np.array([10,0,10])

from readply import readply

# forme du TP3
vertices = np.array([
  [0.0, 0.0, 0.0, -0.577, -0.577, -0.577, 0.375000, 0.000000], #0
  [1.0, 0.0, 0.0, -0.577, -0.577, -0.577, 0.375000, 0.000000], #1
  [0.0, 1.0, 0.0, -0.577, -0.577, -0.577, 0.375000, 0.000000], #2
  [1.0, 1.0, 0.0, -0.577, -0.577, -0.577, 0.375000, 0.000000], #3
  [0.0, 0.0, 1.0, -0.577, -0.577, -0.577, 0.375000, 0.000000], #4
  [1.0, 0.0, 1.0, -0.577, -0.577, -0.577, 0.375000, 0.000000], #5
  [0.0, 1.0, 1.0, -0.577, -0.577, -0.577, 0.375000, 0.000000], #6
  [1.0, 1.0, 1.0, -0.577, -0.577, -0.577, 0.375000, 0.000000], #7
])
triangles = np.array([
  [1,0,2],
  [3,1,2],
  [4,5,6],
  [5,7,6],
  [0,1,4],
  [4,1,5],
  [2,6,3],
  [3,6,7],
  [0,6,2],
  [4,6,0],
  [1,3,7],
  [5,1,7]
  ], dtype=int)


# vertices2, triangles2 = readply('suzanne2.ply')

# vertices3, triangles3 = readply('cube3.ply')

data = dict([
  ('viewMatrix',cam.getMatrix()),
  ('projMatrix',proj.getMatrix()),
  ('cameraPosition',cameraPosition),
  ('lightPosition',lightPosition),
])

# Les valeurs des alphas sont comprises entre 0 et 1
alpha1 = 0.99
alpha2 = 1
alpha3 = 0.98

r = 255
v = 0
b = 0
color = np.array([r/255, v/255, b/255])
pipeline1.draw(vertices, triangles, data, alpha1, color)


# r = 0
# v = 0
# b = 255
# color = np.array([r/255, v/255, b/255])
# pipeline2.draw(vertices2, triangles2, data, alpha2, color)


# pipeline3.draw(vertices3, triangles3, data, alpha3)

# On additionne les deux images pour le rendu final
pipeline4 = pipeline1.image #+ pipeline2.image #+ pipeline3.image

import matplotlib.pyplot as plt

# pipeline4 contient des float, il faut donc le normaliser pour que les valeurs soient comprises entre 0 et 1
imgplot = plt.imshow(np.clip(pipeline4, 0, 1))
plt.show()