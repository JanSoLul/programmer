def solution(new_id):
	new_id = new_id.lower()
	save_id = ''
	for i in new_id:
		if i.isalnum() or i=='-' or i=='_' or i=='.':
			save_id += i
	answer = ''
	save_len = len(save_id)
	for i in range(save_len):
		if save_id[i] == '.':
			if i==0 or i==save_len-1 or save_id[i-1]=='.':
				continue
		answer += save_id[i]
	if answer == '':
		answer += 'aaa'
	elif len(answer) > 15:
		answer = answer[:15]
	if answer[-1] == '.':
		answer = answer[:-1]
	if len(answer) < 3:
		for _ in range(3-len(answer)):
			answer += answer[-1]
                
	return answer