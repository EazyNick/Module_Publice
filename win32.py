import win32api

win32api.Beep(500, 3000) # 500Hz 소리로 3000초동안 소리를 낸다.


pos = win32api.GetCursorPos() # (x, y) 현재 마우스 커서의 위치 반환
print(pos)


pos = (200, 200)
win32api.SetCursorPos(pos) # 200, 200으로 마우스 커서 이동


import win32api
import win32con

def mouse_click(x, y):
    win32api.SetCursorPos((x, y)) #마우스 이동
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) #클릭
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) #클릭 떼기

mouse_click(300, 300) #300, 300 좌표 마우스 클릭


import win32api

# (left, top, right, bottom) 영역으로 마우스 커서 제한하기
win32api.ClipCursor((200, 200, 700, 700))

# 마우스 커서 제한 해제하기
# win32api.ClipCursor((0, 0, 0, 0))
# win32api.ClipCursor()


from win32api import GetSystemMetrics

print('Width:', GetSystemMetrics(0))
print('Height:', GetSystemMetrics(1)) #화면 정보 얻기, 현재 해상도 얻을 수 있다.


import win32api
import win32gui

def rgbint2rgbtuple(RGBint):

    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255 # 색상 값 16진수에서 10진수로 변환

    return (red, green, blue)

color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 500, 500) #500, 500 좌표 rgb값 16진수로 불러옴
print(rgbint2rgbtuple(color))


from win32api import GetLocalTime
#현재 로컬 시간을 튜플 형태로 출력
print(GetLocalTime())


from win32api import GetSystemTime
#현재 시스템 시간을 출력
print(GetSystemTime())


from win32api import GetComputerName
# 컴퓨터 이름 출력
print(GetComputerName())


from win32api import GetUserName
# 사용자 이름 출력
print(GetUserName())


import win32api
# 파일 test.txt을 test_copied.txt라는 파일로 복사
win32api.CopyFile('test.txt', 'test_copied.txt')

#파일 이름 변경
win32api.MoveFile('test_copied.txt', 'test_new.txt')

#파일 위치 이동
win32api.MoveFile('test_new.txt', './new_folder/test_new.txt')

#파일 삭제
win32api.DeleteFile('test.txt')


import win32file

# 폴더 생성
win32file.CreateDirectory('new_folder', None)

# 폴더 삭제
win32file.RemoveDirectory('new_folder')

# 현재 경로 설정
win32file.CreateDirectory('upper_folder', None) # upper_folder 생성
win32file.SetCurrentDirectory('upper_folder') # upper_folder로 이동
win32file.CreateDirectory('new_folder', None) # new_folder 생성

import win32clipboard

# 클립보드에 텍스트 복사하기
win32clipboard.OpenClipboard() #클립보드 열기
win32clipboard.EmptyClipboard() #클립보드 비우기
win32clipboard.SetClipboardText('Text to Clipboard') #복사할 것 입력
win32clipboard.CloseClipboard() # 닫기

# 클립보드에서 텍스트 가져오기
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData() #클립보드에서 텍스트 가져오기
win32clipboard.CloseClipboard()

print(data)
