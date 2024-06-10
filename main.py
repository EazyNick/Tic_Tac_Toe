import random

class Tic_Tac_Toe:
 
    # 게임판 생성
    def __init__(self):
        self.board = [] # board 리스트 생성, self.를 붙여서 클래스 전체에서 쓰는 멤버로 만들어 줌

    # 게임판 초기화
    def create_board(self):
        self.board = []  # 보드 초기화
        for i in range(3):
            row = []    # 하나의 행 생성
            for j in range(3):
                row.append('*') # '*'로 채운 3개의 칸 만들기
            self.board.append(row)

    # 첫 플레이어 선택
    def select_first_player(self):
        if random.randint(0, 1) == 0:
            return 'X'  # 컴퓨터
        else:
            return 'O'  # 사용자  

    # 기호 표시
    def mark_spot(self, row, col, player):
        self.board[row][col] = player

    # 승리 상태 확인
    def is_win(self, player):
        n = len(self.board)

        # 행 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return True

        # 열 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return True

        # 오른쪽 대각선 확인
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return True

        # 왼쪽 대각선 확인
        win = True
        for i in range(n):
            if self.board[i][n-i-1] != player:
                win = False
                break
        if win:
            return True

        return False

    # 잔여 빈칸 여부 확인
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if item == '*':
                    return False
        return True

    # 플레이어 변경
    def next_player(self, player):
        if player == 'O':
            return 'X'
        else:
            return 'O'

    # 현재 게임판 상태 출력
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    # 게임 시작
    def start(self):
        # 새 게임판 생성
        self.create_board()
        self.show_board()

        # 첫 플레이어 선택
        player = self.select_first_player()

        # 게임 루프 시작
        while True:
            # 플레이어 안내
            if player == 'X':
                print("컴퓨터의 차례입니다.")
            else:
                print("사용자의 차례입니다.")

            # 현재 게임판 상태 출력
            self.show_board()

            # 사용자 입력 대기, 컴퓨터일 경우 랜덤 위치 반환
            if player == 'X':
                while True:
                    row, col = random.randint(1, 3), random.randint(1, 3)
                    if self.board[row - 1][col - 1] == '*':
                        break

                print("컴퓨터가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택했습니다.")
                print()
            else:
                row, col = list(map(int, input("선택할 빈칸의 위치를 입력하세요: ").split()))
                print("사용자가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택했습니다.")
                print()

            # row, col 입력값이 0,0인 경우 게임 종료
            if row == 0 and col == 0:
                break

            # 입력된 위치 표시
            self.mark_spot(row - 1, col - 1, player)
            self.show_board()

            # 현재 플레이어가 이겼는지 확인
            if self.is_win(player):
                if player == 'X':
                    print("YOU LOSE.")
                else:
                    print("YOU WIN!")
                break

            # 게임판 가득 참 확인
            if self.is_board_full():
                print("무승부")
                break

            # 플레이어 변경
            player = self.next_player(player)

        # 최종 게임판 출력
        print()
        self.show_board()

# 게임 생성
TTT = Tic_Tac_Toe()

# 게임 시작
TTT.start()
