class AircraftQueue:
  boot = False
  listOfAircraft = []
  typeWeights = {
    'Cargo': 0,
    'Passenger': 2
  }
  sizeWeights = {
    'Small': 0,
    'Large': 1
  }

  # Cargo Small = 0
  # Cargo Large = 1
  # Passenger Small = 2
  # Passenger Large = 3

  def systemBoot(self):
    try:
      self.boot = not self.boot
      return print("System Booting..." if self.boot else "System Shutting Off...")
    except Exception as e:
      return print(e)
      
  
  def enqueue(self, AC):
    try:
      if not self.boot:
        return print("System Not Booted")
        
      return self.listOfAircraft.append(AC)
    except Exception as e:
      return print(e)
    
  def dequeue(self):
    try:
      if not self.boot:
        return print("System Not Booted")

      myAircraft = self.listOfAircraft
      if len(myAircraft) == 0:
        return print("Currently No Aircrafts")
        
      removalIndex = 0
      maxWeight = 0
      for index, aircraft in enumerate(myAircraft):
        currentType = aircraft.getType()
        currentSize = aircraft.getSize()
        currentWeight = self.typeWeights[currentType] + self.sizeWeights[currentSize]
        if currentWeight > maxWeight:
          maxWeight = currentWeight
          removalIndex = index
      
      removed = myAircraft[removalIndex]
      self.listOfAircraft.pop(removalIndex)
      return removed
    except Exception as e:
      return print(e)

  def getList(self):
    return self.listOfAircraft

class Aircraft:
  def __init__(self, ACname, ACtype, ACsize):
    self.ACname = ACname
    self.ACtype = ACtype
    self.ACsize = ACsize
    
  def getName(self):
    try:
      return self.ACname
    except Exception as e:
      return print(e)
    
  def getType(self):
    try:
      return self.ACtype
    except Exception as e:
      return print(e)
  
  def getSize(self):
    try:
      return self.ACsize
    except Exception as e:
      return print(e)

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