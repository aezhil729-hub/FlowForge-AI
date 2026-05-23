import time

def simulate_workflow(workflow):

    logs = []

    trigger = workflow.get("trigger")

    logs.append(f"Trigger detected: {trigger}")

    actions = workflow.get("actions", [])

    for action in actions:

        time.sleep(1)

        logs.append(f"Executing action: {action}")

        logs.append(f"Action completed: {action}")

    logs.append("Workflow execution finished")

    return logs