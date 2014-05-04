#!/usr/bin/env python2

'''Creates a Circle with a given radius
as a special case of a :class:`~psychopy.visual.Polygon`'''

# Part of the PsychoPy library
# Copyright (C) 2014 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

import psychopy  # so we can get the __path__
from psychopy import logging

from psychopy.visual.polygon import Polygon
from psychopy.tools.attributetools import logAttrib, attributeSetter

import numpy


class Circle(Polygon):
    """Creates a Circle with a given radius as a special case of a :class:`~psychopy.visual.ShapeStim`

    (New in version 1.72.00)
    """
    def __init__(self, win, radius=.5, edges=32, **kwargs):
        """
        Circle accepts all input parameters that `~psychopy.visual.ShapeStim` accept, except for vertices and closeShape.

        :Parameters:

            edges : float or int (default=32)
                Specifies the resolution of the polygon that is approximating the
                circle.
        """
        #what local vars are defined (these are the init params) for use by __repr__
        self._initParams = dir()
        self._initParams.remove('self')
        #kwargs isn't a parameter, but a list of params
        self._initParams.remove('kwargs')
        self._initParams.extend(kwargs)
        self.edges = edges

        #initialise parent class
        kwargs['edges'] = edges
        kwargs['radius'] = radius
        super(Circle, self).__init__(win, **kwargs)
    
    @attributeSetter
    def radius(self, radius):
        """float, int, tuple, list or 2x1 array
        Radius of the Circle (distance from the center to the corners).
        If radius is a 2-tuple or list, the values will be interpreted as semi-major and
        semi-minor radii of an ellipse.

        :ref:`Operations <attrib-operations>` supported.
        
        Usually there's a setAttribute(value, log=False) method for each attribute. Use this if you want to disable logging."""
        self.__dict__['radius'] = numpy.asarray(radius)
        self._calcVertices()
        self.setVertices(self.vertices, log=False)
    def setRadius(self, radius, log=True):
        """Usually you can use 'stim.attribute = value' syntax instead,
        but use this method if you need to suppress the log message"""
        self.radius = radius
        logAttrib(self, log, 'radius', radius)
