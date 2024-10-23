import pandas as pd
import numpy as np
from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 1, 1)
date_range = pd.date_range(start_date, end_date, freq='M')

def generate_CPC():
    return round(np.random.uniform(0.1, 10.0), 2)


categories = {
    "fashion": [
        "latest fashion", "fashion week", "fall outfits", "summer fashion", "winter collection",
        "fashion trends", "new styles", "vintage fashion", "designer brands", "eco-friendly fashion",
        "sustainable fashion", "street style", "luxury brands", "fast fashion", "celebrity style",
        "fashion magazines", "online fashion stores", "fashion photography", "runway trends", "fashion influencers"
    ],
    "politics": [
        "election results", "political debate", "parliament session", "government policies", "international relations",
        "diplomatic talks", "campaign rallies", "political scandals", "law reforms", "party conventions",
        "policy discussions", "political speeches", "foreign policy", "senate hearings", "voting laws",
        "political protests", "economic policies", "healthcare reforms", "education reforms", "tax policies"
    ],
    "sport": [
        "football match", "Olympic games", "NBA playoffs", "tennis tournament", "cricket world cup",
        "FIFA world cup", "rugby championship", "cycling race", "marathon event", "golf tournament",
        "boxing championship", "MMA fights", "basketball finals", "swimming competition", "track and field events",
        "hockey league", "skiing competition", "volleyball championship", "surfing contest", "climbing competition"
    ],
    "travel": [
        "travel destinations", "cheap flights", "holiday deals", "city tours", "beach vacations",
        "adventure travel", "luxury hotels", "road trips", "backpacking trips", "cultural tours",
        "mountain trekking", "island hopping", "national parks", "cruise vacations", "historical sites",
        "eco-tourism", "wellness retreats", "ski resorts", "desert safaris", "jungle exploration"
    ],
    "game": [
        "new video games", "game releases", "e-sports events", "online multiplayer", "game tournaments",
        "console gaming", "PC gaming", "mobile games", "strategy games", "action games",
        "RPG games", "indie games", "virtual reality games", "augmented reality games", "MMORPG",
        "puzzle games", "simulation games", "adventure games", "sports games", "arcade games"
    ],
    "cooking": [
        "healthy recipes", "cooking tips", "new cookbooks", "baking recipes", "grilling techniques",
        "vegetarian recipes", "vegan meals", "gluten-free recipes", "dessert ideas", "holiday recipes",
        "quick meals", "one-pot recipes", "soups and stews", "sauces and dips", "international cuisines",
        "meal prepping", "barbecue recipes", "comfort food", "keto meals", "low-carb recipes"
    ]
}

data = []

for date in date_range:
    for category, keywords_list in categories.items():
        random_keywords = np.random.choice(keywords_list, np.random.randint(7, 11), replace=False)
        for item in random_keywords:
            data.append([date, item, generate_CPC()])

df = pd.DataFrame(data, columns=["date", "keyword", "cpc"])

df.to_csv(r'data\synthesis\data.csv', index=False)
