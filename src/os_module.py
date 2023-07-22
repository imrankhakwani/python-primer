import os, shutil, time

# Get current working directory
home = os.getcwd()
print(home)

# Create directory "new" in the current working directory
os.mkdir("new")

# Rename directory "new" to "old"
os.rename("new", "old")

# Remove directory "old" from current working directory
os.rmdir("old")

# List contents of the current working directory
os.system('ls -al')

########################
# Make a backup script #
########################
root_scr_dir = r'./'
root_dst_dir = r'./backup-' + time.asctime()

print(">>>>>>>>>>>>>>>>>>>>Starting Backup<<<<<<<<<<<<<<<<<<")
for src_dir, dirs, files in os.walk(root_scr_dir):
    dst_dir = src_dir.replace(root_scr_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.copy(src_file, dst_dir)
print(">>>>>>>>>>>>>>>>>>>>Backup Complete<<<<<<<<<<<<<<<<<<")

os.system('ls -al')
