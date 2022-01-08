class AircraftQueue:
  listOfAircraft = []
  
  def systemBoot(self):
    print("System Starting")
  
  def enqueue(self, AC):
    return self.listOfAircraft.append(AC)
    
  def dequeue(self):
    myAircraft = self.listOfAircraft
    if len(myAircraft) == 0:
      print("Currently No Aircrafts")
      return
      
    removalIndex = 0
    removalType = ""
    removalSize = ""
    for index, aircraft in enumerate(myAircraft):
      currentType = aircraft.getType()
      currentSize = aircraft.getSize()
      if currentType == "Passenger":
        if currentSize == "Large":
          removalIndex = index
          break
        elif currentSize == "Small" and removalType != "Passenger":
          removalType = currentType
          removalIndex = index
      elif currentType == "Cargo":
        if removalType == "Passenger":
          continue
        elif currentSize == "Large" and removalSize == "Small":
          removalType = currentType
          removalIndex = index
          removalSize = currentSize
        elif currentSize == "Small":
          removalType = currentType
          removalIndex = index
          removalSize = currentSize
    
    removed = myAircraft[removalIndex]
    self.listOfAircraft.pop(removalIndex)
    return removed

  def getList(self):
    return self.listOfAircraft

class Aircraft:
  def __init__(self, ACname, ACtype, ACsize):
    self.ACname = ACname
    self.ACtype = ACtype
    self.ACsize = ACsize
    
  def getName(self):
    return self.ACname
    
  def getType(self):
    return self.ACtype
  
  def getSize(self):
    return self.ACsize

airport = AircraftQueue()
airport.systemBoot()

aircraft1 = Aircraft("AB", "Passenger", "Small")
aircraft2 = Aircraft("CB", "Cargo", "Small")
aircraft3 = Aircraft("AD", "Passenger", "Large")
aircraft4 = Aircraft("CD", "Cargo", "Large")
aircraft5 = Aircraft("XY", "Passenger", "Small")
aircraft6 = Aircraft("YX", "Passenger", "Large")
aircraft7 = Aircraft("ZY", "Cargo", "Large")
aircraft8 = Aircraft("KC", "Passenger", "Large")
aircraft9 = Aircraft("PZ", "Cargo", "Large")
aircraft10 = Aircraft("EZ", "Passenger", "Small")

airport.enqueue(aircraft1)
airport.enqueue(aircraft2)
airport.enqueue(aircraft3)
airport.enqueue(aircraft4)
airport.enqueue(aircraft5)
airport.enqueue(aircraft6)
airport.enqueue(aircraft7)
airport.enqueue(aircraft8)
airport.enqueue(aircraft9)
airport.enqueue(aircraft10)

removedAC1 = airport.dequeue()
print(removedAC1.getName())
removedAC2 = airport.dequeue()
print(removedAC2.getName())
removedAC3 = airport.dequeue()
print(removedAC3.getName())
removedAC4 = airport.dequeue()
print(removedAC4.getName())
removedAC5 = airport.dequeue()
print(removedAC5.getName())
removedAC6 = airport.dequeue()
print(removedAC6.getName())
removedAC7 = airport.dequeue()
print(removedAC7.getName())
removedAC8 = airport.dequeue()
print(removedAC8.getName())
removedAC9 = airport.dequeue()
print(removedAC9.getName())
removedAC10 = airport.dequeue()
print(removedAC10.getName())
removedAC11 = airport.dequeue()
print(removedAC11.getName())