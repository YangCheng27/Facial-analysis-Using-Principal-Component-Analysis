import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

def load_npy_dataset(filename):
    images = np.load(filename)
    information = f"{filename} is a {len(images)} (Number of sample images) x {len(images[0])} (Number of image features) array."
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
        dataset = dataset[i]
        for j in range(len(eigenVectors[0])):
            t = eigenVectors[:,j].T@dataset*eigenVectors[:,j]
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

if __name__ == "__main__":

    # 1. get image dataset and information
    images, information = load_npy_dataset("YaleB_32x32.npy")
    print(information)
    # 2. center the image dataset
    centImages = get_cent_dataset(images)
    # 3. get covariance matrix
    covarianceMatrix = get_covariance_matrix(centImages)
    # 4. get eigenset with largest 1 eigenvalues
    Lambda, U = get_eigenset(covarianceMatrix, 1)
    # 5. get projImages
    projImages = get_project_dataset(centImages, U)

    # 6. display one image with specific index
    display_images(centImages, projImages, 16)

    # 7. display ten orig images and ten proj images with largest 2 eigenvalues
    display_ten_images(centImages)
    display_ten_images(projImages)

    # get the same the images with different number of largest eigenvalues
    Lambda, U = get_eigenset(covarianceMatrix, 6)
    projImages = get_project_dataset(centImages, U)
    display_ten_images(projImages)

    Lambda, U = get_eigenset(covarianceMatrix, 10)
    projImages = get_project_dataset(centImages, U)
    display_ten_images(projImages)

    Lambda, U = get_eigenset(covarianceMatrix, 14)
    projImages = get_project_dataset(centImages, U)
    display_ten_images(projImages)

    Lambda, U = get_eigenset(covarianceMatrix, 18)
    projImages = get_project_dataset(centImages, U)
    display_ten_images(projImages)