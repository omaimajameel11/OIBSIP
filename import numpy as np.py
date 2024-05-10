import numpy as np

# User-item matrix representing user preferences
user_item_matrix = np.array([
    [5, 4, 0, 0, 3],
    [0, 0, 5, 4, 4],
    [4, 0, 4, 0, 0],
    [0, 3, 0, 5, 4],
    [3, 4, 0, 0, 5]
])

# Function to recommend items to a user based on collaborative filtering
def recommend_items(user_id, user_item_matrix, num_recommendations=3):
    user_preferences = user_item_matrix[user_id]
    similarities = []

    # Calculate similarity between the user and each other user
    for other_user_id, other_user_preferences in enumerate(user_item_matrix):
        if other_user_id != user_id:
            similarity = np.dot(user_preferences, other_user_preferences) / (
                np.linalg.norm(user_preferences) * np.linalg.norm(other_user_preferences)
            )
            similarities.append((other_user_id, similarity))
    
    # Sort similarities in descending order
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Get top N similar users and recommend items they liked
    recommendations = []
    for other_user_id, similarity in similarities[:num_recommendations]:
        other_user_preferences = user_item_matrix[other_user_id]
        for item_id, rating in enumerate(other_user_preferences):
            if rating > 0 and user_preferences[item_id] == 0:
                recommendations.append((item_id, rating))
    
    return recommendations

# Example usage
user_id = 0
recommendations = recommend_items(user_id, user_item_matrix)
print("Recommendations for User", user_id, ":")
for item_id, rating in recommendations:
    print("Item", item_id, "- Rating:", rating)
