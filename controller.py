'''
	The is the observer implementation
 	The task names are mapped to action functions
'''

actionlist = dict()

# subscribe actions to the actionlist
# action is synonymous to task here. Named for readability
def register_actions(action: str, fn):
    if not action in actionlist:
        actionlist[action] = fn

# execute action
def perform_task(action: str, data):
    fn = actionlist[action]
    fn(data)