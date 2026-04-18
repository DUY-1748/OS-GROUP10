def run_fifo(pages, num_frames):
    # Khởi tạo mảng tĩnh đại diện cho các Frame (Ví dụ: [None, None, None])
    memory = [None] * num_frames
    faults = 0
    history = []
    
    # Con trỏ đánh dấu vị trí Frame cũ nhất sẽ bị thay thế
    pointer = 0 
    
    for p in pages:
        is_fault = False
        
        # Nếu trang p chưa có trong bộ nhớ
        if p not in memory:
            is_fault = True
            faults += 1
            
            # Ghi đè trang mới vào vị trí con trỏ hiện tại
            memory[pointer] = p
            
            # Nhích con trỏ sang Frame tiếp theo. 
            # Dùng phép chia lấy dư (%) để con trỏ vòng lại 0 khi vượt quá num_frames
            pointer = (pointer + 1) % num_frames 
            
        # Lọc bỏ giá trị None để tương thích với hàm draw_simulation trong GUI
        current_state = [x for x in memory if x is not None]
        history.append((p, current_state, is_fault))
        
    return faults, history
