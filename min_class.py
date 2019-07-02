def findMaximumClassroomsRequired(timeIntervals):
    eventList = []

    for (start, end) in timeIntervals:
        eventList.append((start, "start"))
        eventList.append((end, "end"))
    
    eventList.sort()

    classroomsRequired = 0
    maxClassroomsRequired = 0
    
    for (time, event) in eventList:
        if event == "start":
            classroomsRequired += 1
        elif event == "end":
            classroomsRequired -= 1
        if classroomsRequired > maxClassroomsRequired:
            maxClassroomsRequired = classroomsRequired
    
    return maxClassroomsRequired

if __name__ == "__main__":
    timeIntervals = [(40,60), (50,70), (30,55)]
    print(findMaximumClassroomsRequired(timeIntervals))
