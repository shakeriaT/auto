userinput = input("Please Enter the choice number from the menu: ")

allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'RAM 1500']

print("********************************")
print("AutoCountry Vehicle Finder v0.4")
print("********************************")
print("Please Enter the following number below from the following menu:")

print("1. PRINT all Authorized Vehicles")
print("2. SEARCH for Authorized Vehicle")
print("3. ADD Authorized Vehicle")
print("4.DELETE Authorized Vehicle")
print("5. ")
print("********************************")

if userinput == '1':
      print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
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
    remove_vehicle = input("Please enter full vehicle name you would like to remove:")
    allowedVehiclesList.remove(remove_vehicle)
    print(f"{remove_vehicle} Are you sure you want to remove '{remove_vehicle}' from the Authorized Vehicles List?")
    confirmation = input(f"Are you sure you want to remove '{remove_vehicle}' from the Authorized Vehicles List?:")
    if confirmation.lower() == 'yes':
        print(f"You have REMOVED '{remove_vehicle}' as an authorized vehicle") 

elif userinput == '5':
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")


else:
      print("Invalid choice. Please select a valid option.")