#Theory:
#This calculator will take the density of a final replica part and based on the difference in densitiies between the replica and the origianl material indicate the size of a weighted material to give it the correct weight.
#Units shouldn't matter as long as they are all consistent.
# mass (g)
# length (mm)


class material:
    def __init__(self, name, density):
        self.name = name
        self.density = density

class object:
    def __init__(self, name, materialPart=None, materialPrint=None, materialWeight=None, volume=None):
        self.name = name
        self.materialPart = materialPart
        self.materialPrint = materialPrint
        self.materialWeight = materialWeight
        self.volume = volume if volume is not None else 0#volume
        self.densityPart = materialPart.density
        self.densityPrint = materialPrint.density
        self.densityWeight = materialWeight.density
        self.massPart = self.densityPart * self.volume
        self.isWeightAdded = False


    def addWeight(self, width, height):
        self.barWidth = width
        self.barHeight = height
        self.isWeightAdded = True
        print("Weight dimensions have been added", width, height, ". \nIt is ", obj.isWeightAdded,"the solution can be found")

    def geometry(self):
        print(self.height, self.width, self.length)

##Setup Variables and Initial Conditions
matPrint = material("ABS", 1.1)
matWeight = material("314 SS", 7.7)
matToMimic = material("Bone", 2.0)

obj = object("Tibia", matToMimic, matPrint, matWeight, 400)
# objectPrinted = object("3D Print", matPrint)
# objectWeight = object("Weight Insert", matWeight)

# obj.massPrinted = obj.volume * matPrint.density
# obj.massWeight = obj.massPart - obj.massPrinted
# obj.massWeight = obj.volume * matWeight.density

print(matPrint.name, "Object to print is a ", obj.name, "and the material is", obj.materialPart.name)
# print("the mass of the [actual object, printed part, weight material as part] is [\n", obj.weight, obj.printedWeight, obj.weightWeight, "]")

##Determine the optimal void volume to be contained by the weight to match the actual parts weight.
# object.ratio = #Ratio is the ratio of weight to printed part.
# objectWeight.height = 5
# objectWeight.width = 5
# objectWeight.length = (obj.volume - objectPrinted.volume) / (objectWeight.height * objectWeight.width)
# print(objectWeight.length)
# objectWeight.geometry()
#
print("The part has been created. \nIt is ", obj.isWeightAdded,"the solution can be found")
obj.addWeight(2,2) #In the future this can be monte carolo'd to find optimal size parameters.
massPrint = obj.densityPrint * obj.volume
massWeight = obj.massPart - massPrint
volumeWeight = massWeight / obj.densityWeight
barLength = volumeWeight / (obj.barWidth * obj.barHeight)
massError = obj.massPart - (massPrint + massWeight)
print("The bar Length found is ", round(barLength,2), 'with a mass error of ', massError)

##Now must find the additional mass to be removed from this volume of material.

# massPrintRemoved = volumeWeight * obj.densityPrint
# massWeight2 = massWeight + massPrintRemoved
# volumeWeight2 = massWeight2 / obj.densityWeight
# barLength2 = volumeWeight2 / (obj.barWidth * obj.barHeight)
# print("The bar Length found is ", round(barLength2,2))

#PseudoCode
# Find mass of the Weight
# Find volume of that Weight
# Find the mass of the equivalent Print that's removed to make space for the Weight.
# Take the mass of the original object, subtract the mass of the Print and the Weight
# Calculate the error between the mass of the original object and the Print and weight

isNotConverged = True
counter = 0
while isNotConverged:
    massWeight = obj.massPart - massPrint
    volumeWeight = massWeight / obj.densityWeight
    massPrintRemoved = volumeWeight * obj.densityPrint
    massError = obj.massPart - (massPrint + massWeight - massPrintRemoved)
    # New Variables
    massPrint = massPrint - massPrintRemoved


    # barLengthOld = barLength
    # barLength = volumeWeight / (obj.barWidth * obj.barHeight)
    # print("The bar Length found is ", round(barLength2,2))
    # if round(barLength,2) == round(barLengthOld,2):
        # isNotConverged = False
    counter +=1
    if counter >15:
        isNotConverged = False
    print("Loop:", counter, "The mass [print, weight, print removed, error] is \n", round(massPrint,3), round(massWeight,3), round(massPrintRemoved,3), round(massError,4))
