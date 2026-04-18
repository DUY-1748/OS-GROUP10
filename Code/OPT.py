def run_opt(pages, num_frames):
    memory = []
    faults = 0
    history = []
    
    for i, p in enumerate(pages):
        is_fault = False
        if p not in memory:
            is_fault = True
            faults += 1
            if len(memory) < num_frames:
                memory.append(p)
            else:
                farthest = -1
                replace_idx = -1
                # Quét nhìn vào tương lai để tìm trang thay thế
                for j, mem_p in enumerate(memory):
                    if mem_p not in pages[i+1:]:
                        replace_idx = j
                        break # Trang này sẽ không bao giờ được dùng lại
                    else:
                        next_use = pages[i+1:].index(mem_p)
                        if next_use > farthest:
                            farthest = next_use
                            replace_idx = j
                memory[replace_idx] = p
        history.append((p, list(memory), is_fault))
        
    return faults, history
