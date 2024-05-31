




def vote_menu():
    print("–" * 34)
    print("VOTE MENU")
    print("–" * 34)
    print("v: Vote")
    print("x: Exit")
    choice = input("Option: ").strip().lower()
    while True:
        if choice == 'v':
            break
        if choice == 'x':
            break
        choice = input("Invalid (v/x): ")
        choice = choice.strip().lower()
    return choice

def candidate_menu():
    print("–" * 34)
    print("CANDIDATE MENU")
    print("–" * 34)
    print("1: Bianca")
    print("2: Edward")
    print("3: Felicia")
    vote_choice = input("Candidate: ").strip()
    while not vote_choice.isdecimal() or int(vote_choice) not in range(1, 4):
        vote_choice = input("Invalid (1/2/3): ")
        vote_choice = vote_choice.strip()
    if vote_choice == '1':
        print('Voted Bianca')
    if vote_choice == '2':
        print('Voted Edward')
    if vote_choice == '3':
        print('Voted Felicia')
    return vote_choice

if __name__ == "__main__":

    def main():

        Bianca_vote = 0
        Edward_vote = 0
        Felicia_vote = 0
        Total = 0
        while True:


            m_choice = vote_menu()


            if m_choice == "v":
                votepoint = candidate_menu()

            elif m_choice == "x":
                print("–" * 57)
                print(f'Bianca - {Bianca_vote}, Edward - {Edward_vote}, Felicia - {Felicia_vote}, Total - {Total}')
                print("–" * 57)
                break

            if votepoint == '1':
                Bianca_vote += 1
                Total += 1
            elif votepoint == '2':
                Edward_vote += 1
                Total += 1
            elif votepoint == '3':
                Felicia_vote += 1
                Total += 1
    main()
