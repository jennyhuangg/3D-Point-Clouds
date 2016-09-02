import numpy as np

def drawPolyline(points, ax, linespec=None):
  """
  Given a 2xN array (or matrix) representing N points in the plane, plot all
the points as dots on the plane, connected by straight line segments.  ax is the
pyplot axes on which to plot.
  Optional argument "linespec" may be any Matplotlib line format string.  See
    http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
  """
  if len(points.shape) != 2 or points.shape[0] != 2:
    raise ValueError("'points' must be 2xN")
  if linespec is None:
    linespec = color_cycle.next() + 'o-'
  ax.plot(points[0,:].T, points[1,:].T, linespec)


def drawPolygon(points, ax, linespec=None):
  """
  Given a 2xN array (or matrix) representing N points in the plane, plot all
the points as dots, connected by straight line segments, with a final segment
going back to the first dot.  ax is the pyplot axes on which to plot.
  Optional argument "linespec" may be any Matplotlib line format string.  See
    http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
  """
  if len(points.shape) != 2 or points.shape[0] != 2:
    raise ValueError("'points' must be 2xN")
  if linespec is None:
    linespec = color_cycle.next() + 'o-'
  ax.plot(np.concatenate((points[0,:], [points[0,0]]), 1).T,
          np.concatenate((points[1,:], [points[1,0]]), 1).T, linespec)


def drawPointCloud(points, ax, color=None):
  """
  Given a 3xN array (or matrix) representing N points in space, plot all the
points as dots.
  ax is the pyplot axes on which to plot.  Note that ax must be an Axes3D, which
is found in mpl_toolkits.mplot3d.  Here's how you make one:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')
  Optional argument "color" may be:
   - "b", "g", "r", "c", "m", "y", or "k": blue, green, red, cyan, magenta,
                                           yellow, or black, respectively
   - None: the next default color
   - 0, 1, or 2: shade according to the x, y, or z coordinate of each point
  The default is None (the next default color).
  """
  if len(points.shape) != 2 or points.shape[0] != 3:
    raise ValueError("'points' must be 3xN")
  if color == None:
    color = color_cycle.next()
  elif color in (0, 1, 2):
    color = points[color, :]
  ax.scatter(points[0,:].T, points[1,:].T, points[2,:].T, c=color)


# Generator for a global cycle of plotting colors.
def makeColorCycleGenerator():
  colors = 'bgrcmyk'
  next_color = 0
  while(True):
    color = colors[next_color]
    next_color = (next_color + 1) % len(colors)
    yield color

color_cycle = makeColorCycleGenerator()
