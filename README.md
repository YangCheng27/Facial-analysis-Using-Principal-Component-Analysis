# Facial-Analysis-Using-Principal-Component-Analysis
For this project, I worked with a portion of the Yale face dataset, which is saved in the 'YaleB_32x32.npy' file and contains 2,414 sample images, each of size 32x32. I utilized eight Python functions to perform PCA on this image dataset.

## Open Source Dataset : [The Yale Face Database](http://cvc.cs.yale.edu/cvc/projects/yalefaces/yalefaces.html)

The Extended Yale B face database consists of 2,414 images of 38 individuals. Each individual has between 59 and 64 images taken under different illumination conditions.

![Figure_2_tenImages](https://github.com/YangCheng27/Facial-analysis-using-Principal-Component-Analysis/assets/56757171/c0c3157d-6a83-47e1-96ac-c56800dfc926)

## Perform PCA analysis using Python with the libraries NumPy, SciPy,matplolib, and Axes3D 
  * **load_npy_dataset(filename):** Load the dataset from the provided .npy file and get the array format information

    <img width="870" alt="Screen Shot 2023-06-22 at 2 05 03 PM" src="https://github.com/YangCheng27/Facial-analysis-using-Principal-Component-Analysis/assets/56757171/eb4edfc2-5ace-4eb5-bace-ce8844e139c9">

   
  * **get_cent_dataset(dataset):** Center the dataset around the origin and return it as a numpy array of floats.
  * **get_covariance_matrix(dataset):** Calculate and return the covariance matrix of the dataset as a numpy matrix array
  * **get_eigenset(matrix, n_components):** Perform eigendecomposition on the covariance matrix. Return a diagonal matrix (as a NumPy array) with the n (n_components) largest eigenvalues on the diagonal in descending order, and a matrix (as a NumPy array) with the corresponding eigenvectors as columns.
  * **get_project_dataset(dataset, eigenVectors):** To project each d × 1 image into your m-dimensional subspace (which is spanned by m vectors of size d × 1), return the new representation as a d × 1 NumPy array.
  * **display_images(origDataset, projDataset, index):** Use matplotlib to display a visual representation of the original image and the projected image side-by-side, given the array index.

![Figure_1_oneImage](https://github.com/YangCheng27/Facial-analysis-using-Principal-Component-Analysis/assets/56757171/2f7cd770-5508-45ae-b2db-6346d5dc6d78)

    
  * **display_ten_images(dataset):** Use Matplotlib to display a visual representation of ten example images.


    --- Original images ---
![Figure_2_tenImages](https://github.com/YangCheng27/Facial-analysis-using-Principal-Component-Analysis/assets/56757171/4b178497-2029-457b-92a9-694311213d9e)

    --- Projection images with 1 largest eigenvalue ---
![Figure_3_tenPCA1](https://github.com/YangCheng27/Facial-analysis-using-Principal-Component-Analysis/assets/56757171/dd3b7820-4e53-498c-912a-c3e2016ef25c)

    --- Projection images with 3 largest eigenvalues ---
![4_pca3](https://github.com/YangCheng27/Facial-analysis-using-Principal-Component-Analysis/assets/56757171/cd7abbac-e83d-4fcf-8f12-d4e9c0533cce)

    --- Projection images with 10 largest eigenvalues ---
![7_pca10](https://github.com/YangCheng27/Facial-analysis-using-Principal-Component-Analysis/assets/56757171/c20a7a9a-7087-40ac-a667-4e84c354a2e0)


  * **visual3D(projDataset):** Use Axes3D to perform visualization of the three largest principal components.
![5_pca3_visual2](https://github.com/YangCheng27/Facial-analysis-using-Principal-Component-Analysis/assets/56757171/67847154-80fc-4ae1-8079-8432b1f6c73f)




