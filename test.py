import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from random import randint

# Define the games index
games_index = {
    1: "Lotto",
    2: "Thunderball",
    3: "EuroMillions",
}

# Display the games index to the user
print("Available games:")
for key, value in games_index.items():
    print(f"{key}: {value}")

# Get the game choice from the user
game_choice = int(input("Enter the number of the game you want to play: "))

# Get the number of lines to play from player
num_iterations = int(input("How many lines would you like to play: "))

if game_choice == 1:
    i = 0
    while i < num_iterations: # Generate the number of lines to play
        # Load previous winning numbers from file
        data = pd.read_excel("lotonumbers.xlsx")

        # Split the data into features (X) and target (y)
        X = data[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']]  # N = Number of ball
        y = data.iloc[:, 1:]

        # Train a Random Forest Regression model
        # default is 100 trees in the forest, but we can increase it by adjusting the n_estimators parameter
        model = RandomForestRegressor(n_estimators=1000, random_state=None) 
        model.fit(X, y)

        # Generate a new set of random features for prediction
        new_data = pd.DataFrame({
            "N1": [randint(1, 59) for _ in range(100)], # 100 random numbers between 1 and 59, all arrays must be same size
            "N2": [randint(1, 59) for _ in range(100)], # all arrays must be same size
            "N3": [randint(1, 59) for _ in range(100)],
            "N4": [randint(1, 59) for _ in range(100)],
            "N5": [randint(1, 59) for _ in range(100)],
            "N6": [randint(1, 59) for _ in range(100)], 
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

elif game_choice == 2:
    # Placeholder for Thunderball game script
    print("Running Thunderball game script...")
    # Add the Thunderball game script here

elif game_choice == 3:
    # Placeholder for EuroMillions game script
    print("Running EuroMillions game script...")
    # Add the EuroMillions game script here

else:
    print("Invalid game choice.")