# A program of a simple log system



import datetime


def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open("log.txt", "a") as log_file:
        log_file.write(log_entry)

    print("Log entry added.")

# Example usage
if __name__ == "__main__":
    while True:
        msg = input("Enter log message (or 'exit' to quit): ")
        if msg.lower() == "exit":
            break
        write_log(msg)
