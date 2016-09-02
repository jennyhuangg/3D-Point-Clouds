"""
TODO: Fill in this docstring to sign your name on your work, just like you would
for an assignment in any other class.  Include the assignment name, class name,
date, your name, etc.  See the HW1 solution file for an example.
"""

from gfx_helper_script import *
from gfx_helper_plotting import *

def main():
  """
  Plots several 3D shapes as clouds of points in different octants of space.
  """
  fig = plt.figure()

  # Add a set of 3D axes on which you can plot things.
  ax = fig.add_subplot(1, 1, 1, projection='3d')
  ax.set_xlim(-5, 5)
  ax.set_ylim(-5, 5)
  ax.set_zlim(-5, 5)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.grid(True)

  drawPointCloud(cubeVerts() + np.reshape([2.5, 2.5, 2.5], (3, 1)), ax)
  drawPointCloud(ellVerts() + np.reshape([-2.5, 2.5, 2.5], (3, 1)), ax)
  drawPointCloud(prismVerts(5) + np.reshape([-2.5, -2.5, 2.5], (3, 1)), ax)
  drawPointCloud(prismVerts(15) + np.reshape([2.5, -2.5, 2.5], (3, 1)), ax)
  drawPointCloud(sphereVerts(10) + np.reshape([2.5, 2.5, -2.5], (3, 1)), ax)
  drawPointCloud(torusVerts(10) + np.reshape([-2.5, 2.5, -2.5], (3, 1)), ax)

  # This needs to be the last line of main() --- the program pauses here until
  # the user closes the window, and after that there's nothing more to do.
  plt.show()


def cubeVerts():
  """
  Returns a 3x8 array of the eight vertices of the "unit cube".  In analogy with
the unit circle, it has "radius" 1 --- that is, the edges all have length 2.
  """
  p1 = [1,1,1]
  p2 = [1,1,-1]
  p3 = [1,-1,-1]
  p4 = [1,-1,1]
  p5 = [-1,1,1]
  p6 = [-1,1,-1]
  p7 = [-1,-1,-1]
  p8 = [-1,-1,1]
  points = np.array([p1, p2, p3, p4, p5, p6, p7, p8]).T
  return points

def ellVerts():
  """
  Returns a 3x12 array of the 12 vertices of an L shape, like three cubes
attached to each other.  The edge length of each cube is 1, the whole shape is
centered on the origin, and the L lies parallel to the X-Y plane.  Like this:

              *----*
             /    /|
            *----* |              | Y
            |    | *----*         |
            |    |/    /|         |    X
            |    *----* |         *-----
            |         | *        /
            |         |/        /
            *---------*          Z

  """
  p1 = [1, 0, 0.5]
  p2 = [0,0,0.5]
  p3 = [0,1,0.5]
  p4 = [-1,1,0.5]
  p5 = [-1,-1,0.5]
  p6 = [1,-1,0.5]
  p7 = [1, 0, -0.5]
  p8 = [0,0,-0.5]
  p9 = [0,1,-0.5]
  p10 = [-1,1,-0.5]
  p11 = [-1,-1,-0.5]
  p12 = [1,-1,-0.5]

  points = np.array([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]).T
  return points

def prismVerts(K):
  """Returns a 3x(2K) array representing vertices of a regular K-gon prism.  The
prism is centered on the origin, has height 2 along an axis parallel to the Y-
axis, and has "radius" 1: all the vertices are a distance 1 from this axis.  The
points (1,1,0) and (1,-1,0) should always be vertices of the prism.
Here's what a K=4 (square) prism would look like:

                .-*-.
             .-`     `-.
            *           *
            |`-.     .-`|         | Y
            |   `-*-`   |         |
            |     |     |         |    X
            |     |     |         *-----
            |     |     |        /
            *     |     *       /
             `-.  |  .-`         Z
                `-*-`

  """
  # Finds equally distributed angles from 0 to 2pi
  maxAngle = 2*np.pi
  angles = np.linspace(0, maxAngle, K, False)

  # Finds respective points according to angle
  x = np.concatenate((np.cos(angles), np.cos(angles)), 0)
  z = np.concatenate((np.sin(angles), np.sin(angles)), 0)
  y = np.concatenate((np.repeat([1], K, 0), np.repeat([-1], K, 0)), 0)

  points = np.concatenate(([x], [y], [z]), 0)
  return points

