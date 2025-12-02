from crewai import Crew, Agent, Task
from pathlib import Path
import yaml

CONFIG_DIR = Path(__file__).parent / "config"

class WellbeingCrew:
    def __init__(self):
        self.agents_config = yaml.safe_load(open(CONFIG_DIR / "agents.yaml"))
        self.tasks_config = yaml.safe_load(open(CONFIG_DIR / "tasks.yaml"))
        self.agents = {}
        self._register_agents()

    def _register_agents(self):
        for key, data in self.agents_config["agents"].items():
            # Ensure required optional fields exist for current crewai Agent schema
            if "backstory" not in data:
                data["backstory"] = ""
            self.agents[key] = Agent(**data)

    def router_agent(self):
        return self.agents["router_agent"]

    def mood_agent(self):
        return self.agents["mood_agent"]

    def stress_agent(self):
        return self.agents["stress_agent"]

    def sleep_agent(self):
        return self.agents["sleep_agent"]

    def motivation_agent(self):
        return self.agents["motivation_agent"]

    def knowledge_agent(self):
        return self.agents["knowledge_agent"]

    def classify_intent(self, user_input):
        task_conf = self.tasks_config["tasks"]["classify_intent"]
        desc = task_conf["description"]
        expected = task_conf.get("expected_output", "")
        t = Task(description=f"{desc} Input: {user_input}", agent=self.router_agent(), expected_output=expected)
        return t

    def respond_to_intent(self, agent_key, user_input):
        task_conf = self.tasks_config["tasks"][f"handle_{agent_key}"]
        desc = task_conf["description"]
        expected = task_conf.get("expected_output", "")
        t = Task(description=f"{desc} User: {user_input}", agent=self.agents[f"{agent_key}_agent"], expected_output=expected)
        return t

    def get_crew(self, tasks=None):
        return Crew(agents=list(self.agents.values()), tasks=tasks or [])
