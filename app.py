from streamlit_webrtc import webrtc_streamer, RTCConfiguration, VideoProcessorBase
import av
import cv2
import mediapipe as mp
import pickle
import streamlit as st

# Load the trained model outside the recv method
model_dict = pickle.load(open("./model.p", "rb"))
model = model_dict["model"]

# Initialize MediaPipe Hands with mobile-optimized parameters
mp_hands = mp.solutions.hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1  # Consider detecting only one hand to reduce complexity
)

labels_dict = {
    0: 'G', 1: 'U', 2: 'E', 3: 'L', 4: 'P', 5: 'H'
}

st.title("Real-Time Sign Language Recognition")

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        # Downscale the frame to reduce processing load
        small_frame = cv2.resize(frame.to_ndarray(format="bgr24"), (144, 144), interpolation=cv2.INTER_AREA)

        # Convert to RGB
        small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Process the image
        results = mp_hands.process(small_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Simplified drawing for mobile; consider removing drawing to increase performance
                # Draw only the wrist for reference
                wrist = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.WRIST]
                cv2.circle(small_frame, (int(wrist.x * 144), int(wrist.y * 144)), 4, (0, 255, 0), -1)

                # Prepare data for prediction
                data_aux = [landmark.x for landmark in hand_landmarks.landmark] + [landmark.y for landmark in hand_landmarks.landmark]

                # Predict the hand sign
                prediction = model.predict([data_aux])
                predicted_character = labels_dict[int(prediction[0])]

                # Display the predicted character in a simple way
                cv2.putText(small_frame, predicted_character, (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Convert back to AV frame at original resolution for display
        new_frame = av.VideoFrame.from_ndarray(small_frame, format="bgr24")
        return new_frame

# WebRTC configuration optimized for mobile
webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
    rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}),
    layout="mobile"  # This is a hypothetical parameter for demonstration. Adjust layout settings as needed.
)
