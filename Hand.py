import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils #Drawing Lines of Hand's Node
mp_hands = mp.solutions.hands



class Hand_value:
    def updown_Value(init):
        cam = cv2.VideoCapture(0)  # 0d은 0번째 카메라
        with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            while cam.isOpened():
                success, image = cam.read()
                if not success:
                    continue
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB) #flip = 좌우반전, 색 전처리
                results = hands.process(image)

                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        thumb = hand_landmarks.landmark[4]
                        mid = hand_landmarks.landmark[12]
                        ret = abs(mid.y - thumb.y) * 100  # (중지-엄지) y축값

                        cv2.putText(
                            image, text='Value: %d' % ret, org=(10, 30),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                            color=255, thickness=2)

                        mp_drawing.draw_landmarks(
                            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                if cv2.waitKey(1) == ord('q'):
                    break
            cam.release()
        return ret


    def leftright_Value(init):
        cam = cv2.VideoCapture(0)  # 0d은 0번째 카메라
        with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            while cam.isOpened():
                success, image = cam.read()
                if not success:
                    continue
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB) #flip = 좌우반전, 색 전처리
                results = hands.process(image)

                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        thumb = hand_landmarks.landmark[4]
                        mid = hand_landmarks.landmark[12]
                        ret = abs(mid.x - thumb.x) * 100  # (중지-엄지) x축값

                        cv2.putText(
                            image, text='Value: %d' % ret, org=(10, 30),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                            color=255, thickness=2)

                        mp_drawing.draw_landmarks(
                            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)



                cv2.imshow('image', image)
                if cv2.waitKey(1) == ord('q'):
                    break
            cam.release()
            return ret

    def forwardback_Value(init):
        cam = cv2.VideoCapture(0)  # 0d은 0번째 카메라
        with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            while cam.isOpened():
                success, image = cam.read()
                if not success:
                    continue
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB) #flip = 좌우반전, 색 전처리
                results = hands.process(image)

                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        thumb = hand_landmarks.landmark[4]
                        mid = hand_landmarks.landmark[12]
                        buttom = hand_landmarks.landmark[0]
                        baby = hand_landmarks.landmark[20]
                        ret = abs((mid.y - buttom.y) * (thumb.x - baby.x)) * 100  # 손면적

                        cv2.putText(
                            image, text='Value: %d' % ret, org=(10, 30),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                            color=255, thickness=2)

                        mp_drawing.draw_landmarks(
                            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                cv2.imshow('image', image)
                if cv2.waitKey(1) == ord('q'):
                    break
            cam.release()
            return ret
