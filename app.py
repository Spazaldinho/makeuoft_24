from streamlit_webrtc import webrtc_streamer, RTCConfiguration, VideoProcessorBase
import av
import cv2
import mediapipe as mp
import numpy as np
import pickle
import streamlit as st

# Load the trained model
model_dict = pickle.load(open("./model.p", "rb"))
model = model_dict["model"]

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Updated label dictionary for your model's outputs
labels_dict = {
    0: 'G', 1: 'U', 2: 'E', 3: 'L', 4: 'P', 5: 'H'
}

st.title("Real-Time Sign Language Recognition")

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        image = frame.to_ndarray(format="bgr24")

        # Convert the image from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and get the result
        results = mp_hands.process(image)

        # Convert the image from RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                )

                # Prepare data for prediction
                data_aux = []
                for landmark in hand_landmarks.landmark:
                    data_aux.extend([landmark.x, landmark.y])

                # Predict the hand sign
                prediction = model.predict([data_aux])
                predicted_character = labels_dict[int(prediction[0])]

                # Display the predicted character on the image
                cv2.putText(image, f"Predicted: {predicted_character}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Convert the processed image back to an AV frame
        new_frame = av.VideoFrame.from_ndarray(image, format="bgr24")
        return new_frame

# WebRTC streamer configuration
webrtc_streamer(key="example", video_processor_factory=VideoProcessor,
                media_stream_constraints={"video": True, "audio": False},
                rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}))