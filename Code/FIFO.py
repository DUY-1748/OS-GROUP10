def run_fifo(pages, num_frames):
    memory = []
    faults = 0
    history = []
    
    for p in pages:
        is_fault = False
        if p not in memory:
            is_fault = True
            faults += 1
            if len(memory) < num_frames:
                memory.append(p)
            else:
                memory.pop(0) # Đẩy trang vào sớm nhất ra khỏi bộ nhớ
                memory.append(p)
        history.append((p, list(memory), is_fault))
        
    return faults, history

# Test nhanh
if __name__ == "__main__":
    test_pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    frames = 3
    total_faults, _ = run_fifo(test_pages, frames)
    print(f"Số lỗi trang (Page Faults) với {frames} frames là: {total_faults}")