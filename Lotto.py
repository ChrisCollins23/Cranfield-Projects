import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from random import randint


# Get the number of games to play from player
num_iterations = int(input("How many lines would you like to play: "))

i = 0
while i < num_iterations: # Generate the number of lines to play
    # Load previous winning numbers from file
    data = pd.read_excel("lotonumbers.xlsx")

    # Split the data into features (X) and target (y)
    X = data[['1st_number', '2nd_number', '3rd_number', '4th_number', '5th_number', '6th_number']]
    y = data.iloc[:, 1:]

    # Train a Random Forest Regression model
        # default is 100 trees in the forest, but we can increase it by adjusting the n_estimators parameter
    model = RandomForestRegressor(n_estimators=1000, random_state=None)
    model.fit(X, y)

    # Generate a new set of random features for prediction
    new_data = pd.DataFrame({
        "1st_number": [randint(1, 59) for _ in range(100)], # 100 random numbers between 1 and 59
        "2nd_number": [randint(1, 59) for _ in range(100)], 
        "3rd_number": [randint(1, 59) for _ in range(100)],
        "4th_number": [randint(1, 59) for _ in range(100)],
        "5th_number": [randint(1, 59) for _ in range(100)],
        "6th_number": [randint(1, 59) for _ in range(100)], # 100 random numbers between 1 and 59
    })

    # Use the trained model to predict the next 6 numbers for each set of features
    predictions = model.predict(new_data)

    # Get the most likely set of numbers based on the predictions
    most_likely_set = predictions[0]
    for p in predictions:
        if p[0] > most_likely_set[0]:
            most_likely_set = p

    # Convert most_likely_set to whole numbers
    rounded_most_likely_set = [round(x) for x in most_likely_set]

    # Print the most likely set of numbers
    print(str(f"{i+1:02d}") + ". The most likely set of numbers for this draw are:", rounded_most_likely_set)
    i += 1