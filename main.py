import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from mpl_toolkits.mplot3d import Axes3D

def load_npy_dataset(filename):
    images = np.load(filename)
    information = f"{filename} is a n (Number of sample images = {len(images)}) x d (Number of image features = {len(images[0])}) array."
    return images, information

def get_cent_dataset(dataset):
    return dataset - np.mean(dataset, axis = 0)

def get_covariance_matrix(dataset):
    return np.dot(np.transpose(dataset), dataset) / (len(dataset) - 1 )

def get_eigenset(matrix, n_components):
    eigenValues, eigenVectors = eigh(matrix)
    index = eigenValues.argsort()[::-1]
    eigenValues, eigenVectors = eigenValues[index], eigenVectors[:, index]
    diagonal = np.diag(eigenValues)
    return diagonal[:n_components, :n_components], eigenVectors[:, :n_components]

def get_project_dataset(dataset, eigenVectors):
    projections = np.zeros(dataset.shape)
    for i in range (dataset.shape[0]):
        data = dataset[i]
        for j in range(len(eigenVectors[0])):
            t = eigenVectors[:,j].T@data*eigenVectors[:,j]
            projections[i] += t
    return projections

def display_images(origDataset, projDataset, index):
    origImage = np.transpose(origDataset[index].reshape(32,32))
    projImage = np.transpose(projDataset[index].reshape(32,32))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    ax1.set_title('Original', fontweight="bold")
    ax2.set_title('Projection', fontweight="bold")
    origImage = ax1.imshow(origImage, aspect = 'equal')
    projImage = ax2.imshow(projImage, aspect = 'equal')
    fig.colorbar(origImage, ax = ax1)#, shrink=0.75)
    fig.colorbar(projImage, ax = ax2)#, shrink=0.9)
    plt.show()

def display_ten_images(dataset):
    images = [np.transpose(dataset[i].reshape(32,32)) for i in [0, 100, 1937, 2001, 1308, 1200, 1400, 1600, 650, 2400]]
    fig, ax = plt.subplots(2, 5, figsize=(14, 6))
    for i in range(2):
        for j in range(5):
            ax[i][j].set_title(f'image{i*5 + j + 1}', fontweight="bold")
            img = ax[i][j].imshow(images[i*5 + j], aspect = 'equal')
            #fig.colorbar(img, ax=ax[i][j])
    cbar_ax = fig.add_axes([0.92, 0.075, 0.02, 0.85])  
    fig.colorbar(img, cax=cbar_ax)
        
    plt.tight_layout(rect=[0, 0, .9, 1])

    plt.show()

def visual3D(projDataset):
    x_proj_values = []
    y_proj_values = []
    z_proj_values = []

    x_proj_values.append(projDataset[0])
    y_proj_values.append(projDataset[1])
    z_proj_values.append(projDataset[2])

    fig = plt.figure(dpi = 120)
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x_proj_values, y_proj_values, z_proj_values)
    ax.set_xlabel('First Principal Component', fontweight="bold", fontsize=8)
    ax.set_ylabel('Second Principal Component', fontweight="bold", fontsize=8)
    ax.set_zlabel('Third Principal Component', fontweight="bold", fontsize=8)
    plt.show()



if __name__ == "__main__":

    images, information = load_npy_dataset("YaleB_32x32.npy")
    print(information)
    centImages = get_cent_dataset(images)
    covarianceMatrix = get_covariance_matrix(centImages)

    # 1 largest eigenvalue
    Lambda, U = get_eigenset(covarianceMatrix, 1)
    projImages = get_project_dataset(centImages, U)
    display_images(centImages, projImages, 16)
    display_ten_images(centImages)
    display_ten_images(projImages)

    # 3 largest eigenvalues
    Lambda, U = get_eigenset(covarianceMatrix, 3)
    projImages = get_project_dataset(centImages, U)
    display_ten_images(projImages)
    visual3D(projImages)

    # 10 largest eigenvalues
    Lambda, U = get_eigenset(covarianceMatrix, 10)
    projImages = get_project_dataset(centImages, U)
    display_ten_images(projImages)
    
