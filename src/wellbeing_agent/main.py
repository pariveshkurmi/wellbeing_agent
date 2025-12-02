from wellbeing_agent.crew import WellbeingCrew

def main():
    crew = WellbeingCrew()
    print("\nWellbeing Crew Ready\n")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Take care! See you soon.")
            break

        # Step 1: classify intent
        classify_task = crew.classify_intent(user_input)
        intent_result = crew.get_crew([classify_task]).kickoff(inputs={"user_input": user_input})
        print(f"Router chose: {intent_result}")

        # Step 2: respond based on intent
        agent_key = str(intent_result).strip().lower()
        if f"handle_{agent_key}" in crew.tasks_config["tasks"]:
            response_task = crew.respond_to_intent(agent_key, user_input)
        else:
            response_task = crew.respond_to_intent("knowledge", user_input)

        response = crew.get_crew([response_task]).kickoff(inputs={"user_input": user_input})
        print(f"\n{response}\n")

if __name__ == "__main__":
    main()

# Entry point expected by the crewai CLI
def run():
    return main()