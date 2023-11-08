import win32gui
import Logger

def enum_windows_callback(hwnd, lParam):
    window_title = win32gui.GetWindowText(hwnd)
    if window_title == '카카오톡':
        print(f"Window Title: {window_title}, Handle: {hwnd}")

# EnumWindows 함수 호출()
win32gui.EnumWindows(enum_windows_callback, 0)
Logger.HLOG.debug('파일 찾기 진행')

#윈도우 + L 과 동일
# import ctypes
# ctypes.windll.user32.LockWorkStation()

#pyautogui https://pyautogui.readthedocs.io/en/latest/keyboard.html 참조.