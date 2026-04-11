from collections import OrderedDict

def run_lru(pages, num_frames):
    memory = OrderedDict()
    faults = 0
    history = []

    for page in pages:
        page_fault = False

        if page in memory:
            memory.move_to_end(page)
        else:
            faults += 1
            page_fault = True

            if len(memory) >= num_frames:
                memory.popitem(last=False)  # LRU

            memory[page] = True

        history.append((page, list(memory.keys()), page_fault))

    return faults, history