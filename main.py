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

vertices, triangles = readply('suzanne.ply')

vertices2, triangles2 = readply('suzanne2.ply')

# vertices3, triangles3 = readply('cube3.ply')

data = dict([
  ('viewMatrix',cam.getMatrix()),
  ('projMatrix',proj.getMatrix()),
  ('cameraPosition',cameraPosition),
  ('lightPosition',lightPosition),
])

alpha1 = 0.99
alpha2 = 1
alpha3 = 0.98

pipeline1.draw(vertices, triangles, data, alpha1)

pipeline2.draw(vertices2, triangles2, data, alpha2)

# pipeline3.draw(vertices3, triangles3, data, alpha3)

# On additionne les deux images pour le rendu final
pipeline4 = pipeline1.image + pipeline2.image #+ pipeline3.image

import matplotlib.pyplot as plt
imgplot = plt.imshow(pipeline4)
plt.show()