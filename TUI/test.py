# import urwid
#
#
# def main():
#     urwid.set_encoding('utf8')
#     term = urwid.Terminal(
#         ['python3', '-m', 'IPython', '-i'],
#         env={"TMUX": "TRUE", "TERM": "xterm-256color"},
#         encoding='utf-8'
#     )
#
#     mainframe = urwid.LineBox(
#         urwid.Pile([
#             ('weight', 70, term),
#             ('fixed', 1, urwid.Filler(urwid.Edit('focus test edit: '))),
#         ]),
#     )
#
#     def set_title(widget, title):
#         mainframe.set_title(title)
#
#     def quit(*args, **kwargs):
#         raise urwid.ExitMainLoop()
#
#     def handle_key(key):
#         if key in ('q', 'Q'):
#             quit()
#
#     urwid.connect_signal(term, 'title', set_title)
#     urwid.connect_signal(term, 'closed', quit)
#
#     loop = urwid.MainLoop(
#         mainframe,
#         handle_mouse=False,
#         unhandled_input=handle_key,
#         screen=urwid.raw_display.Screen()
#     )
#
#     term.main_loop = loop
#     loop.run()
#
#
# if __name__ == '__main__':
#     main()

# import pty
# import os
# import time
#
# f = open("/dev/ttys008", "w+")
#
# def master_read(fd):
#     data = os.read(f.fileno(), 1024)
#     f.write(str(data))
#     return data
#
# def master_stdin(fd):
#     data = os.read(f.fileno(), 1024)
#     f.write(str(data))
#     return data
#
# # fd = pty.spawn("ipython3")
# #
# pid, fd = os.openpty()
# print(os.ttyname(fd))
# time.sleep(10000)

import glob

files = glob.glob("/tmp/Libflier_Log*")
if len(files) > 0:
    print(f"Logが {len(files)} 個見つかりました")


print(files)




