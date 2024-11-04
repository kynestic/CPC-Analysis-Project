import pandas as pd
import numpy as np
from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 1, 1)
date_range = pd.date_range(start_date, end_date, freq='D')

def generate_CPC():
    return round(np.random.uniform(0.1, 10.0), 2)


# Định nghĩa từ điển chứa các chủ đề và từ khóa
categories = {
    "education": [
        "learning", "teaching", "curriculum", "classroom", "student", "teacher", "degree", "scholarship", "research", "assessment",
        "university", "college", "syllabus", "pedagogy", "training", "skillset", "literacy", "matriculation", "schooling", "certification",
        "academic", "coursework", "tutoring", "seminar", "lectures", "exams", "evaluation", "online learning", "graduation", "diploma",
        "extracurricular", "attendance", "internship", "mentorship", "qualification", "textbook", "professor", "specialization", "e-learning",
        "innovation", "classmate", "education policy", "literature", "science fair", "homeschooling", "achievement", "critical thinking", "workshop",
        "knowledge", "study habits", "assessment tool"
    ],

    "space": [
        "astronomy", "cosmos", "galaxy", "planet", "telescope", "orbit", "NASA", "spacecraft", "launch", "astronaut",
        "satellite", "solar", "alien", "comet", "gravity", "milky way", "black hole", "meteor", "nebula", "interstellar",
        "observatory", "cosmology", "rocket", "mission", "space station", "lunar", "martian", "star", "extraterrestrial", "expedition",
        "space shuttle", "universe", "astrophysics", "exoplanet", "cosmic", "astronomer", "spacewalk", "aerospace", "rover", "stargazing",
        "orbiting", "space exploration", "dark matter", "wormhole", "ionosphere", "cosmic rays", "gravitation", "probe", "solar system",
        "celestial", "planetary science"
    ],

    "sport": [
        "football", "basketball", "baseball", "tennis", "cricket", "hockey", "marathon", "swimming", "gymnastics", "wrestling",
        "rugby", "athletics", "boxing", "cycling", "skiing", "skateboarding", "esports", "competition", "tournament", "championship",
        "team", "coach", "fitness", "training", "performance", "endurance", "agility", "strategy", "equipment", "athlete",
        "match", "season", "league", "records", "scores", "highlights", "fanbase", "sponsorship", "sportsmanship", "referee",
        "officiating", "drills", "technique", "warmup", "meditation", "recovery", "injury", "rivalry", "sports gear", "tournament"
    ],
    
    "travel": [
        "destination", "adventure", "itinerary", "vacation", "tour", "explore", "passport", "journey", "culture", "sightseeing",
        "accommodation", "backpacking", "local", "travel blog", "flight", "transport", "adventure", "cruise", "city", "beach",
        "resort", "nature", "landmark", "excursion", "guidebook", "hiking", "experience", "relaxation", "travel agent",
        "photography", "travel community", "wanderlust", "budget", "sustainable", "wildlife", "culinary", "heritage", "transportation",
        "vacation", "festival", "city tour", "adventure travel", "resort", "eco-tourism", "heritage", "historical", "picturesque",
        "destination wedding", "cruise", "getaway"
    ],
    
    "cooking": [
        "recipe", "cooking", "baking", "grilling", "healthy", "vegetarian", "vegan", "gluten-free", "dessert", "meal",
        "spice", "sauce", "dip", "international", "cuisine", "breakfast", "lunch", "dinner", "snack", "preparation",
        "ingredient", "technique", "kitchen", "cookware", "chef", "flavor", "garnish", "presentation", "fusion", "meal prep",
        "slow cooker", "stir fry", "salad", "soup", "steak", "pasta", "seafood", "sustainable", "seasonal", "comfort",
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
        random_keywords = np.random.choice(keywords_list, np.random.randint(0, 5), replace=False)
        for item in random_keywords:
            data.append([date, item, generate_CPC()])

df = pd.DataFrame(data, columns=["date", "keyword", "cpc"])

df.to_csv(r'data\synthesis\data.csv', index=False)
