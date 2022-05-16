import glob

for i in range(1,2001):
    imgs_path_list = glob.glob(f'./front/comp{i}/*')
    if len(imgs_path_list) < 2:
        print(i)

print()
for i in range(1,801):
    imgs_path_list = glob.glob(f'./left/comp{i}/*')
    if len(imgs_path_list) < 2:
        print(i)

print()
for i in range(1,801):
    imgs_path_list = glob.glob(f'./right/comp{i}/*')
    if len(imgs_path_list) < 2:
        print(i)