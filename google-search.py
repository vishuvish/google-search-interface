from google import search

# Enter your query
print("Enter your Query")
query = input()

# It will print the first 10 links recommended by google according to your query.

for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(j)
