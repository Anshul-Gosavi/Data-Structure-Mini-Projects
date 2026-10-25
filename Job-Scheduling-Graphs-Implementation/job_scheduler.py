"""Arrange event tasks according to their prerequisites using a graph."""


def find_order(tasks, prerequisites):
    """Return a possible task order and whether a cycle prevents full ordering."""
    connections = {task: [] for task in tasks}
    required_count = {task: 0 for task in tasks}

    for first, next_task in prerequisites:
        connections[first].append(next_task)
        required_count[next_task] += 1

    ready_tasks = []
    for task in tasks:
        if required_count[task] == 0:
            ready_tasks.append(task)

    order = []
    front = 0

    while front < len(ready_tasks):
        task = ready_tasks[front]
        front += 1
        order.append(task)

        for next_task in connections[task]:
            required_count[next_task] -= 1
            if required_count[next_task] == 0:
                ready_tasks.append(next_task)

    cycle_found = len(order) != len(tasks)
    return order, cycle_found


def show_plan(tasks, descriptions, prerequisites):
    print("\nTask list:")
    for task in tasks:
        print("-", task + ":", descriptions[task])

    print("\nPrerequisites:")
    for first, next_task in prerequisites:
        print(first, "must be completed before", next_task)

    order, cycle_found = find_order(tasks, prerequisites)

    if cycle_found:
        print("\nThese prerequisites contain a cycle.")
        print("A complete task order cannot be made.")
    else:
        print("\nSuggested task order:")
        for number in range(len(order)):
            task = order[number]
            print(str(number + 1) + ".", task + " -", descriptions[task])


def main():
    event_tasks = ["Select date", "Book hall", "Invite guests", "Arrange sound", "Hold event"]
    event_descriptions = {
        "Select date": "Choose a suitable day",
        "Book hall": "Reserve the event location",
        "Invite guests": "Send invitations after the hall is booked",
        "Arrange sound": "Prepare the sound system at the hall",
        "Hold event": "Run the event after preparations are complete",
    }
    event_prerequisites = [
        ("Select date", "Book hall"),
        ("Book hall", "Invite guests"),
        ("Book hall", "Arrange sound"),
        ("Invite guests", "Hold event"),
        ("Arrange sound", "Hold event"),
    ]

    while True:
        print("\nEVENT TASK SCHEDULER")
        print("1. Show event task order")
        print("2. Show what happens with a cycle")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_plan(event_tasks, event_descriptions, event_prerequisites)
        elif choice == "2":
            cycle_tasks = ["Prepare", "Run", "Review"]
            cycle_descriptions = {
                "Prepare": "Prepare the activity",
                "Run": "Run the activity",
                "Review": "Review the activity",
            }
            cycle_prerequisites = [
                ("Prepare", "Run"),
                ("Run", "Review"),
                ("Review", "Prepare"),
            ]
            show_plan(cycle_tasks, cycle_descriptions, cycle_prerequisites)
        elif choice == "3":
            print("Scheduler closed.")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()