import speech_recognition as sr #음성 인식하는 라이브러리
from djitellopy import tello
#from time import sleep
import cv2

drone = tello.Tello() #드론객체 생성
drone.connect() #드론과 노트북 연결
print(drone.get_battery()) #현재 드론의 배터리 출력(드론 연결 유무 파악 가능)


class Voice:
    def voice_Recognition():
        r = sr.Recognizer() #인스턴스 생성

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) #주변 소음이 있는 경우 활성화

            print("Say Command")

            audio = r.listen(source) #음성인식

            print("Recognizing Now....")

            try:
                said = r.recognize_google(audio,language="ko-KR") #said변수에 음성 저장

                print("You said \n" + said)

            except Exception as e:
                print("Error : "+str(e))


        return said

    def command(c):

        if "이륙" in c:
            drone.takeoff() #드론이륙
            return "성공"

        elif "착륙" in c:
            drone.land() #드론착륙
            return "성공"

        elif "오른쪽" in c:
            drone.send_rc_control(10,0,0,0) #오른쪽으로 이동
            return "성공"

        elif "왼쪽" in c:
            drone.send_rc_control(-10,0,0,0) #왼쪽으로 이동
            return "성공"

        elif "위" in c:
            drone.send_rc_control(0,0,10,0) #위로 이동
            return "성공"

        elif "아래" in c:
            drone.send_rc_control(0,0,-10,0) #아래로 이동
            return "성공"

        elif "앞으로" in c:
            drone.send_rc_control(0,10,0,0) #앞으로 이동
            return "성공"

        elif "뒤로" in c:
            drone.send_rc_control(0,-10,0,0) #뒤로 이동
            return "성공"



