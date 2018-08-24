# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:40:33 2017

@author: Daniel Abrunhosa
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:50:32 2017

@author: Daniel Abrunhosa
"""

from Conventions.NeuroCore.Models.Conditions.Base import BaseParameters


class BCsParameters(BaseParameters):

    @property
    def InStart(self):
        return "inStart"

    @property
    def InEnd(self):
        return "inEnd"
