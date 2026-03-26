def run_opt(pages, num_frames):
    """
    
    input
    - pages (list): Danh sách các trang truy cập (VD: [7, 0, 1, 2, 0, 3, 0, 4])
    - num_frames (int): Số lượng khung trang (VD: 3)
    
    output return về 2 biến này nha
    1. faults (int): Tổng số lỗi trang.
    2. history (list): Lịch sử chạy. Mỗi phần tử là 1 tuple có dạng: 
       (trang_đang_xét, [trạng_thái_bộ_nhớ], có_bị_lỗi_trang_không)
       VD: (7, [7], True)
    """
    
    memory = []
    faults = 0
    history = []
   
    return faults, history

    for i in range(len(pages)):
        page = pages[i]
        page_fault = False

        # 1. Kiểm tra nếu trang đã có trong bộ nhớ (Hit)
        if page in memory:
            page_fault = False
        else:
            # 2. Nếu trang chưa có trong bộ nhớ (Miss/Fault)
            faults += 1
            page_fault = True

            if len(memory) < num_frames:
                # Nếu RAM còn chỗ trống, nạp trang vào
                memory.append(page)
            else:
                # Nếu RAM đầy, tìm trang để thay thế (Victim Page) bằng cách nhìn tương lai
                victim_idx = -1
                furthest_usage = -1
                
                for m_idx in range(len(memory)):
                    current_page = memory[m_idx]
                    
                    try:
                        # Tìm lần xuất hiện kế tiếp của trang này (từ i + 1 trở đi)
                        next_usage = pages.index(current_page, i + 1)
                    except ValueError:
                        # Nếu không bao giờ xuất hiện lại, đây là nạn nhân tốt nhất
                        victim_idx = m_idx
                        break
                    
                    # Cập nhật trang có khoảng cách đến lần dùng kế tiếp xa nhất
                    if next_usage > furthest_usage:
                        furthest_usage = next_usage
                        victim_idx = m_idx
                
                # Thay thế trang cũ tại vị trí victim_idx bằng trang mới
                memory[victim_idx] = page

        # 3. Lưu lại lịch sử (dùng memory.copy() để tránh lỗi tham chiếu danh sách)
        history.append((page, memory.copy(), page_fault))

    return faults, history


   # Test thử với dữ liệu bạn cung cấp
input_pages = [7, 0, 1, 2, 0, 3, 0, 4]
n_frames = 3

total_faults, run_history = run_opt(input_pages, n_frames)

print(f"Tổng số lỗi trang: {total_faults}")
for step in run_history:
    print(step)
