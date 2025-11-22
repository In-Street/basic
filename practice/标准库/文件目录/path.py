import os
print(os.path.abspath('.'))  # 获取当前文件的绝对路径

print(os.path.exists('/Users/chengyufei/Downloads/未命名.txt'))
print(os.path.isdir('/Users/chengyufei/Downloads'))



from pathlib import Path, PurePosixPath

path = Path('..')

pure_posix_path = PurePosixPath('/Users/chengyufei/Downloads/未命名2.txt')
print(pure_posix_path.name)  # 未命名2.txt

suffix = pure_posix_path.suffix
print(suffix) # 文件后缀  .txt
print(suffix[1:]) # txt  ，从1位截取到最后


#创建文件夹
# Path.mkdir(Path('/Users/chengyufei/Downloads/未命名文件夹2'), parents=True, exist_ok=True)

# 获取path下的所有文件夹
dir_list = [n.name for n in path.iterdir()]
print(dir_list)

walk = Path.walk(Path('/Users/chengyufei/Downloads/dmg/common/pictures/notion'))
print(list(walk))

