# This program asks the user about the current weather condition
weather_condition = str(input('What is weather like today? (sunny/rainy/cold): '))

#Weather advice:

if weather_condition == 'sunny':
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == 'cold':
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")