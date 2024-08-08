from collections import defaultdict, deque

class TaskScheduler:
    def __init__(self, tasks, dependencies, durations):
        self.tasks = tasks
        self.dependencies = dependencies
        self.durations = durations
        self.graph = defaultdict(list)
        self.in_degree = {t: 0 for t in tasks}
        self.est = {t: 0 for t in tasks}  # Earliest start time
        self.eft = {t: 0 for t in tasks}  # Earliest finish time
        self.lst = {t: float('inf') for t in tasks}  # Latest start time
        self.lft = {t: float('inf') for t in tasks}  # Latest finish time
        self._build_graph()

    def _build_graph(self):
        for u, v in self.dependencies:
            self.graph[u].append(v)
            self.in_degree[v] += 1

    def _topological_sort(self):
        topo_order = []
        queue = deque([t for t in self.tasks if self.in_degree[t] == 0])

        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v in self.graph[u]:
                self.in_degree[v] -= 1
                if self.in_degree[v] == 0:
                    queue.append(v)
        
        return topo_order

    def calculate_times(self):
        topo_order = self._topological_sort()

        for t in topo_order:
            self.eft[t] = self.est[t] + self.durations[t]
            for v in self.graph[t]:
                self.est[v] = max(self.est[v], self.eft[t])

        last_task = topo_order[-1]
        self.lft[last_task] = self.eft[last_task]
        self.lst[last_task] = self.lft[last_task] - self.durations[last_task]

        for t in reversed(topo_order):
            for v in self.graph[t]:
                self.lft[t] = min(self.lft[t], self.lst[v])
            self.lst[t] = self.lft[t] - self.durations[t]

    def earliest_completion_time(self):
        return max(self.eft.values())

    def latest_completion_time(self):
        return max(self.lft.values())

def main():
    
    n = int(input("Enter the number of tasks: "))
    tasks = []
    durations = {}
    
    for i in range(n):
        task_name = input(f"Enter the name of task {i + 1}: ")
        duration = int(input(f"Enter the duration of {task_name}: "))
        tasks.append(task_name)
        durations[task_name] = duration
    
    m = int(input("Enter the number of dependencies: "))
    dependencies = []
    
    for i in range(m):
        u = input(f"Enter the task that must be completed before task {i + 1}: ")
        v = input(f"Enter the task that depends on {u}: ")
        dependencies.append((u, v))
    
    scheduler = TaskScheduler(tasks, dependencies, durations)
    scheduler.calculate_times()
    
    print("Earliest time all tasks will be completed:", scheduler.earliest_completion_time())
    print("Latest time all tasks will be completed:", scheduler.latest_completion_time())

if __name__ == "__main__":
    main()
