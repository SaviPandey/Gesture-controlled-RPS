import cv2
from cvzone.HandTrackingModule import HandDetector
import random
import time
import pyttsx3

# Initialize webcam and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector()
sp = pyttsx3.init()
gestures = ["rock", "paper", "scissors"]

def detect_user_gesture(img):
    hands, img = detector.findHands(img, draw=False)
    if hands:
        lmlist = hands[0]['lmList']  # Landmark list for the first hand
        handphoto = detector.fingersUp(hands[0])  # Get finger status
        return img, handphoto
    else:
        return img, None

def get_computer_gesture():
    return random.choice(gestures)

def get_winner(user_gesture, computer_gesture):
    if user_gesture == computer_gesture:
        sp.say("It's a tie")
        sp.runAndWait()
        return "It's a tie!"
    elif (user_gesture == "rock" and computer_gesture == "scissors") or \
         (user_gesture == "paper" and computer_gesture == "rock") or \
         (user_gesture == "scissors" and computer_gesture == "paper"):
        sp.say("You Win")
        sp.runAndWait()
        return "You win!"
    else:
        sp.say("Computer Wins")
        sp.runAndWait()
        return "Computer wins!"

def findGestures(lmlist):
    if lmlist is None:
        return None
    
    if lmlist == [0,0,0,0,0]:  
        sp.say("Rock")
        sp.runAndWait()
        return "rock"
    elif lmlist == [1,1,1,1,1]: 
        sp.say("Paper")
        sp.runAndWait()
        return "paper"
    elif lmlist == [0, 1, 1, 0, 0]:  
        sp.say("Scissors")
        sp.runAndWait()
        return 'scissors'
    else:
        return None

while True:
    status, img = cap.read()
    
    if not status:
        break
    
    user_img, user_lmList = detect_user_gesture(img)
    if user_lmList:
        user_gesture = findGestures(user_lmList)
        if user_gesture:
            computer_gesture = get_computer_gesture()
            print(user_gesture, computer_gesture.capitalize())
            winner = get_winner(user_gesture, computer_gesture)
            print(winner)
            time.sleep(2)
    
    cv2.imshow("myphoto", img)
    
    if cv2.waitKey(10) == 13:  
        break

cap.release()
cv2.destroyAllWindows()
