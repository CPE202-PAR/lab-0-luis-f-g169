# Given earth weight and planet, returns weight on provided planet
# If string does not match a planet, raise ValueError
def weight_on_planets(pounds: float, planet: str) -> float:
   # write your code here
   new_weight: float = 0.0
   if planet == "Mars":
      new_weight = pounds * .38
   elif planet == "Jupiter":
      new_weight = pounds * 2.34
   elif planet == "Venus":
      new_weight = pounds * .91
   else:
      raise ValueError
   return new_weight

if __name__ == '__main__':    # pragma: no cover
   pounds = float(input("What do you weigh on earth? "))
   print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
         "\nOn Venus you would weigh", weight_on_planets(pounds, 'Venus'), "pounds.\n" +
          "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.")