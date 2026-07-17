import time

def cal_exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        exec_time = end_time - start_time
        print(f'Total execution time for function {func.__name__}: {exec_time:.5f}')
        # return result
    return wrapper

@cal_exec_time
def run_heavy_load():
    print("🚀 Simulating heavy data processing...")
    time.sleep(2)  # Simulate a 1.5 second delay
    print("✅ Processing finished.")

# 3. Call your function normally
run_heavy_load()

