import numpy as np
import cv2

def main():
    print("Hello from computer-vision-project!")

    print(f"OpenCV version: {cv2.__version__}")
    print(f"numpy version: {np.__version__}")

    canvas = np.zeros((200,200,3), dtype=np.uint8)
    cv2.putText(canvas, "CV Ready", (30,140), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)

    print(f"canvas matrix shape: {canvas.shape}")
    print("setup verified successfully!")
if __name__ == "__main__":
    main()
