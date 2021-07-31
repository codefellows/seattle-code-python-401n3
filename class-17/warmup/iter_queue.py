def iterate_queue(input_queue):
    largest = 0 
    while input_queue.front is not None:
        holder = input_queue.dequeue()
        if holder > largest:
            largest = holder
    return largest