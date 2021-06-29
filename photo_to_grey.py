from PIL import Image
import os



for file in os.listdir('original'):    # listdir= list 就是列出，dir 就是資料夾， 'original' 就是讀取original的資料夾。 for loop, 就是一個個東西拿出來變成清單"字串"（file)。
	if file.endswith('.jpeg'):	# file是一個字串，而endswith 就是檢查字串的結尾是否為 .jpeg。
		image_file = Image.open(os.path.join('original', file)) # os.path.join 就直接給它檔案資料夾和檔名，它就會變成正確的路徑。
		image_file = image_file.convert('L') # convert image to black and white
		image_file.save(os.path.join('results', file[:-5] + '_grey.png'))	# os.path.join 就直接給它檔案資料夾和檔名，它就會變成正確的路徑。



# 原本程式-3
# for file in os.listdir('original'):    # listdir= list 就是列出，dir 就是資料夾， 'original' 就是讀取original的資料夾。 for loop, 就是一個個東西拿出來變成清單"字串"（file)。
# 	if file.endswith('.jpeg'):	# file是一個字串，而endswith 就是檢查字串的結尾是否為 .jpeg。
# 		image_file = Image.open('original/' + file) # 'original/' 就是加上它的路徑，不然會找不到檔案。
# 		image_file = image_file.convert('L') # convert image to black and white
# 		image_file.save('results/' + file[:-5] + '_grey.png')	# [:-5] 清單分割法，就是.jpeg 不讀取，然而加上 _grey.png 然而存檔。



# 原本程式-2
# for file in os.listdir('.'):    # listdir= list 就是列出，dir 就是資料夾， '.' 就是目前所在的資料夾。 for loop, 就是一個個東西拿出來變成清單"字串"（file)。
# 	if file.endswith('.jpeg'):	# file是一個字串，而endswith 就是檢查字串的結尾是否為 .jpg。
# 		image_file = Image.open(file) # open colour image
# 		image_file = image_file.convert('L') # convert image to black and white
# 		image_file.save(file[:-5] + '_grey.png')	# [:-5] 清單分割法，就是.jpeg 不讀取，然而加上 _grey.png 然而存檔。


# 原本程式-1
# for file in os.listdir('.'):    # listdir= list 就是列出，dir 就是資料夾， '.' 就是目前所在的資料夾。 for loop, 就是一個個東西拿出來變成清單"字串"（file)。
# 	if file.endswith('.jpeg'):	# file是一個字串，而endswith 就是檢查字串的結尾是否為 .jpg。
# 		image_file = Image.open(file) # open colour image
# 		image_file = image_file.convert('L') # convert image to black and white
#  		image_file.save('result.png')	# 這兒會把全部的檔案存成一個檔案result.png，也就會覆蓋之前的檔案。


# 原本程式
# image_file = Image.open("nice.jpeg") # open colour image
# image_file = image_file.convert('L') # convert image to black and white
# image_file.save('result.png')

# for file in os.listdir('.'):    # listdir= list 就是列出，dir 就是資料夾， '.' 就是目前所在的資料夾。 for loop, 就是一個個東西拿出來變成清單"字串"（file)。
# 	if file.endswith('.jpeg'):	# file是一個字串，而endswith 就是檢查字串的結尾是否為 .jpg。
# 		print (file)