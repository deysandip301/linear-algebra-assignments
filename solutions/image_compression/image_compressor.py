from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import hashlib

def compress_image(image):
    # Determine the number of singular values to keep based on the compression percentage
    percent = int(input("Enter compression percentage "))
    # print(image.shape[:2])
    r = int(min(image.shape[:2]) *(1 - percent / 100))

    # Split the color image into its RGB components
    r_vals = image[:, :, 0]  # Red channel
    g_vals = image[:, :, 1]  # Green channel
    b_vals = image[:, :, 2]  # Blue channel
    
    # Perform SVD separately for each color channel
    U_r, S_r, Vt_r = np.linalg.svd(r_vals, full_matrices=False)
    U_g, S_g, Vt_g = np.linalg.svd(g_vals, full_matrices=False)
    U_b, S_b, Vt_b = np.linalg.svd(b_vals, full_matrices=False)
    
    # Compress each color channel based on the compression level
    r_approx = U_r[:, :r] @ np.diag(S_r[:r]) @ Vt_r[:r, :]
    g_approx = U_g[:, :r] @ np.diag(S_g[:r]) @ Vt_g[:r, :]
    b_approx = U_b[:, :r] @ np.diag(S_b[:r]) @ Vt_b[:r, :]
    
    # Clip pixel values to the valid range (0 to 255)
    r_approx = np.clip(r_approx, 0, 255)
    g_approx = np.clip(g_approx, 0, 255)
    b_approx = np.clip(b_approx, 0, 255)
    
    # Reconstruct the compressed RGB image
    compressed_image = np.stack((r_approx, g_approx, b_approx), axis=-1)
    
    return compressed_image

def add_digital_fingerprint(image):
    # Generate a unique fingerprint for the image
    fingerprint = hashlib.md5(image.tobytes()).hexdigest()
    
    # Add the fingerprint as text to the bottom of the image
    plt.text(10, image.shape[0] - 10, f"Digital Fingerprint: {fingerprint}", color='white')
    
    return image

def main(image_path):
    # Read the color image
    color_image = imread(image_path)
    
    # Compress the image
    compressed_image = compress_image(color_image)
    
    # Add digital fingerprint
    fingerprinted_image = add_digital_fingerprint(compressed_image)
    
    # Display the compressed and fingerprinted image
    plt.imshow(fingerprinted_image.astype('uint8'))  # Ensure pixel values are uint8
    plt.axis('off')
    plt.savefig('output.png')
    print(f"Compressed and fingerprinted image saved as output.png")
    
image_path = 'demo_picture.jpg'  # Path to the color image
main(image_path)