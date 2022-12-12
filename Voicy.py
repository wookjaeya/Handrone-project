import speech_recognition as sr #음성 인식하는 라이브러리
from djitellopy import tello


drone = tello.Tello() #드론객체 생성
drone.connect() #드론과 노트북 연결
print(drone.get_battery()) #현재 드론의 배터리 출력(드론 연결 유무 파악 가능)


class Voices:
    def Command(init):
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

        if "이륙" in said:
            drone.takeoff() #드론이륙
            said = "이륙"
            return "이륙"

        elif "착륙" in said:
            drone.land() #드론착륙
            said = "착륙"
            return "착륙"

        elif "오른쪽" in said:
            drone.send_rc_control(1,0,0,0) #오른쪽으로 이동
            said = "오른쪽"
            return "오른쪽"

        elif "왼쪽" in said:
            drone.send_rc_control(-1,0,0,0) #왼쪽으로 이동
            said = "왼쪽"
            return "왼쪽"

        elif "위" in said:
            drone.send_rc_control(0,0,1,0) #위로 이동
            said = "위"
            return "위"

        elif "아래" in said:
            drone.send_rc_control(0,0,-1,0) #아래로 이동
            said = "아래"
            return "아래"

        elif "앞으로" in said:
            drone.send_rc_control(0,1,0,0) #앞으로 이동
            said = "앞으로"
            return "앞으로"

        elif "뒤로" in said:
            drone.send_rc_control(0,-1,0,0) #뒤로 이동
            said = "뒤로"
            return "뒤로"

        return said
