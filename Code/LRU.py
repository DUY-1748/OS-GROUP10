def run_lru(pages, num_frames):
    # Khởi tạo mảng tĩnh đại diện cho các Frame cố định của RAM
    memory = [None] * num_frames
    faults = 0
    history = []

    # Dictionary lưu thời điểm sử dụng gần nhất của từng trang
    last_used = {}
    time = 0

    for page in pages:
        time += 1
        page_fault = False

        if page in memory:
            # Trang đã có trong RAM -> Chỉ cập nhật lại thời gian sử dụng
            last_used[page] = time
        else:
            # Lỗi trang (Page Fault)
            faults += 1
            page_fault = True

            # Giai đoạn 1: Nếu RAM vẫn còn khung trống (None)
            if None in memory:
                empty_idx = memory.index(None)
                memory[empty_idx] = page
            # Giai đoạn 2: RAM đã đầy -> Tìm trang LRU để thay thế tại chỗ
            else:
                lru_idx = 0
                min_time = float('inf')
                
                # Quét qua các Frame để xem Frame nào chứa trang có last_used nhỏ nhất
                for i in range(num_frames):
                    mem_p = memory[i]
                    if last_used[mem_p] < min_time:
                        min_time = last_used[mem_p]
                        lru_idx = i  # Bắt được vị trí của Frame cần thay thế
                
                # Ghi đè trực tiếp trang mới lên Frame cũ nhất
                memory[lru_idx] = page

            # Cập nhật thời gian sử dụng cho trang mới
            last_used[page] = time

        # Lọc bỏ giá trị None để tương thích với hàm draw_simulation trong GUI
        current_state = [x for x in memory if x is not None]
        history.append((page, current_state, page_fault))

    return faults, history

