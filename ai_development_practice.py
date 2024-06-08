
import pandas as pd
import Levenshtein


class LevenshteinChatBot:
    # 챗봇 객체 초기화, 데이터 파일을 로드
    def __init__(self, file_path):
        self.questions, self.answers = self._load_data(file_path)

    # CSV 파일에서 질문과 답변 데이터를 로드하는 메서드
    def _load_data(self, file_path):
        df = pd.read_csv(file_path)
        queries = df['Q'].tolist()
        responses = df['A'].tolist()
        return queries, responses

    # 입력 문장에 가장 적합한 답변을 찾는 메서드
    def get_best_response(self, user_input):
        # 입력 문장과 각 질문 간의 레벤슈타인 거리 계산
        distances = [Levenshtein.distance(user_input, query) for query in self.questions]

        # 가장 유사한 질문의 인덱스를 찾음
        closest_match_idx = distances.index(min(distances))

        # 가장 유사한 질문에 대한 답변 반환
        return self.answers[closest_match_idx], closest_match_idx

# CSV 파일 경로 지정
csv_file_path = 'ChatbotData.csv'

# 챗봇 객체 생성
bot = LevenshteinChatBot(csv_file_path)

# '종료' 입력이 들어올 때까지 사용자 입력에 따라 챗봇 응답을 출력하는 루프 실행
while True:
    user_input = input('You: ')
    if user_input.lower() == '종료':
        break
    response, index = bot.get_best_response(user_input)
    print(f'Chatbot: {response} (유사 질문 인덱스: {index})')

