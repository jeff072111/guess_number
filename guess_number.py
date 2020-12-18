import random
start =input('請自行設定數字最小值: ')
end = input('請自行設定數字最大值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1  #相同於count = count + 1
	num = input('請猜一個數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		print('恭喜你！第', count,'次，終於猜對')
		break
	elif num > r:
		print('需要更小一點')
	elif num < r:
		print('需要更大一點')
	print('你已經猜了第', count,'次')