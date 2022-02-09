import numpy as np


def GET_VALUE_FROM_TXT_MEF1D_FINITO(FILENAME):
    """
    This function reads data from .txt file.

    Input:
    FILENAME              | Structural dataset                                     | .txt extension

    Output: 
    TYPE_ELEMENT          | Type element in Finito algorithm                       | Integer 
                               0 - Frame bar element    
    TYPE_SOLUTION         | Solution of the system of equations                    | Integer
                               0 - Condense procedure
                               1 - Zero and One algorithm    
    N_NODES               | Number of nodes                                        | Integer
    N_MATERIALS           | Number of materials                                    | Integer
    N_SECTIONS            | Number of sections                                     | Integer
    N_ELEMENTS            | Number of frame elements                               | Integer
    N_DOFPRESCRIPTIONS    | Number of DOF displacement control                     | Integer
    N_DOFLOADED           | Number of DOF forces                                   | Integer
    N_DOFSPRINGS          | Number of DOF spring elements                          | Integer
    COORDINATES           | Coordinates properties                                 | Py Numpy array
                               Node, x, y
    ELEMENTS              | Elements properties                                    | Py Numpy array
                               Node 0 ... Node (N_NODES - 1), Material ID, 
                               Geometry ID, Hinge ID node 0, Hinge ID node 1
    MATERIALS             | Materials properties                                   | Py Numpy array
                               Young, Poisson, Density, Thermal coefficient
    SECTIONS              | Sections properties                                    | Py Numpy array
                               Area, Inertia 1, Inertia Frame bar, X GC, Y GC
    PRESCRIPTIONS         | Prescribed DOF displacement properties                 | Py Numpy array              
                               Node, Direction (X = 0, Y = 1, Z = 2), Value 
    NODAL_LOAD            | Nodal DOF force properties                             | Py Numpy array              
                               Node, Direction (X = 0, Y = 1, Z = 2), Value
    SPRINGS               | Nodal DOF spring properties                            | Py Numpy array              
                               Node, Direction (X = 0, Y = 1, Z = 2), Value 
    """
    # Open file and read dataset
    FILE = open(FILENAME, "r")
    DATASET = FILE.read().split("\n")
    TYPE_ELEMENT = int(DATASET.pop(0).split(':')[1])
    TYPE_SOLUTION = int(DATASET.pop(0).split(':')[1])
    N_NODES = int(DATASET.pop(0).split(':')[1])
    N_MATERIALS = int(DATASET.pop(0).split(':')[1])
    N_SECTIONS = int(DATASET.pop(0).split(':')[1])
    N_ELEMENTS = int(DATASET.pop(0).split(':')[1])
    N_DOFPRESCRIPTIONS = int(DATASET.pop(0).split(':')[1])
    N_DOFLOADED = int(DATASET.pop(0).split(':')[1])
    N_DOFSPRINGS = int(DATASET.pop(0).split(':')[1])
    DATASET.pop(0)
    DATASET.pop(0)
    # Coordinates
    COORDINATES = np.zeros((N_NODES, 2))
    for I_COUNT in range(N_NODES):
        VALUES = DATASET.pop(0).split(',')
        COORDINATES[int(VALUES[0]), 0] = float(VALUES[1])
        COORDINATES[int(VALUES[0]), 1] = float(VALUES[2])
    DATASET.pop(0)
    DATASET.pop(0)
    # Elements
    ELEMENTS = np.zeros((N_ELEMENTS, 6))
    for J_COUNT in range(N_ELEMENTS):
        VALUES = DATASET.pop(0).split(',')
        ELEMENTS[int(VALUES[0]), 0] = int(VALUES[1])
        ELEMENTS[int(VALUES[0]), 1] = int(VALUES[2])
        ELEMENTS[int(VALUES[0]), 2] = int(VALUES[3])
        ELEMENTS[int(VALUES[0]), 3] = int(VALUES[4])
        ELEMENTS[int(VALUES[0]), 4] = int(VALUES[5])
        ELEMENTS[int(VALUES[0]), 5] = int(VALUES[6])
    DATASET.pop(0)
    DATASET.pop(0)
    # Materials
    MATERIALS = np.zeros((N_MATERIALS, 4))
    for K_COUNT in range(N_MATERIALS):
        VALUES = DATASET.pop(0).split(',')
        MATERIALS[int(VALUES[0]), 0] = float(VALUES[1])
        MATERIALS[int(VALUES[0]), 1] = float(VALUES[2])
        MATERIALS[int(VALUES[0]), 2] = float(VALUES[3])
        MATERIALS[int(VALUES[0]), 3] = float(VALUES[4])
    DATASET.pop(0)
    DATASET.pop(0)
    # Sections
    SECTIONS = np.zeros((N_SECTIONS, 5))
    for L_COUNT in range(N_SECTIONS):
        VALUES = DATASET.pop(0).split(',')
        SECTIONS[int(VALUES[0]), 0] = float(VALUES[1])
        SECTIONS[int(VALUES[0]), 1] = float(VALUES[2])
        SECTIONS[int(VALUES[0]), 2] = float(VALUES[3])
        SECTIONS[int(VALUES[0]), 3] = float(VALUES[4])
        SECTIONS[int(VALUES[0]), 4] = float(VALUES[5])
    DATASET.pop(0)
    DATASET.pop(0)
    # Prescribed DOF displacements
    PRESCRIPTIONS = np.zeros((N_DOFPRESCRIPTIONS, 3))
    for M_COUNT in range(N_DOFPRESCRIPTIONS):
        VALUES = DATASET.pop(0).split(',')
        PRESCRIPTIONS[int(VALUES[0]), 0] = int(VALUES[1])
        PRESCRIPTIONS[int(VALUES[0]), 1] = int(VALUES[2])
        PRESCRIPTIONS[int(VALUES[0]), 2] = float(VALUES[3])
    DATASET.pop(0)
    DATASET.pop(0)
    """
    # Element load *Under development
    if N_ELEMENTSLOADED == 0:
        DATASET.pop(0)
        ELEMENT_EXTERNAL_LOAD = "null"
    else:
        ELEMENT_EXTERNAL_LOAD = np.zeros((N_ELEMENTSLOADED, 5))
        for N_COUNT in range(N_ELEMENTSLOADED):
            VALUES = DATASET.pop(0).split(',')
            ELEMENT_EXTERNAL_LOAD[int(VALUES[0]),0] = float(VALUES[1])
            ELEMENT_EXTERNAL_LOAD[int(VALUES[0]),1] = float(VALUES[2])    
            ELEMENT_EXTERNAL_LOAD[int(VALUES[0]),2] = float(VALUES[3])
            ELEMENT_EXTERNAL_LOAD[int(VALUES[0]),3] = float(VALUES[4])
    DATASET.pop(0)
    DATASET.pop(0)
    """
    # Nodal DOF load
    NODAL_LOAD = np.zeros((N_DOFLOADED, 3))
    for O_COUNT in range(N_DOFLOADED):
        VALUES = DATASET.pop(0).split(',')
        NODAL_LOAD[int(VALUES[0]), 0] = float(VALUES[1])
        NODAL_LOAD[int(VALUES[0]), 1] = float(VALUES[2])
        NODAL_LOAD[int(VALUES[0]), 2] = float(VALUES[3])
    DATASET.pop(0)
    DATASET.pop(0)
    # Spring DOF elements
    if N_DOFSPRINGS == 0:
        DATASET.pop(0)
        SPRINGS = "null"
    else:
        SPRINGS = np.zeros((N_DOFSPRINGS, 3))
        for P_COUNT in range(N_DOFSPRINGS):
            VALUES = DATASET.pop(0).split(',')
            SPRINGS[int(VALUES[0]), 0] = int(VALUES[1])
            SPRINGS[int(VALUES[0]), 1] = int(VALUES[2])
            SPRINGS[int(VALUES[0]), 2] = float(VALUES[3])
    return TYPE_SOLUTION, TYPE_ELEMENT, N_NODES, N_MATERIALS, N_SECTIONS, N_ELEMENTS, N_DOFPRESCRIPTIONS, N_DOFLOADED, N_DOFSPRINGS, COORDINATES, ELEMENTS, MATERIALS, SECTIONS, PRESCRIPTIONS, NODAL_LOAD, SPRINGS
