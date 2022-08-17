## Workflow challenge
The workflow engine use a simple observer pattern. All implement actions are registered and the corresponding json file must conform to the stated actions.

Conditionals are handled by the implemeted action functions.

Implemented actions:

* send mail: `send_mail()`
* print tasks: `print_task()`
* process payment: `process_payment()`

#### Note: The name of the task in the `workflow.json` file must match  the names written above

### How to use:
1. Create a `workflow.json` file
   
   The file should be structured thus:

	 `{
			"user": "{User name}",
		   "tasks": [_list of tasks_]
		}`

2. Run `python main.py`: windows or `python3 main.py`: Linux and Mac


* A workflow.json file is provided in the repositiory. Feel free to run it as test. It can also be modified within the stated implementation constraints

### PS: This is a basic skeleton to serve as a scaffolding for building a proper workflow engine. It is a Proof of concept.
