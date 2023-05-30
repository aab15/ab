class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def sort_by_profit(job):
    return job.profit

def schedule_jobs(jobs):
    jobs.sort(key=sort_by_profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)

    slots = [-1] * max_deadline
    scheduled_jobs = []
    total_profit = 0

    for job in jobs:
        for slot in range(job.deadline - 1, -1, -1):
            if slots[slot] == -1:
                slots[slot] = job.id
                scheduled_jobs.append(job)
                total_profit += job.profit
                break

    print("Scheduled jobs:", end=" ")
    for job in scheduled_jobs:
        print(job.id, end=" ")
    print()

    return total_profit

n = int(input("Enter the number of jobs you want to enter: "))
jobs = []
print("Enter the details of the jobs:")
for i in range(n):
    print("Job", i + 1, ":")
    id = int(input("Enter the id of the job: "))
    profit = int(input("Enter the profit of the job: "))
    deadline = int(input("Enter the deadline of the job: "))
    jobs.append(Job(id, deadline, profit))

total_profit = schedule_jobs(jobs)
print("Total profit:", total_profit)