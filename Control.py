from djitellopy import Tello
import Voicy
import Handy

Hand = Handy.Hand_value()
Voice = Voicy.Voices()

def Controller():
    ret = Voice.Command()
    if ret == "오른쪽" and "왼쪽":
        Hand.leftright_Value()
    elif ret == "위" and "아래":
        Hand.updown_Value()
    elif ret == "앞으로" or "뒤로":
        Hand.forwardback_Value()




