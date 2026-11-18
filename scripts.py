import kagglehub

cache_path = kagglehub.dataset_download("marvyaymanhalim/student-performance-and-attendance-dataset", output_dir="datasets")

print(f"✅ Dữ liệu đã tải thành công: {cache_path}")