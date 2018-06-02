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
        print("Parameters Initialized\nPrint a {1} made of {2} out of {0}, and a weight of {3}\n".format(matPrint.name, self.name, self.materialPart.name,matWeight.name))

    def addWeight(self, width, height):
        self.barWidth = width
        self.barHeight = height
        self.isWeightAdded = True
        print("Weight dimensions have been added", width, height, ". \nIt is ", obj.isWeightAdded,"the solution can be found")

    def geometry(self):
        print(self.height, self.width, self.length)

    def calculateWeightMass(self):
        #PseudoCode
        # Find mass of the Weight
        # Find volume of that Weight
        # Find the mass of the equivalent Print that's removed to make space for the Weight.
        # Take the mass of the original object, subtract the mass of the Print and the Weight
        # Calculate the error between the mass of the original object and the Print and weight
        if self.isWeightAdded == True:
            #Initial Conditions
            isNotConverged = True
            counter = 0
            massPart = self.massPart
            densityWeight = self.densityWeight
            densityPrint = self.densityPrint
            massPrint = self.volume * densityPrint
            massWeight = massPart - massPrint
            volumeWeight = massWeight / densityWeight
            massError = volumeWeight * densityPrint #This is the volume of weight removed from the print.
            massPrint = massPrint - massError

            while isNotConverged:
                massError = massPart - (massWeight + massPrint)
                volumeError = massError / densityWeight
                massPrint = massPrint - volumeError
                massWeight = massWeight + massError
                counter += 1
                if counter > 150 or round(massError,1) < 0.01:
                    isNotConverged = False
                print("Loop: {0:2}. The mass print:{1:.2f}, weight:{2:.2f}, error:{3:.2f}".format(counter, massPrint, massWeight, massError))

            #Outputs
            self.massPrint = massPrint
            self.volumePrint = massPrint / densityPrint
            self.massWeight = massWeight
            self.volumeWeight = massWeight / densityWeight
        else:
            print("The part has been created. It is ", obj.isWeightAdded,"the solution can be found")
    # def testObject(self):

    
##Setup Variables and Initial Conditions
matPrint = material("ABS", 1.1)
matWeight = material("314 SS", 7.7)
matToMimic = material("Bone", 2.0)
obj = object("Tibia", matToMimic, matPrint, matWeight, 400)
obj.addWeight(2,2) #In the future this can be monte carolo'd to find optimal size parameters.
obj.calculateWeightMass()

barLength = obj.volumeWeight / (obj.barWidth * obj.barHeight)
# massError = obj.massPart - (massPrint + massWeight)
print("The bar Length found is ", round(barLength,2))
