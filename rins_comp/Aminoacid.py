class Aminoacid_node():
    def __init__(self, nodeId, chain, position, residue, dssp, degree, bfactorCA, x, y, z, pdbFileName, rapdf, tap, accessibility):
        self._nodeId = nodeId
        self._chain = chain
        self._position = int(position)
        self._residue = residue
        self._dssp = dssp
        self._degree = degree
        self._bfactorCA = bfactorCA
        self._x = x
        self._y = y
        self._z = z
        self._pdbFileName = pdbFileName
        self._rapdf = rapdf
        self._tap = tap
        self._accessibility = accessibility

    #MOSTRAR AMINOACIDO
    def show_amino(self):
        return self._nodeId + '\t\t' + self._chain + '\t\t\t' + str(self._position) + '\t\t\t' + self._degree + '\t\t\t' + self._bfactorCA + '\t\t\t' + self._pdbFileName

    #MOSTRAR AMINOACIDO
    def show_id(self):
        return self._nodeId


    #COMPARAR NODES NAO EXISTENTES
    def compare_nodeId(self, aminoacid):
        if self._position == aminoacid._position and self._residue == aminoacid._residue:
            return True
        else:
            return False

    #COMPARAR BFACTOR
    def compare_bfactor(self, aminoacid):
        if self._bfactorCA == aminoacid._bfactorCA:
            return True
        else:
            return False

    #COMPARAR DEGREE
    def compare_degree(self, aminoacid):
        if self._degree == aminoacid._degree:
            return True
        else:
            return False

class Aminoacid_edge():
    def __init__(self, nodeId1, interaction, nodeId2, distance, angle, energy, atom1, atom2, donor, positive, cation, orientation):
        self._nodeId1 = nodeId1
        self._interaction = interaction
        self._nodeId2 = nodeId2
        self._distance = distance
        self._angle = angle
        self._energy = energy
        self._atom1 = atom1
        self._atom2 = atom2
        self._donor = donor
        self._positive = positive
        self._cation = cation
        self._orientation = orientation

        num1 = nodeId1.split(':')
        self._chain = num1[0] #CHAIN DO NODE 1
        self._numNode1 = int(num1[1])

        num2 = nodeId2.split(':')
        self._chain2 = num2[0] #CHAIN DO NODE 2
        self._numNode2 = int(num2[1])

        self._protein_name = ""

    def set_protein_name(self, name):
        self._protein_name = name

    def show_edge(self):
        if len(self._interaction) > 11:
            return self._nodeId1 + '\t\t' + self._interaction + '\t' + self._nodeId2 + '\t\t'
        else:
            return self._nodeId1 + '\t\t' + self._interaction + '\t\t' + self._nodeId2 + '\t\t'

    def compare_edge(self, aminoacid):
        if self._nodeId1 == aminoacid._nodeId1 and self._interaction == aminoacid._interaction and self._nodeId2 == aminoacid._nodeId2:
            return True
        else:
            return False
