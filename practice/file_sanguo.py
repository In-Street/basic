# file.write("諸葛亮|關羽|劉備|曹操|孫權|關羽|張飛|呂布|周瑜|趙雲|龐統|司馬懿|黃忠|馬超")

def read_file(file, seek):
    file.seek(seek)
    print(file.read())


def write_file(file, data):
    file.write(data)


name_path = "doc/name_c.txt"

# 模式参数：读写模式同时打开
#   r+   默认从文件开头读写，文件必须已存在，否则会抛出 FileNotFoundError；写入会覆盖原有内容（需注意指针位置，默认指针偏移量为0，所以会覆盖开头的内容）。
#   w+  文件不存在则创建；打开时会先清空文件，原有内容会丢失
#   a+  文件不存在则创建；写入始终追加到末尾，但读取前需用 seek(0) 移动指针到开头
file = open(name_path, "r+", encoding="utf-8")
print(file.tell())  # 0 , 指针在文件中的偏移量。按字节算，utf-8 中一个中文3字节
file.write("城堡为爱守着秘密")
print(file.tell())  # 24
read_file(file,0)
file.close()

name_path = "doc/name_b.txt"
with open(name_path, "w+", encoding="utf-8") as file:
    print(file.tell())
    file.write("后视镜里的世界")
    print(file.tell())

with open(name_path, "a+", encoding="utf-8") as f:
    print("a+ " + f.tell().__str__())
    f.write("\n不懂的道歉我没那么聪明")
    print(f.tell())
    read_file(f,0)

# close() 、 flush()
#      1.  close() 的核心作用是释放文件资源（如操作系统的文件描述符），并在关闭前自动调用 flush() 确保缓冲区数据写入磁盘。
#           当使用with语句时，with 会在代码块结束后自动调用 close()，无需手动操作。 没有with语句时，需手动调用close

#       2. flush() 作用是强制将缓冲区中的数据立即写入磁盘（不关闭文件，可继续读写）。文件操作中，系统为了提高效率，会将数据先暂存在内存缓冲区（buffer），当缓冲区满、文件关闭（close()）或程序退出时，才会批量写入磁盘
#           手动调用flush，需要数据立即写入磁盘的使用场景： 实时性要求高的场景（监控数据）、多线程共享文件（多线程共享统一文件时，手动flush能确保其他线程及时读到最新数据）
