# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  print(c_temp)

f100_in_celcius = f_to_c(100)
print()


def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  print(f_temp)


c0_in_fahrenheit = c_to_f(0)
print()


def get_force(mass, acceleration):
  train_force = mass * acceleration
  return train_force


train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force")

print()
def get_energy(mass, c= 3 * 10**8):
 bomb_energy = (mass * c**2) * bomb_mass
 return bomb_energy


bomb_energy = get_energy(bomb_mass)
print(f'A 1kg bomb supplies {bomb_energy} Joules')

print()
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print(f'The GE train does {train_work} Joules of work over {train_distance} meters')