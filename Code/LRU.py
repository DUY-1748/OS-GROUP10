from collections import OrderedDict

def run_lru(pages, num_frames):
    if num_frames <= 0:
        return len(pages), [
            {"page": p, "memory": [], "fault": True} for p in pages
        ]

    memory = OrderedDict()
    faults = 0
    history = []

    for page in pages:
        page_fault = page not in memory

        if page_fault:
            faults += 1
            if len(memory) >= num_frames:
                memory.popitem(last=False)

        else:
            memory.move_to_end(page)

        memory[page] = True

        history.append({
            "page": page,
            "memory": list(memory.keys()),
            "fault": page_fault
        })

    return faults, history
