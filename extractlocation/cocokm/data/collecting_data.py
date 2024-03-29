import os
from pprint import pprint
from cocokm.data.google_apis import create_service

def collect_data(q,order=None,publishedAfter=None):
	CLIENT_SECRET_FILE = '/home/kmusw/바탕화면/Django/OIDC/extractlocation/cocokm/data/km-client-secret.json' # Oauth2 사용자 인증 정보 json파일 가져오기
	API_NAME = 'youtube'
	API_VERSION = 'v3'
	SCOPES = ['https://www.googleapis.com/auth/youtube']
	service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

	max_result = 30
	search_response = service.search().list(
		part = 'snippet',
		q = q,
		order = order,
		publishedAfter = publishedAfter,
		maxResults = max_result
	).execute()

	# 결과 보고시프면 pprint된 거 주석 풀면 됩니당 ! print말고 pprint로 찍어야 언니가 보기 편할거야 !!
	# pprint(search_response)

	video_list=[]
	for n in range(max_result):
		# pprint(search_response['items'][n]['id']['videoId'])
		video_id = search_response['items'][n]['id']['videoId']
		video_list.append(video_id)


	# video_response = service.videos().list(
	# 	part='contentDetails,statistics,snippet',
	# 	id=video_list
	# ).execute()

	# pprint(video_response)
	# return video_response
	return video_list

# collect_data('제주 vlog')
