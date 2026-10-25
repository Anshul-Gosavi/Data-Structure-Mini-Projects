# Event Task Scheduling with Graphs

## Project Aim
This program finds an order for event preparation tasks when some tasks depend on others. It uses a directed graph and topological sorting.

## Graph Representation
- Each task is a vertex in the graph.
- A directed edge from one task to another means the first task must finish before the second can start.
- The adjacency list stores the tasks that follow each task.
- The in-degree count stores how many prerequisites each task still has.

## Method
The program puts tasks with an in-degree of zero into a queue. It takes tasks from the front, adds each one to the result, and reduces the in-degree of the tasks connected from it. A task is added to the queue when its in-degree reaches zero.

If the result does not contain every task, at least one cycle exists. The dependent tasks in a cycle can never reach an in-degree of zero, so a complete order is not possible.

## Algorithm
1. Make an adjacency list and set every task's in-degree to zero.
2. For every prerequisite pair, add the directed edge and increase the next task's in-degree.
3. Add each zero-in-degree task to a queue.
4. Take a task from the queue and add it to the order.
5. Reduce the in-degree of each task that follows it.
6. Add any task whose in-degree becomes zero to the queue.
7. Continue until the queue has no more tasks.
8. Compare the number of ordered tasks with the total. If they differ, report a cycle.

## Example Scenario
The sample plans an event: choose a date, book a hall, invite guests, arrange sound, and hold the event. Invitations and sound arrangements both depend on booking the hall. The event itself depends on both preparations.

The menu also shows a small cyclic example to demonstrate why such dependencies cannot produce a complete schedule.

## Complexity
For `V` tasks and `E` prerequisite links, the adjacency list and queue method takes `O(V + E)` time and uses `O(V + E)` space.

## Run
From this folder, run:

```text
python job_scheduler.py
```

No external Python packages are needed.