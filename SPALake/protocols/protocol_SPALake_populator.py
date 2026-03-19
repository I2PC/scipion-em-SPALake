# **************************************************************************
# *
# * Authors: Alberto Garcia Mena   (alberto.garcia@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 3 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************
import os

import pyworkflow.protocol.constants as cons
from pyworkflow.utils import Message
from pyworkflow import BETA, UPDATED, NEW, PROD
import pyworkflow.utils as pwutils
import pyworkflow.protocol.params as params
from pwem.protocols import EMProtocol
from pyworkflow.protocol import getUpdatedProtocol


class spaLakePopulator(EMProtocol):
    _label = 'This protocol will collect the main data from the SPA workflow and push to the SPALake dataBase those data'
    _devStatus = BETA

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # -------------------------- DEFINE param functions ----------------------
    def _defineParams(self, form):
        """ Define the input parameters that will be used.
        """
        # You need a params to belong to a section:
        form.addSection(label=Message.LABEL_INPUT)
        form.addParam('dataFromScreening', params.EnumParam, default=1,
                      choices=['True', 'False'],
                      display=params.EnumParam.DISPLAY_HLIST,
                      label='Data from the screening (Smartscope or SmartEPU plugin)',
                      help='True if data from the screening is on the workflow (Smartscope or SmartEPU plugin).')

        form.addParam('Grids', params.PointerParam,
                       pointerClass='SetOfMicrographs',
                       label="Grid used for picker",
                       help='Micrographs used on the picker')



        #Grid, Square, holes, moviesSS


        form.addParam('micrographs', params.PointerParam,
                       pointerClass='SetOfMicrographs',
                       label="Micrographs used for picker",
                       help='Micrographs used on the picker')

        form.addParam('goodClassesOrigin', params.EnumParam, default=0,
                      choices=['Relion', 'Cryoasses', 'Manual'],
                      display=params.EnumParam.DISPLAY_HLIST,
                      label='Select the protocol that generate the good2Dclasses ranked',
                      help='Relion generates setOf2DClasses and Cryoasses SetOfAverages, select the protocol the good classes come from.')
        form.addParam('goodClasses2DRelion', params.PointerParam,
                       condition='goodClassesOrigin==0',
                       pointerClass='SetOfClasses2D',
                       label="Good Classes2D from Relion",
                       help='Set of good Classes2D calculated by Relion ranker')
        form.addParam('goodClasses2DCryoasses', params.PointerParam,
                       condition='goodClassesOrigin==1',
                       pointerClass='SetOfAverages',
                       label="Good Classes2D from Cryoasses",
                       help='Set of good Classes2D calculated by Cryoasses ranker')
        form.addParam('goodClasses2DManual', params.PointerParam,
                       condition='goodClassesOrigin==2',
                       pointerClass='SetOfAverages',
                       label="Good Classes2D from manual selection",
                       help='Set of good Classes2D from manual selection (protUserSubset')


        form.addParam('volume', params.PointerParam,
                       pointerClass='SetOfMicrographs',
                       label="Volume refined",
                       help='Volume refined')



