
# Research Agent

knowledge = {
    "artificial intelligence":
        "AI enables machines to perform tasks that normally require human intelligence.",

    "machine learning":
        "Machine learning allows computers to learn patterns from data.",

    "python":
        "Python is a beginner-friendly programming language used in AI, web development, and automation.",

    "rag":
        "RAG stands for Retrieval-Augmented Generation. It retrieves relevant information before generating an answer.",

    "ai agent":
        "An AI agent observes information, makes decisions, and performs actions to achieve a goal."
}

print("🔎 Welcome to Research Agent!")
print("Topics: AI, machine learning, Python, RAG, AI agent")
print("Type 'exit' to stop.")

while True:
    query = input("\nResearch topic: ").lower().strip()

    if query == "exit":
        print("Research Agent: Research session ended.")
        break

    found = False

    for topic, information in knowledge.items():
        if query in topic or topic in query:
            print("\nResearch Result:")
            print(information)
            found = True

    if not found:
        print("No matching information found.")
        print("Try a topic from the suggested list.")