def sphereVerts(K):
  """
  Returns a 3x(2 + (K+1)(K+3)) array representing vertices on the surface of the
unit sphere, centered at the origin.  The sampling on the sphere follows a
"latitude/longitude" pattern: there are K+1 lines of latitude, and K+3 lines of
longitude, equally distributed around the sphere.  There's one vertex at each
pole (2 verts total), plus one more at each lat/lon intersection (that's
(K+1)(K+3) additional verts).
  The north and south poles are at (0,1,0) and (0,-1,0), respectively, and the
"prime meridian" (which should always be included) runs between the poles
through the point (1,0,0).  (This means that your sphere should always include
at least K+3 points whose Z-coordinate is 0: the poles, plus the K+1 vertices
along the prime meridian.)
  """
  # Finds equally distributed angles
  phi = np.array([np.linspace(0, np.pi, K+2, False)[1:]]).T
  theta = np.linspace(0, 2*np.pi, K+3, False)

  # Finds respective points according to angles
  x = (np.sin(phi) * np.cos(theta)).reshape((-1,))
  z = (np.sin(phi) * np.sin(theta)).reshape((-1,))
  y = (np.cos(phi) * np.ones_like(theta)).reshape((-1,))

  points = np.concatenate(([x], [y], [z]), 0)
  points = np.concatenate(([[0], [1], [0]], points, [[0], [-1], [0]]), 1)
  return points

def torusVerts(K):
  """
  Returns a 3x((K+3)^2) array representing vertices on the surface of a torus
lying parallel to the X-Y plane, centered at the origin.  The overall diameter
is 2, and the diameter of the inner hole is 2/3.  The point (1,0,0) should
always be included; it's indicated by an arrow in each picture below.  Here are
two plan views:

    Looking down the Z-axis:

                      ,,ggddY"^"Ybbgg,,                 --+----
                 ,agd""'             `""bg,               |
              ,gdP"                      "Ybg,            |
            ,dP"                            "Yb,          |  2/3
          ,dP"                                "Yb,        |
         ,8"                                     "8,      |          | Y
        ,8'                ,gPPRg,                `8,   --+----      |
       ,8'              ,dP"'   '"Yb,              `8,    |          |     X
       d'              d"           "b              `b    |          *------
       8              d'             `b              8    |
       8              8               8        ----> *    |  2/3
       8              Y,             ,P              8    |
       Y,              Ya           aP              ,P    |
       `8,              "Yb,_   _,dP"              ,8'    |
        `8,               `"YbbdP"'               ,8'   --+----
         `8a                                     a8'      |
          `Yba                                 adP'       |
            "Yba                             adY"         |  2/3
              `"Yba,                     ,adP"'           |
                 `"Y8ba,             ,ad8P"'              |
                      ``""YYbaaadPP""''                 --+----

                                     (edited from http://ascii.co.uk/art/circle)

    Looking up the Y-axis:

            ,ggddY""'""'""'""''""'""'""'""'Ybbgg,       --+----
         ,dP"'                                 '"Yb,      |
        d"                                         "b     |          | Z
       d'                                           `b    |          |
       8                                       ----> *    |  2/3     |     X
       Y,                                           ,P    |          *------
        Ya                                          aP    |
         "Yb,_                                  _,dP"     |
            `"Ybba..........................addP"'      --+----

  """
  """# Finds equally distributed angles from 0 to 2pi
  phi = np.array([np.linspace(0, 2*np.pi, K+3, False)]).T
  theta = np.linspace(0, 2*np.pi, K+3, False)

  # Finds respective points according to angles
  r = 2/3.0 - 1/3.0 * np.cos(theta)
  x = (r * np.cos(phi)).reshape((-1,))
  y = (r * np.sin(phi)).reshape((-1,))
  z = (1/3.0 * np.sin(theta) * np.ones_like(phi)).reshape((-1,))

  points = np.concatenate(([x], [y], [z]), 0)
  return points"""

  wand = np.concatenate((
      (np.cos(np.linspace(0, 2*np.pi, K+3, False))[None, :, None] + 2)/3,
      (np.cos(np.linspace(0, 2*np.pi, K+3, False))[None, :, None] + 2)/3,
      np.sin(np.linspace(0, 2*np.pi, K+3, False))[None, :, None]/3
    ), 2)
  sweep = np.concatenate((
      np.cos(np.linspace(0, 2*np.pi, K+3, False))[:, None, None],
      np.sin(np.linspace(0, 2*np.pi, K+3, False))[:, None, None],
      np.ones((K+3, 1, 1))
    ), 2)
  return (wand * sweep).reshape((-1,3)).T

# This calls main() when the program is invoked from the command line.
if __name__ == "__main__":
  main()
