
def makespan(perm, data):
    job_count = len(perm)
    machine_count = len(data)
    
    makespan = [[0] * (machine_count + 1) for _ in range(0, job_count + 1)]
    for i, job in enumerate(perm):
        for machine in range(0, machine_count):
            makespan[i + 1][machine + 1] = max(makespan[i][machine + 1], makespan[i + 1][machine]) + data[machine][job - 1]
    
    return makespan[job_count][machine_count]
