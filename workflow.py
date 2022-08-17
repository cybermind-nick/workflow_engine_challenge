from controller import actionlist, perform_task

'''
	Workflow obkect represents a workflow.
 	It is  a graph structure
	Contains tasks

	@wrkflw: parameter workflow. A dictionary gotten from workflow.json
'''
class Workflow:
	def __init__(self, wrkflw: dict):
		self.user = wrkflw["user"]
		self.tasks = wrkflw["tasks"]
		self.execution_list = []

		# iterate over the tasks and place in a new dictionary
	def build(self):
		for task in self.tasks:
			if not task in actionlist:
				print(f"Task '{task}' not currently supported")
			else:
				self.execution_list.append(str(task.lower()))
        
	def execute_tasks(self):
		for task in self.execution_list:
			perform_task(task, self.user)