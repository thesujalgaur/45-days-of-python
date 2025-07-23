# import cv2
# import mediapipe as mp

# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# def detect_emotion(frame):
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = face_mesh.process(rgb_frame)
    
#     # Dummy logic: Replace with ML model or rule-based landmark analysis
#     if results.multi_face_landmarks:
#         # This is where you would classify based on landmarks
#         return "Happy"  # just a placeholder
#     return "Neutral"

from deepface import DeepFace
import cv2

def detect_emotion(frame):
    try:
        # Analyze frame for emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        return emotion.capitalize()
    except Exception as e:
        print(f"[Emotion Detection Error] {e}")
        return "Unknown"