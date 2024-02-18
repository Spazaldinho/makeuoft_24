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
        image = frame.to_ndarray(format="bgr24")

        # Downscale the image for processing efficiency
        target_width = 144  # Example width, adjust as necessary
        height, width, _ = image.shape
        scale_ratio = target_width / width
        target_height = int(height * scale_ratio)
        image = cv2.resize(image, (target_width, target_height))

        # Convert the image from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image with MediaPipe Hands
        results = mp_hands.process(image)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Previously here would be the drawing code for the skeleton, which we now omit

                # Prepare data for prediction
                data_aux = []
                for landmark in hand_landmarks.landmark:
                    data_aux.extend([landmark.x, landmark.y])

                # Predict the hand sign
                prediction = model.predict([data_aux])
                predicted_character = labels_dict[int(prediction[0])]

                # Display the predicted character on the image
                # Adjust the position and scale of the text as needed for clarity
                cv2.putText(image, f"Predicted: {predicted_character}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Convert the processed image back to an AV frame
        new_frame = av.VideoFrame.from_ndarray(image, format="bgr24")
        return new_frame

# WebRTC configuration optimized for mobile
webrtc_streamer(key="example", video_processor_factory=VideoProcessor,
                media_stream_constraints={"video": True, "audio": False},
                rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}))

