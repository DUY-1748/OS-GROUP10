def run_lru(pages, num_frames):
    memory = []
    faults = 0
    history = []
    
    # dùng dict để lưu thời điểm sử dụng gần nhất
    last_used = {}
    time = 0

    for page in pages:
        time += 1
        page_fault = False

        if page in memory:
            # cập nhật thời gian sử dụng
            last_used[page] = time
        else:
            faults += 1
            page_fault = True

            if len(memory) < num_frames:
                memory.append(page)
            else:
                # tìm trang ít dùng gần đây nhất (LRU)
                lru_page = min(memory, key=lambda p: last_used[p])
                memory.remove(lru_page)
                memory.append(page)

            last_used[page] = time

        # lưu lịch sử (copy memory để tránh bị thay đổi sau)
        history.append((page, memory.copy(), page_fault))

    return faults, history