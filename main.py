userinput = input("Please Enter the choice number from the menu: ")

allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'RAM 1500']

print("********************************")
print("AutoCountry Vehicle Finder v0.3")
print("********************************")
print("Please Enter the following number below from the following menu:")

print("1. PRINT all Authorized Vehicles")
print("2. SEARCH for Authorized Vehicle")
print("3. ADD Authorized Vehicle")
print("4. Exit")
print("********************************")

if userinput == '1':
      print("Authorized Vehicles List:")
      for vehicle in allowedVehiclesList:
          print(vehicle)

elif userinput == '2':
      search_vehicle = input("Please Enter the full Vehicle name you would like to search:")
      if search_vehicle in allowedVehiclesList:
          print(f"{search_vehicle} is an authorized vehicle.")
      else:
          print(f"{search_vehicle} is not an authorized vehicle.")

elif userinput == '3':
      new_vehicle = input("Please Enter the full Vehicle name you would like to add:")
      allowedVehiclesList.append(new_vehicle)
      print(f"{new_vehicle} has been added to the authorized vehicles list.")

elif userinput == '4':
      print("Exiting...")

else:
      print("Invalid choice. Please select a valid option.")