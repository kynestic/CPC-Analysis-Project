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
    "education": [
        "learning", "teaching", "curriculum", "classroom", "student", "teacher", "degree", "scholarship", "research", "assessment",
        "university", "college", "syllabus", "pedagogy", "training", "skillset", "literacy", "matriculation", "schooling", "certification",
        "academic", "coursework", "tutoring", "seminar", "lectures", "exams", "evaluation", "onlinelearning", "graduation", "diploma",
        "extracurricular", "attendance", "internship", "mentorship", "qualification", "textbook", "professor", "specialization", "e-learning",
        "innovation", "classmate", "educationpolicy", "literature", "sciencefair", "homeschooling", "achievement", "criticalthinking", "workshop",
        "knowledge", "studyhabits", "assessmenttool"
    ],

    "space": [
        "astronomy", "cosmos", "galaxy", "planet", "telescope", "orbit", "NASA", "spacecraft", "launch", "astronaut",
        "satellite", "solar", "alien", "comet", "gravity", "milkyway", "blackhole", "meteor", "nebula", "interstellar",
        "observatory", "cosmology", "rocket", "mission", "spacestation", "lunar", "martian", "star", "extraterrestrial", "expedition",
        "spaceshuttle", "universe", "astrophysics", "exoplanet", "cosmic", "astronomer", "spacewalk", "aerospace", "rover", "stargazing",
        "orbiting", "spaceexploration", "darkmatter", "wormhole", "ionosphere", "cosmicrays", "gravitation", "probe", "solarsystem",
        "celestial", "planetaryscience"
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
