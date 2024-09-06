# KeyShot-Automated-Camera-Wheel-Render

A Python script for KeyShot that automates the process of rendering four-view images of wheel products from four pre-set cameras. The script rotates the 3D model as needed for each camera view, renders the scene, and saves the output to a specified folder.

## Features

- Renders four-view images of wheel products from four pre-defined cameras in KeyShot.
- Automatically rotates the model to the correct angle for specific camera views.
- Saves rendered images to a user-defined output folder.
- Works with pre-configured materials, lighting, and other scene settings.
- Supports rendering queue processing for efficient batch rendering.

## Requirements

- **KeyShot Software**: Ensure KeyShot is installed and configured properly.
- **Python Environment**: The script runs in the KeyShot scripting environment with access to the KeyShot Python API.
- **Pre-set Cameras**: Four cameras must be pre-configured in the KeyShot scene with a naming convention matching the specified prefix (default is "相机").

## Pre-configured Parameters

- **Render Time**: Set to 60 seconds by default. This can be adjusted by changing the `RENDER_TIME` constant.
- **Output Path**: Rendered images will be saved to `D:\\0-KEYSHOT\\`. Modify the `OUTPUT_PATH` variable to change the output directory.
- **Render Resolution**: The default resolution is set to 2560x2560. Adjust `RENDER_WIDTH` and `RENDER_HEIGHT` for different sizes.
- **Camera Prefix**: The prefix for camera names is set to "相机". You can change `CAMERA_PREFIX` to match your camera naming convention in KeyShot.
- **Rotation Angles**: Specific rotation angles for different cameras are predefined in the `ROTATION_ANGLES` dictionary. These are optimized for wheels, but they can be adjusted for other products as needed.

## Usage Instructions

1. **Set Up Cameras and Scene**: Ensure you have four cameras set up in KeyShot with the required naming convention and desired materials, lighting, and other settings. The script is optimized for rendering four-view images of wheel products.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/zpowin/KeyShot-Automated-Camera-Wheel-Render.git
