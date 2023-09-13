import time
import subprocess


def run_batch_script():
    return subprocess.Popen("runNewJenkins.bat", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


def main():
    process = run_batch_script()

    while True:
        time.sleep(5)
        line = process.stdout.readline().decode().strip()
        if line:
            print(line)
            if "terminated" in line:
                print("Detected 'terminated' in output. Restarting...")
                process.terminate()
                process.wait()
                process = run_batch_script()

        if process.poll() is not None:
            print("Batch script terminated. Restarting...")
            process = run_batch_script()





if __name__ == '__main__':
    main()

