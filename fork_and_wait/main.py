import os
import sys
import random
import time
# 子プロセスで実行する処理


def some_work() -> int:
    wait_time: int = random.SystemRandom().randint(0, 10)
    pid: int = os.getpid()

    print('Child process works for %d sec (PID:%s)' % (wait_time, pid))
    time.sleep(wait_time)

    return wait_time


if __name__ == '__main__':

    # 5つの子プロセスを生成する
    for i in range(5):
        pid: int = os.fork()
        if pid == 0:  # No pid. so this is child process!
            result: int = some_work()
            child_pid: int = os.getpid()
            print('Child process worked for %d sec. (PID:%s)' %
                  (result, child_pid))
            sys.exit()
        else:
            os.waitpid(pid, 0)
    print('Ended main process (PID: %s)' % os.getpid())
