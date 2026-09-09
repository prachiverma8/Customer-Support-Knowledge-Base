import json

with open("knowledge_base.json", "r") as file:
    knowledge = json.load(file)

print("CUSTOMER SUPPORT KNOWLEDGE REPOSITORY")
print("Available problems:")

for key in knowledge:
    print("-", key)

problem = input("\nEnter problem: ").lower().replace(" ", "_")

if problem in knowledge:
    print("\nProblem:", knowledge[problem]["problem"])
    print("Solution:", knowledge[problem]["solution"])
else:
    print("No solution found in the knowledge repository.")
