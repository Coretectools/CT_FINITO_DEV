import json
from django.http import HttpResponse
import sys
import numpy
import os
from FINITO_FEM_TOOLBOX import MEF1D
from READ_INPUT_MEF1D import GET_VALUE_FROM_TXT_MEF1D_FINITO as gt


def index(request):
    return HttpResponse("index, baby")


def process(request):
    calc_data = MEF1D(FILENAME=filename)

    (
        TYPE_SOLUTION,
        TYPE_ELEMENT,
        N_NODES,
        N_MATERIALS,
        N_SECTIONS,
        N_ELEMENTS,
        N_DOFPRESCRIPTIONS,
        N_DOFLOADED,
        N_DOFSPRINGS,
        COORDINATES,
        ELEMENTS,
        MATERIALS,
        SECTIONS,
        PRESCRIPTIONS,
        NODAL_LOAD,
        SPRINGS,
    ) = gt(FILENAME=filename)

    raw_data = {
        "": TYPE_SOLUTION,
        "": TYPE_ELEMENT,
        "numNodes": N_NODES,
        "": N_MATERIALS,
        "": N_SECTIONS,
        "numElements": N_ELEMENTS,
        "": N_DOFPRESCRIPTIONS,
        "": N_DOFLOADED,
        "": N_DOFSPRINGS,
        "coords": COORDINATES.tolist(),
        "elems": ELEMENTS.tolist(),
        "": MATERIALS.tolist(),
        "": SECTIONS.tolist(),
        "": PRESCRIPTIONS.tolist(),
        "": NODAL_LOAD.tolist(),
        "": SPRINGS.tolist(),
    }

    # print(calc_data)

    for dict in calc_data:
        for key in dict:
            if type(dict[key]) is numpy.ndarray:
                dict[key] = dict[key].tolist()

    results = {"raw_data": raw_data, "calc_data": calc_data}
    print(json.dumps(results))
    return HttpResponse("process, ayaya")
