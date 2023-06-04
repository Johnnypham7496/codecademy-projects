# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. 
# Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

# Ground Shipping

# Weight of Package	                             Price per Pound	Flat Charge
# 2 lb or less	                                 $1.50	            $20.00
# Over 2 lb but less than or equal to 6 lb	     $3.00	            $20.00
# Over 6 lb but less than or equal to 10 lb	     $4.00	            $20.00
# Over 10 lb	                                 $4.75	            $20.00

# Ground Shipping Premium

# Flat charge: $125.00

# Drone Shipping

# Weight of Package	                            Price per Pound	    Flat Charge
# 2 lb or less	                                $4.50	            $0.00
# Over 2 lb but less than or equal to 6 lb	    $9.00	            $0.00
# Over 6 lb but less than or equal to 10 lb	    $12.00	            $0.00
# Over 10 lb	                                $14.25	            $0.00


weight = 80

# ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print(f'The cost of ground shipping is ${cost_ground}')

cost_ground_premium = 125
print(f'Ground Shipping Premium is ${cost_ground_premium}')


# drone shipping 
if weight <= 2:
  cost_drone = weight * 4.5 
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12 
else:
  cost_drone = weight * 14.25 

print(f'The cost for drone shipping is {cost_drone}')