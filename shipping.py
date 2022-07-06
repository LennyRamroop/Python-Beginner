#Lenny Ramroop
#Sal's Shipping mini project - completed on Codecademy

#The Sal's Shipping project demonstrates my use of operators and if/elif/else statements
#We take a single variable and do simple calculations based on weight to determine
#the most cost effective shipping method.

weight = 41.5

#GROUND SHIPPING
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping Cost: $" + str(cost_ground))

#GROUND SHIPPING PREMIUM
cost_ground_premium = 125.00

print('Ground Shipping Premium Cost: $' + str(cost_ground_premium))

#DRONE SHIPPING
if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print('Drone Shipping Cost: $' + str(cost_drone))