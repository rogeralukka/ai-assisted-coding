"""
Task 5: Transparency in AI Recommendations
AI Assisted Coding Lab 5

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def recommend_products(user_profile, product_catalog, top_k=2):
    """
    Explainable Content-Based Recommendation System:
    Calculates multi-attribute affinity scores and provides clear, human-readable rationale.
    """
    recommendations = []
    user_pref_cats = set(user_profile.get("preferred_categories", []))
    max_budget = user_profile.get("max_budget", float("inf"))
    user_pref_brand = user_profile.get("preferred_brand")

    for item in product_catalog:
        score = 0
        reasons = []

        # Category Interest Factor (+40 pts)
        if item["category"] in user_pref_cats:
            score += 40
            reasons.append(f"Matches your interest in '{item['category']}'")

        # Budget Compatibility Factor (+30 pts)
        if item["price"] <= max_budget:
            savings = max_budget - item["price"]
            score += 30
            reasons.append(f"Within budget (${item['price']} <= ${max_budget}, saves ${savings:.2f})")
        else:
            reasons.append(f"Exceeds budget limit (${item['price']} > ${max_budget})")

        # Brand Affinity Factor (+20 pts)
        if user_pref_brand and item["brand"] == user_pref_brand:
            score += 20
            reasons.append(f"Manufactured by your favorite brand '{item['brand']}'")

        # Quality Rating Factor (+10 pts)
        if item.get("rating", 0) >= 4.5:
            score += 10
            reasons.append(f"Top-rated product ({item['rating']}/5.0 stars)")

        recommendations.append({
            "name": item["name"],
            "score": score,
            "price": item["price"],
            "category": item["category"],
            "reasons": reasons
        })

    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations[:top_k]


def test_explainable_recommendations():
    print("--- Running Test Assertions for Task 5 (Transparency in AI Recommendations) ---")
    user = {
        "preferred_categories": ["Laptops", "Audio"],
        "max_budget": 1200,
        "preferred_brand": "TechPro"
    }
    catalog = [
        {"name": "TechPro UltraBook 14", "category": "Laptops", "price": 999, "brand": "TechPro", "rating": 4.8},
        {"name": "NoiseCancel Pro Headphones", "category": "Audio", "price": 199, "brand": "SoundWave", "rating": 4.6},
        {"name": "Gaming Desktop Extreme", "category": "Desktops", "price": 2500, "brand": "MegaPower", "rating": 4.9}
    ]

    recs = recommend_products(user, catalog, top_k=2)

    # Test Case 1: Verify top recommendation
    assert recs[0]["name"] == "TechPro UltraBook 14", "Test 1 Failed"
    assert recs[0]["score"] == 100, "Test 1 Failed (Score mismatch)"
    print(f"Assertion 1 Passed: Top recommendation '{recs[0]['name']}' scored 100/100.")

    # Test Case 2: Verify explainable rationale output
    assert len(recs[0]["reasons"]) >= 3, "Test 2 Failed"
    print(f"Assertion 2 Passed: Recommendation includes {len(recs[0]['reasons'])} transparent reasons.")

    # Test Case 3: Over-budget filter evaluation
    desktop_rec = [r for r in recs if r["name"] == "Gaming Desktop Extreme"]
    assert len(desktop_rec) == 0, "Test 3 Failed (Over-budget item ranked top)"
    print("Assertion 3 Passed: Out-of-budget/category items correctly penalized.")

    print("All 3 Assertions passed successfully!")


def main():
    print("=== Task 5: Transparency in AI Recommendations (Explainable AI) ===")
    print("Observed Risk: Black-box recommendation engines obscure algorithmic bias and erode user trust.")
    print("Applied Fix: Built transparent recommender system that pairs suggestions with interpretable reasons.\n")
    test_explainable_recommendations()


if __name__ == "__main__":
    main()
