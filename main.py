# import sys
# from recommendations import get_recommendations


# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python main.py <user_id> <n>")
#         sys.exit(1)

#     user_id = int(sys.argv[1])
#     n = int(sys.argv[2])
    
    
#     recommendations = get_recommendations(user_id, n) 
#     print(recommendations)

# import os
# from recommendations import get_recommendations

# if __name__ == "__main__":
#     user_id = int(os.getenv("USER_ID", 1))
#     n = int(os.getenv("N", 5))
    
#     recommendations = get_recommendations(user_id, n)
#     print(recommendations)



import argparse
import os
from recommendations import get_recommendations

def main():
    parser = argparse.ArgumentParser(description="Video Recommendation System")
    parser.add_argument("user_id", type=int, help="User ID")
    parser.add_argument("n", type=int, help="Number of recommendations")
    args = parser.parse_args()

    recommendations = get_recommendations(args.user_id, args.n)
    print(recommendations)

if __name__ == "__main__":
    main()
