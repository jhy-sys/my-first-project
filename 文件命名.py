import os
import sys

def batch_rename(files, prefix="文件", start_num=1):
    success = 0
    print("==== 开始重命名 ====\n")
    
    for i, file_path in enumerate(files, start_num):
        if not os.path.isfile(file_path):
            continue

        dirname = os.path.dirname(file_path)
        ext = os.path.splitext(file_path)[1]
        new_name = f"{prefix}{i}{ext}"
        new_path = os.path.join(dirname, new_name)

        if os.path.exists(new_path):
            print(f"已存在，跳过：{new_name}")
            continue

        try:
            os.rename(file_path, new_path)
            print(f"✅ {os.path.basename(file_path)} → {new_name}")
            success += 1
        except Exception as e:
            print(f"❌ 失败：{e}")

    print(f"\n🎉 全部完成！成功重命名 {success} 个文件")
    print("="*30)

if __name__ == "__main__":
    print("==== 文件批量重命名工具 ====")
    print("使用方法：把文件拖到本软件上\n")

    if len(sys.argv) < 2:
        print("⚠️  未检测到文件，请把文件拖到软件图标上！")
        sys.exit()

    # 获取拖拽进来的文件
    files = sys.argv[1:]
    batch_rename(files, prefix="文件", start_num=1)