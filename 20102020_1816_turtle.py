import turtle
fred = turtle.Pen()
fred.shape("turtle")


run = 1
# to nam mowi ze nasz program ma dzialac dopuki w run jest 1
while run == 1:
    # tutaj dajemy komus kto uzywa naszego programu opcje wpisania co chce
    # zebysmy zrobili i zapisujemy to w 'command' (mozemy zmienic nazwe)
    command = input('Type a command (forward, left or right): ')
    # tutaj sprawdzamy co ktos wpisal 'command'
    if command == 'forward' or command == 'f': # moze wpisac forward albo f
        # robimy to samo ale teraz musi wpisac dystans
        distance = input('Type a distance: ')
        # int() robi ze to co ktos wpisal to napewno numer
        # np. jak ktos wpisze 5 to bedzie:
        # fred.forward(5)
        # a jak ktos wpisze 200 to bedzie:
        # fred.forward 200
        # jak ktos wpisze marek to bedzie:
        # fred.forward(marek)
        fred.forward(int(distance))
    elif command == 'left' or command == 'l':
        angle = input('Type an angle: ')
        fred.left(int(angle))
        # TODO ADD RIGHT
    else:
        # run bedzie 0 wiec nasz program nie bedzie dzialac
        run = 0 
