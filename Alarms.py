import time

import datetime as datetime
import schedule
import threading
import uuid

tasks = {}


def run_at(after_time: datetime, callback):
    tag = uuid.uuid4()
    tasks[tag] = (after_time, callback)
    return tag


def remove_schedule(tag):
    if tag in tasks: tasks.pop(tag)


def run_continuously(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


def background_job():
    # print("Running at " + str(datetime.datetime.now()))
    remove_tags = set()
    for tag in list(tasks):
        after_time, callback = tasks[tag]
        if datetime.datetime.now() > after_time:
            remove_tags.add(tag)
            callback()

    for remove_tag in remove_tags:
        if remove_tag in tasks:
            tasks.pop(remove_tag)


schedule.every().second.do(background_job)
stop_run_continuously = run_continuously()
