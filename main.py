import json
from workflow import Workflow
from actions import build_action_list

def main():
	build_action_list()
	wrkflw = None
	try:
		with open("workflow.json", "r") as t:
			wrkflw = json.load(t)
	except:
		print("Workflow file not available")

	flow = Workflow(wrkflw)

	flow.build()
	flow.execute_tasks()

if __name__ == "__main__":
	main()