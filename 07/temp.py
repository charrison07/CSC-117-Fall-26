def check_weather(temp, precip):
    if temp > 60 and precip == "Sunny":
        return "It's a great day for outdoor activities!"
    elif temp > 60 and precip == "Rainy":
        return "It's warm but rainy. You might want to stay indoors."
    elif temp <= 60 and precip == "Sunny":
        return "It's a bit chilly, but sunny. Dress warmly if you go outside."
    elif temp <= 60 and precip == "Rainy":
        return "It's cold and rainy. Best to stay indoors."
    