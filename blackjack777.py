import random

# 카드 덱 생성
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [rank +" "+ suit for suit in suits for rank in ranks]

# 카드 점수 계산
def calculate_score(cards):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
              '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    score = sum(values[card.split(' ')[0]] for card in cards)
    # A 처리: 11이 넘으면 1로 계산
    if score > 21 and any(card.startswith('A') for card in cards):
        score -= 10
    return score

# 카드 나눠주기
def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# 블랙잭 게임 실행
def blackjack():
    balance = 100  # 초기 잔액
    print("블랙잭 게임을 시작합니다!")
    print(f"소유 칩: {balance}")
    
    while balance > 0:
        print("\n새 게임!")
        print(f"현재 칩: {balance}")
        
        # 베팅 입력
        while True:
            try:
                bet = int(input("베팅 금액: "))
                if bet > balance:
                    print("가지고 있는 칩보다 더 많은 칩을 베팅했습니다.")
                elif bet < 1:
                    print("1개 이상의 칩을 베팅해야 합니다.")
                else:
                    break
            except ValueError:
                print("자연수를 입력해주세요.")
        
        random.shuffle(deck)
        player_cards = [deal_card(deck), deal_card(deck)]
        dealer_cards = [deal_card(deck), deal_card(deck)]
        
        print(f"\n당신의 카드: {player_cards}, 현재 점수: {calculate_score(player_cards)}")
        print(f"딜러의 첫번째 카드: {dealer_cards[0]}")
        
        # 플레이어의 선택
        game_over = False
        while not game_over:
            choice = input("카드를 더 받으시겠습니까? (y/n): ").lower()
            if choice == 'y':
                player_cards.append(deal_card(deck))
                print(f"현재 카드: {player_cards}, 현재 점수: {calculate_score(player_cards)}")
                if calculate_score(player_cards) > 21:
                    print("21점을 넘기셨군요! 패배하셨습니다!")
                    balance -= bet
                    game_over = True
            elif choice == 'n':
                game_over = True
                while calculate_score(dealer_cards) < 17:
                    dealer_cards.append(deal_card(deck))
                print(f"\n딜러의 카드: {dealer_cards}, dealer's score: {calculate_score(dealer_cards)}")
                
                player_score = calculate_score(player_cards)
                dealer_score = calculate_score(dealer_cards)
                if len(player_cards) == 3 and all(card.startswith('7') for card in player_cards):
                    print("와! 777! 베팅 금액의 10배를 얻습니다!")
                    balance += bet * 10
                    game_over = True
                elif dealer_score > 21 or player_score > dealer_score:
                    print("승리하셨습니다! 베팅한 금액의 두 배를 얻습니다!")
                    balance += bet
                elif player_score < dealer_score:
                    print("딜러가 승리하였습니다!")
                    balance -= bet
                else:
                    print("무승부! 베팅한 칩을 돌려받습니다!")
        
        # 게임 종료 조건 확인
        if balance <= 0:
            print("\n칩을 모두 잃으셨군요! 파산하였습니다!")
        else:
            play_again = input("한번 더 플레이하시겠습니까? (y/n): ").lower()
            if play_again != 'y':
                print(f"\n최종 점수: {balance}")
                break

blackjack()
