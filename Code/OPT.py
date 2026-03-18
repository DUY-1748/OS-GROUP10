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

