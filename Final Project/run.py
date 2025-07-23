# import cv2
# from emotion_detector import detect_emotion
# from voice_feedback import speak_emotion

# cap = cv2.VideoCapture(0)
# last_emotion = None

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     emotion = detect_emotion(frame)
    
#     if emotion != last_emotion:
#         speak_emotion(emotion)
#         last_emotion = emotion

#     cv2.putText(frame, f"Emotion: {emotion}", (10, 30), 
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
#     cv2.imshow("Webcam Feed", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import time
# from emotion_detector import detect_emotion
# from voice_feedback import speak_emotion

# def main():
#     print("🔴 Starting webcam...")
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("❌ Cannot access the webcam.")
#         return

#     last_spoken_time = 0
#     cooldown_seconds = 3
#     frame_count = 0
#     start_time = time.time()

#     try:
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 print("⚠️ Failed to grab frame.")
#                 continue

#             # Emotion Detection
#             emotion = detect_emotion(frame)

#             # FPS Calculation
#             frame_count += 1
#             elapsed_time = time.time() - start_time
#             fps = frame_count / elapsed_time if elapsed_time > 0 else 0

#             # Speak Emotion every 3 seconds
#             current_time = time.time()
#             if emotion != "Unknown" and (current_time - last_spoken_time) > cooldown_seconds:
#                 print(f"🧠 Detected Emotion: {emotion}")
#                 speak_emotion(emotion)
#                 last_spoken_time = current_time

#             # Display emotion and FPS
#             cv2.putText(frame, f"Emotion: {emotion}", (10, 30),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             cv2.putText(frame, f"FPS: {fps:.2f}", (10, 60),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

#             cv2.imshow("Real-Time Emotion Detection", frame)

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 print("🛑 Quitting...")
#                 break

#     finally:
#         cap.release()
#         cv2.destroyAllWindows()
#         print("✅ Camera and windows released.")

# if __name__ == "__main__":
#     main()

import cv2
from deepface import DeepFace
from voice_feedback import speak_emotion

def main():
    print("🔴 Starting webcam...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Cannot access the webcam.")
        return

    last_emotion = None

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Failed to grab frame.")
                break

            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion'].capitalize()
            except Exception as e:
                print(f"⚠️ Emotion detection error: {e}")
                emotion = "Unknown"

            if emotion != last_emotion and emotion != "Unknown":
                print(f"🧠 Detected Emotion: {emotion}")
                speak_emotion(emotion)
                last_emotion = emotion

            # Display the emotion on the video frame
            cv2.putText(frame, f"Emotion: {emotion}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Real-Time Emotion Detection", frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("👋 Quitting...")
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("✅ Resources released.")

if __name__ == "__main__":
    main()