from FINITO_FEM_TOOLBOX import MEF1D, GET_VALUE_FROM_TXT_MEF1D_FINITO as gt
from django.http import HttpResponse
from django.http import JsonResponse
import numpy
import time
import os


def index(request):
    return HttpResponse("index")


def process(request):
    data = request.body.decode()
    filename = "data_" + str(time.time()) + ".txt"

    with open(filename, "w") as file:
        file.write(data)

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

    for dict in calc_data:
        for key in dict:
            if type(dict[key]) is numpy.ndarray:
                dict[key] = dict[key].tolist()

    os.remove(filename)
    results = {"rawData": raw_data, "calculatedData": calc_data}
    return JsonResponse(results)
