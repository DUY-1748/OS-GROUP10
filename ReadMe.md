# OS Project - Hệ Điều Hành

- **Project Name**: Build an APP for demonstration Virtual Memory management algorithm: LRU, FIFO and OPT
- **Project Code**: OS_VME_08
- **Group Members**: 
    1. [Nguyễn Hoàng Duy] - [080206011748]
    2. [Nguyễn Gia Huy] - [MSSV]
    3. [Lê Minh Khang] - [MSSV]
    4. [Trương Văn Hào]- [MSSV]
    5.
    6.

## Giới thiệu dự án

Dự án tập trung vào việc xây dựng một ứng dụng minh họa các thuật toán quản lý bộ nhớ ảo (Virtual memory), bao gồm:
* Thuật toán LRU (Least Recently Used)
* Thuật toán FIFO (First-In, First-Out)
* Thuật toán OPT (Optimal Page Replacement)

### Repository Structure
Dự án được tổ chức theo đúng yêu cầu đồ án:

```text
OS_VME_08/
│
├── Code/                   # Chứa toàn bộ mã nguồn của ứng dụng
│   ├── main.py             # File khởi chạy 
│   ├── gui.py              # Xử lý giao diện (View & Controller), Export CSV, Stress Test
│   ├── fifo.py             # Logic thuật toán FIFO
│   ├── lru.py              # Logic thuật toán LRU
│   └── opt.py              # Logic thuật toán OPT
│
├── DOCX/                   # Chứa báo cáo chi tiết (Word)
├── Extra/                  # Chứa file Test I/O 
├── PPTX/                   # Chứa slide thuyết trình (PowerPoint)
└── ReadMe.md               # Tổng quan dự án 