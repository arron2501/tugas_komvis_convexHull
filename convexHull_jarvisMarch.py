import time, cv2 as cv, numpy as num, scan_jarvisMarch as sj

delta_time = 0
chain_code = []
def findCC(img,X,Y):
    global chain_bitmap, chain_code, count
    if (img[X][Y+1] == 255):
        if (chain_bitmap[X][Y+1] == 0):
            newX = X
            newY = Y+1
            chain_code.append([newX,newY])
            count += 1
            chain_bitmap [X][Y+1] = 255
            findCC(img,newX,newY)

    if (img[X-1][Y] == 255):
        if (chain_bitmap[X-1][Y] == 0):
            newX = X-1
            newY = Y
            chain_bitmap[X-1][Y] = 3
            chain_code.append([newX,newY])
            count += 1
            findCC(img,newX,newY)

    if (img[X][Y-1] == 255):
        if (chain_bitmap[X][Y-1] == 0):
            newX = X
            newY = Y-1
            chain_code.append([newX,newY])
            count += 1
            chain_bitmap[X][Y-1] = 255
            findCC(img,newX,newY)

    if (img[X+1][Y] == 255):
        if (chain_bitmap[X+1][Y] == 0):
            newX = X+1
            newY = Y
            chain_code.append([newX,newY])
            count += 1
            chain_bitmap[X+1][Y] = 255
            findCC(img,newX,newY)

    if (img[X-1][Y+1] == 255):
        if (chain_bitmap[X-1][Y+1] == 0):
            newX = X-1
            newY = Y+1
            chain_code.append([newX,newY])
            count += 1
            chain_bitmap[X-1][Y+1] = 255
            findCC(img,newX,newY)

    if (img[X-1][Y-1] == 255):
        if (chain_bitmap[X-1][Y-1] == 0):
            newX = X-1
            newY = Y-1
            chain_code.append([newX,newY])
            count += 1
            chain_bitmap[X-1][Y-1] = 255
            findCC(img,newX,newY)

    if (img[X+1][Y-1] == 255):
        if (chain_bitmap[X+1][Y-1] == 0):
            newX = X+1
            newY = Y-1
            chain_code.append([newX,newY])
            count += 1
            chain_bitmap[X+1][Y-1] = 255
            findCC(img,newX,newY)

    if (img[X+1][Y+1] == 255):
        if (chain_bitmap[X+1][Y+1] == 0):
            newX = X+1
            newY = Y+1
            chain_bitmap[X+1][Y+1] = 8
            chain_code.append([newX,newY])
            count += 1
            findCC(img,newX,newY)

original_img = cv.imread('kuda.png', cv.IMREAD_GRAYSCALE)
(thresh, binary_img) = cv.threshold(original_img, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imwrite('kuda_binary.png', binary_img)

kernel = num.ones((3,3),num.uint8)

edges2 = cv.Canny(binary_img,100,200)
edges = cv.Canny(binary_img,100,100)

WhitePixels = num.array(num.where(edges2==255))
firstWhitePixels = WhitePixels[:,0]
startingPoint = firstWhitePixels
x = startingPoint[0]
y = startingPoint[1]
count = 0
chain_bitmap = num.zeros_like(edges2)
chain_bitmap[x][y] = 9

findCC(edges2,x,y)

chain_code = num.array(chain_code)

start_time = time.time()
convex_hull = sj.jarvis_march(chain_code)
delta_time = time.time() - start_time   
print("Time Executed: " + str(delta_time))

sj.scatter_plot(convex_hull, chain_code)

cv.waitKey(0)
