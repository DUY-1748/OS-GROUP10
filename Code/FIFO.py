# File: Code/FIFO.py

def run_fifo(pages, num_frames):
    """
    Hàm mô phỏng thuật toán First-In-First-Out (FIFO)
    
    Args:
        pages (list): Danh sách các trang truy cập (VD: [7, 0, 1, 2, 0, 3, 0, 4])
        num_frames (int): Số lượng khung trang (VD: 3)
        
    Returns:
        tuple: (faults, history)
            - faults (int): Tổng số lỗi trang.
            - history (list): Lịch sử chạy, chứa các tuple (page, memory_state, is_fault)
    """
    
    memory = []
    faults = 0
    history = []
    
    for page in pages:
        is_fault = False
        
        # Nếu trang không có trong bộ nhớ -> Lỗi trang (Page Fault)
        if page not in memory:
            is_fault = True
            faults += 1
            
            # Nếu bộ nhớ đã đầy các khung trang
            if len(memory) == num_frames:
                # Xóa phần tử đầu tiên (trang vào sớm nhất - First In)
                memory.pop(0)
            
            # Thêm trang mới vào cuối bộ nhớ
            memory.append(page)
            
        # Lưu lại bản sao của trạng thái bộ nhớ hiện tại để GUI vẽ giao diện
        # Chú ý: Dùng list(memory) để không bị tham chiếu vùng nhớ
        history.append((page, list(memory), is_fault))
        
    return faults, history

# ==========================================
# Khối code này giúp bạn tự test độc lập file này trước khi ghép vào GUI
if __name__ == "__main__":
    # Test case giống ví dụ trong giáo trình Hệ điều hành
    test_pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    test_frames = 3
    
    total_faults, run_history = run_fifo(test_pages, test_frames)
    
    print(f"--- KẾT QUẢ TEST THUẬT TOÁN FIFO ---")
    print(f"Tổng số lỗi trang (Page Faults): {total_faults}\n")
    print(f"{'Trang':<10} | {'Trạng thái Frame':<20} | {'Kết quả'}")
    print("-" * 50)
    for step in run_history:
        current_page, mem_state, is_fault = step
        status = "Page Fault" if is_fault else "Hit"
        print(f"{current_page:<10} | {str(mem_state):<20} | {status}")