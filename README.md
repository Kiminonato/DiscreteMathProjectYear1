# CSS113 Graph Algorithms Project

โปรเจกต์รวมอัลกอริทึมบนกราฟไม่มีทิศทาง (Undirected Weighted Graph) ได้แก่ **DFS**, **BFS**, **Kruskal's MST**, **Prim's MST** และ **Dijkstra's Shortest Path**

## ภาษาและเวอร์ชัน
- Python 3.x (ใช้เฉพาะ Built-in Library: `collections.deque` และ `heapq`)

## วิธีติดตั้ง
ไม่ต้องติดตั้งไลบรารีเพิ่มเติม สามารถรันได้ทันทีหากมี Python 3.x ในเครื่อง

## รูปแบบข้อมูล (Input Format)
ไฟล์ `.txt` ในโฟลเดอร์ชุดทดสอบ โดยบรรทัดแรกเป็นจำนวนโหนด `n` และจำนวนเส้นเชื่อม `m` ตามด้วยเส้นเชื่อม `m` บรรทัด (`u v w`)
```text
6 7
0 1 2
1 2 2
...
```
## วิธีรันและตัวอย่างคำสั่ง
แก้พาธไฟล์ข้อมูลในโค้ดให้ตรงกับไฟล์ที่ต้องการทดสอบ แล้วรันผ่าน Terminal / PowerShell:
python DFS_BFS.py      # ท่องกราฟด้วย DFS และ BFS (กรอกโหนดเริ่มต้น)
python Kruskal.py      # หา Minimum Spanning Tree / Forest ด้วย Kruskal
python Prim.py         # หา Minimum Spanning Tree ด้วย Prim
python Dijkstra.py     # หาเส้นทางสั้นที่สุดด้วย Dijkstra (กรอกโหนดต้นทาง-ปลายทาง)