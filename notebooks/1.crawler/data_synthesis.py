import pandas as pd
import numpy as np
from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 1, 1)
date_range = pd.date_range(start_date, end_date, freq='M')

def generate_CPC():
    return round(np.random.uniform(0.1, 10.0), 2)


# Định nghĩa từ điển chứa các chủ đề và từ khóa
categories = {
    "fashion": [
        "trend", "style", "outfit", "collection", "design", "model", "brand", "fabric", "color", "accessory",
        "runway", "vintage", "chic", "couture", "streetwear", "sustainable", "seasonal", "casual", "footwear", "print",
        "boutique", "fashionista", "elegance", "lookbook", "wardrobe", "tailoring", "makeup", "photography", "influencer",
        "apparel", "high-end", "collection", "online", "menswear", "womenswear", "beauty", "styleguide", "collaboration",
        "elegance", "comfort", "festival", "bohemian", "outfitidea", "athleisure", "preppy", "statement", "layering",
        "accessories", "runwayshow", "personalstyle"
    ],
    "politics": [
        "election", "debate", "policy", "government", "reform", "democracy", "campaign", "party", "senator", "legislation",
        "protest", "diplomacy", "vote", "candidate", "administration", "authority", "nationalism", "leadership", "socialism",
        "conservatism", "capitalism", "populism", "judiciary", "parliament", "scandal", "electioneering", "platform",
        "constituents", "advocacy", "governance", "foreign", "statecraft", "voter", "polling", "mandate", "ethics",
        "accountability", "grassroots", "oversight", "referendum", "civilrights", "negotiations", "dialogue", "tensions",
        "arbitration", "consensus", "representation", "reforms", "initiatives", "treaties"
    ],
    "sport": [
        "football", "basketball", "baseball", "tennis", "cricket", "hockey", "marathon", "swimming", "gymnastics", "wrestling",
        "rugby", "athletics", "boxing", "cycling", "skiing", "skateboarding", "esports", "competition", "tournament", "championship",
        "team", "coach", "fitness", "training", "performance", "endurance", "agility", "strategy", "equipment", "athlete",
        "match", "season", "league", "records", "scores", "highlights", "fanbase", "sponsorship", "sportsmanship", "referee",
        "officiating", "drills", "technique", "warmup", "meditation", "recovery", "injury", "rivalry", "sportsgear", "tournament"
    ],
    "travel": [
        "destination", "adventure", "itinerary", "vacation", "tour", "explore", "passport", "journey", "culture", "sightseeing",
        "accommodation", "backpacking", "local", "travelblog", "flight", "transport", "adventure", "cruise", "city", "beach",
        "resort", "nature", "landmark", "excursion", "guidebook", "hiking", "experience", "relaxation", "travelagent",
        "photography", "travelcommunity", "wanderlust", "budget", "sustainable", "wildlife", "culinary", "heritage", "transportation",
        "vacation", "festival", "citytour", "adventuretravel", "resort", "eco-tourism", "heritage", "historical", "picturesque",
        "destinationwedding", "cruise", "getaway"
    ],
    "game": [
        "gaming", "action", "strategy", "shooter", "adventure", "multiplayer", "puzzle", "platformer", "simulation", "RPG",
        "esports", "console", "PC", "mobile", "indie", "virtual", "reality", "augmented", "MMORPG", "arcade",
        "narrative", "character", "development", "gameplay", "score", "level", "challenge", "community", "fanbase",
        "tournament", "competition", "streaming", "content", "platform", "dev", "update", "release", "trailer",
        "mechanics", "design", "graphics", "art", "soundtrack", "music", "characters", "worldbuilding", "universe"
    ],
    "cooking": [
        "recipe", "cooking", "baking", "grilling", "healthy", "vegetarian", "vegan", "gluten-free", "dessert", "meal",
        "spice", "sauce", "dip", "international", "cuisine", "breakfast", "lunch", "dinner", "snack", "preparation",
        "ingredient", "technique", "kitchen", "cookware", "chef", "flavor", "garnish", "presentation", "fusion", "mealprep",
        "slowcooker", "stirfry", "salad", "soup", "steak", "pasta", "seafood", "sustainable", "seasonal", "comfort",
        "bistro", "cafe", "bakery", "restaurant", "brunch", "catering", "barbecue", "tasting", "menu", "dining"
    ]
}

# In ra danh sách từ khóa cho mỗi chủ đề
for category, keywords in categories.items():
    print(f"Keywords for {category}:")
    print(", ".join(keywords))
    print("\n")



data = []

for date in date_range:
    for category, keywords_list in categories.items():
        random_keywords = np.random.choice(keywords_list, np.random.randint(7, 11), replace=False)
        for item in random_keywords:
            data.append([date, item, generate_CPC()])

df = pd.DataFrame(data, columns=["date", "keyword", "cpc"])

df.to_csv(r'data\synthesis\data.csv', index=False)
